from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkmacosx import Button

class ReminderInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Reminder Scheduler")
        self.window.config(padx=20, pady=20, bg="Lavender")

        self.canvas = Canvas(width=300, height=200, bg="Lavender", highlightthickness=0)
        self.flower_img = PhotoImage(file="images/flower.png")
        self.canvas.create_image(100, 120, image=self.flower_img)
        self.canvas.grid(column=1, row=0)

        self.reminder_scheduler_label = Label(text="Schedule Upcoming Reminders", fg="slate blue", bg="Lavender", font=("Helvetica", 20, "bold"))
        self.reminder_scheduler_label.grid(column=0, row=1, pady=20, columnspan=2)

        self.template_label = Label(text="Template: ", fg="slate blue", bg="Lavender", font=("Helvetica", 15, "bold"))
        self.template_label.grid(column=0, row=2)
        self.template_dropdown = Combobox(self.window, width=30)
        self.template_dropdown.set('Pick a template')
        self.template_dropdown['values'] = [
            "Submission reminder",
            "Laptop reminder",
            "Uniform reminder"
        ]
        self.template_dropdown.grid(column=1, row=2)

        self.date_label = Label(text="Reminder date: ", fg="slate blue", bg="Lavender", font=("Helvetica", 15, "bold"))
        self.date_label.grid(column=0, row=3)
        self.date_input = Entry(highlightbackground="Lavender")
        self.date_input.grid(column=1, row=3, ipadx=55)

        self.time_label = Label(text="Reminder time: ", fg="slate blue", bg="Lavender", font=("Helvetica", 15, "bold"))
        self.time_label.grid(column=0, row=4)
        self.time_input = Entry(highlightbackground="Lavender")
        self.time_input.insert(0, "Default")
        self.time_input.grid(column=1, row=4, ipadx=55)

        self.subject_label = Label(text="Subject: ", fg="slate blue", bg="Lavender", font=("Helvetica", 15, "bold"))
        self.subject_label.grid(column=0, row=5)
        self.subject_dropdown = Combobox(self.window, width=30)
        self.subject_dropdown.set('Pick a subject')
        self.subject_dropdown['values'] = [
            "Income Tax",
            "Subject 2",
            "Subject 3",
            "Subject 4",
            "Subject 5",
            "Subject 6"
        ]
        self.subject_dropdown.grid(column=1, row=5)

        self.add_button = Button(text="Add to Calendar", borderless=True, width=300, bg="slate blue", fg="white")
        self.add_button.grid(row=6, column=1, pady=10)


    def get_template(self):
        return self.template_dropdown.get()

    def get_date(self):
        return self.date_input.get()

    def get_time(self):
        return self.time_input.get()

    def get_subject(self):
        return self.subject_dropdown.get()

    def clear_fields(self):
        self.template_dropdown.set('Pick a template')
        self.date_input.delete(0, 'end')
        self.time_input.delete(0, 'end')
        self.subject_dropdown.set('Pick a subject')
        messagebox.showinfo(message="Your details have been added successfully!")




