from ast import Lambda

import tkinter as tk
from tkinter import messagebox

from matplotlib import text

from preformance import Preformance
from data_handler import load_preformance, save_preformance

class PreformanceGui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Student Preformance Managment System")
        self.root.geometry("450x600")
        self.root.config(bg="#1e1e2f")

        self.input_frame = tk.Frame(self.root, bg="#1e1e2f")
        self.input_frame.pack(pady=20)

        self.name_label = tk.Label(self.input_frame, text="Name:", bg="#1e1e2f", fg="white")
        self.name_entry = tk.Entry(self.input_frame)
        self.name_label.grid(row=0, column=0, padx=5, pady=5)
        self.name_entry.grid(row= 0, column=1, padx=5, pady=5)

        self.marks_label = tk.Label(self.input_frame, text="Marks:", bg="#1e1e2f", fg="white")
        self.marks_entry = tk.Entry(self.input_frame)
        self.marks_label.grid(row=1, column=0, padx=5, pady=5)
        self.marks_entry.grid(row=1, column=1, padx=5, pady=5)

        self.button_frame = tk.Frame(self.root, bg="#1e1e2f")
        self.button_frame.pack(pady=20)

        self.add_button = tk.Button(
            self.button_frame,
            text="Add Preformance",
            command=self.add_preformance
        )
        self.add_button.pack(pady=10)

        self.view_button = tk.Button(
            self.button_frame,
            text="View Preformance",
            command=self.view_preformance
        )
        self.view_button.pack(pady=10)

        self.search_button = tk.Button(
            self.button_frame,
            text="Search Preformance",
            command=self.search_preformance
        )
        self.search_button.pack(pady=10)

        self.delete_button = tk.Button(
            self.button_frame,
            text="Delete Preformance",
            command=self.delete_preformance
        )
        self.delete_button.pack(pady=10)

        self.average_button = tk.Button(
            self.button_frame,
            text="Calculate Average",
            command=self.calculate_average
        )
        self.average_button.pack(pady=10)

        self.topper_button = tk.Button(
            self.button_frame,
            text="Show Topper",
            command=self.show_topper
        )
        self.topper_button.pack(pady=10)

        self.preformance_listbox = tk.Listbox(self.root, width=50)
        self.preformance_listbox.pack(pady=10)



    def add_preformance(self):
        name = self.name_entry.get()
        marks = self.marks_entry.get()

        if not name or not marks:
            messagebox.showerror(
                "Error",
                "All fields are required"
            )
            return
        
        try:
            marks = float(marks)
        except ValueError:
            messagebox.showerror(
                "Error", 
                "Marks must be a Number"
            )
            return


        preformance = Preformance(
            name,
            marks
        )

        preformances = load_preformance()

        preformances.append(preformance.to_dict())
        save_preformance(preformances)

        messagebox.showinfo(
            "Info",
            "Preformance added Successfully"
        )

        self.name_entry.delete(0, tk.END)
        self.marks_entry.delete(0, tk.END)


    def view_preformance(self):
        self.preformance_listbox.delete(0, tk.END)


        preformances = load_preformance()

        for preformance in preformances:
            self.preformance_listbox.insert(
                tk.END,
                f"{preformance['name']} - {preformance['marks']}"
            )

    def search_preformance(self):
        self.preformance_listbox.delete(0, tk.END)
        
        preformances = load_preformance()

        name = self.name_entry.get()

        for preformance in preformances:
            if preformance['name'] == name:
                self.preformance_listbox.insert(
                    tk.END,
                    f"{preformance['name']} - {preformance['marks']}"
                )

    def delete_preformance(self):
        try:
            preformances = load_preformance()
            selected_index = self.preformance_listbox.curselection()[0]

            remove = preformances.pop(selected_index)
            save_preformance(preformances)

            messagebox.showinfo("Deleted", f"{remove['name']} - {remove['marks']} deleted!")

            self.view_preformance()
        except IndexError:
            messagebox.showerror("Error", "Please select an item to deleted")


    def calculate_average(self):
        preformances = load_preformance()

        if not preformances:
            messagebox.showinfo("Info", "No student records found.")
            return

        total_marks = sum(
            preformance['marks'] for preformance in preformances
        )

        average_marks = total_marks / len(preformances)

        self.preformance_listbox.delete(0, tk.END)

        self.preformance_listbox.insert(
            tk.END,
            f"Average Marks: {average_marks:.2f}"
        )

    def show_topper(self):
        preformances = load_preformance()

        if not preformances:
            messagebox.showinfo("Info", "No student records found.")
            return

        topper = max(preformances, key=lambda x: x['marks'])

        self.preformance_listbox.delete(0, tk.END)
        self.preformance_listbox.insert(
            tk.END,
            f"Topper: {topper['name']} - {topper['marks']}"
        )

    def run(self):
        self.root.mainloop() 


    

    




