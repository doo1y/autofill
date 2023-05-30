import tkinter as tk
from tkinter import ttk
from tkinter import font
from actions.fill_template import fill_template as fill


class TkApp(tk.Tk):
    # __init__ function for class tkinterApp
    def __init__(self):
        # __init__ function for class Tk
        tk.Tk.__init__(self)

        self.template_name_label = ttk.Label(self, text= "Template Name: ")
        self.recipient_name_label = ttk.Label(self, text="Recipient Name: ")
        self.company_name_label = ttk.Label(self, text="Company Name: ")
        self.technology_label = ttk.Label(self, text="Technology: ")
        self.listing_source_label = ttk.Label(self, text="Listing Source:")

        self.template_name_entry = ttk.Entry(self)
        self.recipient_name_entry = ttk.Entry(self)
        self.company_name_entry = ttk.Entry(self)
        self.technology_entry = ttk.Entry(self)
        self.listing_source_entry = ttk.Entry(self)

        self.template_name_label.grid(column=0, row=1)
        self.recipient_name_label.grid(column=0, row=2)
        self.company_name_label.grid(column=0, row=3)
        self.technology_label.grid(column=0, row=4)
        self.listing_source_label.grid(column=0, row=5)

        self.template_name_entry.grid(column=1, row=1)
        self.recipient_name_entry.grid(column=1, row=2)
        self.company_name_entry.grid(column=1, row=3)
        self.technology_entry.grid(column=1, row=4)
        self.listing_source_entry.grid(column=1, row=5)

        self.create_button = ttk.Button(
            self, text="Autofill", command=self.fill_template
        )
        self.create_button.grid(columnspan=2, row=6)



    def fill_template(self) -> None:
        temp_name = self.template_name_entry.get()
        re = self.recipient_name_entry.get()
        co = self.company_name_entry.get()
        li = self.listing_source_entry.get()
        te = self.technology_entry.get()

        fill(temp_name=temp_name, re=re, co=co, li=li, te=te)
