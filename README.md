## 📆 reminder-scheduler 

A Python project that sends reminders using Twilio's API. It has a GUI (built using Tkinter) to help users set up reminders. The idea for this project came up to help students stay on top of college submissions.

In the GUI, the user can pick what kind of a reminder they would like to receive, along with the date the reminder is to be sent. The program then picks the appropriate template which contains the message to be sent with some dynamic fields (including what subject the submission is for). The message is then sent on the scheduled date.

## 🧰 modules, libraries and APIs used
- Tkinter
- Datetime
- Pandas
- Twilio

## current status
🚧 **Work in Progress**: This project is actively being developed and improved, new features will be added soon. Check back for updates!

## ✨ features
- [x] GUI to add reminders
- [x] Send SMS reminders via Twilio
- [ ] Send WhatsApp reminders via Twilio
- [ ] Update templates and subjects
- [ ] Time-based reminders
- [ ] Automated check for reminders
- [ ] Error handling

## ⚙️ installation
1. Clone the repository
2. Set up a data.csv with the following columns - (template,date,time,subject,status)
3. Run the program each time you would like to add a reminder and check for a reminder

## 🖼️ screenshots
<img width="457" alt="GUI" src="https://github.com/user-attachments/assets/ec96e7e1-ea34-4850-8f91-d80bb6d35f23">
<img width="457" alt="Reminder Message" src="https://github.com/user-attachments/assets/b548ba4b-e8e2-4e53-bf7c-f120ac74dc81">









