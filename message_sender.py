import os
from dotenv import load_dotenv
from twilio.rest import Client
from datetime import *
import pandas

load_dotenv()

ACCOUNT_SID = os.getenv("ACCOUNT_SID")
TWI_AUTH_TOKEN = os.getenv("TWI_AUTH_TOKEN")
FROM_NUMBER = os.getenv("FROM_NUMBER")
TO_NUMBER = os.getenv("TO_NUMBER")

class MessageSender:

    def notification(self):
        today = datetime.today()
        formatted_date = today.strftime("%d/%m/%y")

        data = pandas.read_csv('data.csv')
        print(data)
        todays_reminders = (data.loc[data['date'] == formatted_date])
        print(f"todays_reminders = \n{todays_reminders}")

        for i in range(0, len(todays_reminders)):
            template = todays_reminders.iat[i, 0]
            subject = todays_reminders.iat[i, 3]
            status = todays_reminders.iat[i, 4]
            if template == "Submission reminder" and status != "done":
                with open('templates/submission-template.txt', 'r') as template_file:
                    template = template_file.read()
                    content = template.replace('[subject]', f"{subject}")
                client = Client(ACCOUNT_SID, TWI_AUTH_TOKEN)
                message = client.messages.create(
                    body=f'{content}',
                    from_=FROM_NUMBER,
                    to=TO_NUMBER
                )
                print(message.status)

        return todays_reminders.index.values.tolist()
