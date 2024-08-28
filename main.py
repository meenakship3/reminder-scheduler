from ui import ReminderInterface
from data import Data
from message_sender import MessageSender

data = Data()
reminder_interface = ReminderInterface()
message_sender = MessageSender()

reminder_interface.add_button.config(command=lambda: [data.save_data(
                                                                reminder_interface.get_template(),
                                                                reminder_interface.get_date(),
                                                                reminder_interface.get_time(),
                                                                reminder_interface.get_subject()
                                                                )
                                                                ,reminder_interface.clear_fields()])

def send_message():
    data.update_status(message_sender.notification())

send_message()

reminder_interface.window.mainloop()
