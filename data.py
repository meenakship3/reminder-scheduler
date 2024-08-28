from tkinter import messagebox
import csv

import pandas


class Data:
    def save_data(self, template, date, time, subject):
        # fields = ["template", "date", "time", "subject", "status"]
        row = [template, date, time, subject, "not done"]
        if len(template) == 0 or len(date) == 0 or len(time) == 0 or len(subject) == 0:
            messagebox.showwarning(title="Oops", message="Make sure you've filled in all the fields.")
        else:
            # try:
            with open("data.csv", "a") as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(row)
            # except FileNotFoundError:
            #     with open("data.csv", "w") as csvfile:
            #         csvwriter = csv.writer(csvfile)
            #         csvwriter.writerow(fields)
            #         csvwriter.writerow(row)

    def update_status(self, index):
        for i in index:
            data = pandas.read_csv('data.csv')
            data['status'] = data['status'].astype(str)
            data._set_value(i, 'status', 'done')
            data.to_csv('data.csv', index=False)
