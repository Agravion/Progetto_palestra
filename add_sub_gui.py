from datetime import datetime
import tkinter as tk
from tkinter.filedialog import asksaveasfile
from tkinter.messagebox import askyesno

from tabulate import tabulate
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from data_insertion import SubscriberManager, create_excel_file

class PlaceholderEntry(ttk.Entry):
    def __init__(self, master=None, placeholder="", *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.placeholder = placeholder
        self.placeholder_color = "grey"
        self.normal_color = self["foreground"]

        self.bind("<FocusIn>", self.on_focus_in)
        self.bind("<FocusOut>", self.on_focus_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self.config(foreground=self.placeholder_color)

    def on_focus_in(self, event):
        if self.get() == self.placeholder:
            self.delete(0, tk.END)
            self.config(foreground=self.normal_color)

    def on_focus_out(self, event):
        if not self.get():
            self.put_placeholder()


class Gui:
    def __init__(self, parent):
        self.parent = parent
        self.root = parent.root
        self.style = parent.style
        self.sub_manager = SubscriberManager()
        self.fields = {
            "name": ["Nome", tk.StringVar()],
            "surname": ["Cognome", tk.StringVar()],
            "byrthday": ["Data di nascita", tk.StringVar()],
            "subscription_date": ["Data di iscrizione", tk.StringVar()],
            "tax_code": ["Codice fiscale", tk.StringVar()],
            "medical_certificate": ["Certificato medico", tk.StringVar()],
            "medical_certificate_expiration_date": [
                "Scadenza certificato medico", tk.StringVar()
            ],
            "monthly_payment": ["Pagamenti mensili", tk.StringVar()], 
            "monthly_payment_amount": [
                "Quantita' pagamento mensile", tk.StringVar()
            ],
            "enrolment_course": ["Corso di iscrizione", tk.StringVar()]
        }

    def save_file(self):
        """ Save the data to an excel file. """
        today = datetime.today()
        f = asksaveasfile(
            initialfile = f"iscritti_{today.month}_{today.year}",
            defaultextension=".xlsx",
            filetypes=[("Excel documents","*.xlsx")]
        )
        file_name = f.name
        f.close()
        create_excel_file(data=self.sub_manager.sub_data, path=file_name)

    def add_user(self):
        """ Add a new user to the data dict. """

        headers = [value[0] for value in self.fields.values()]
        data = [[value[1].get() for value in self.fields.values()]]
        message = "Confermi i dati inseriti?\n\n"

        for i, header in enumerate(headers):
            message += f"{header}: {data[0][i]}\n--------------------------\n"

        answer = askyesno(
            title="Conferma",
            message=message
        )
        if not answer:
            return None
        self.sub_manager.add_subscription(
            name=self.fields["name"][1].get(),
            surname=self.fields["surname"][1].get(),
            byrthday=self.fields["byrthday"][1].get(),
            subscription_date=self.fields["subscription_date"][1].get(),
            tax_code=self.fields["tax_code"][1].get(),
            medical_certificate=self.fields["medical_certificate"][1].get(),
            medical_certificate_expiration_date=self.fields[
                "medical_certificate_expiration_date"
            ][1].get(),
            monthly_payment=self.fields["monthly_payment"][1].get(),
            monthly_payment_amount=self.fields[
                "monthly_payment_amount"
            ][1].get(),
            enrolment_course=self.fields["enrolment_course"][1].get()
        )

    def go_back(self):
        """ Returns in main page. """
        [widget.pack_forget() for widget in list(self.root.children.values())]
        self.parent.build_gui_widgets()

    def build_gui_widgets(self):
        for _, v in self.fields.items():
            entry = PlaceholderEntry(
                self.root,
                placeholder=v[0],
                bootstyle=PRIMARY,
                textvariable=v[1],
                width=150
            )
            entry.pack(padx=100, pady=20)

        b2 = ttk.Button(
            self.root,
            text="Salva utente",
            bootstyle=(INFO, OUTLINE),
            command=self.add_user
        )
        b2.pack(padx=5, pady=10)

        b1 = ttk.Button(
            self.root,
            text="Salva excel",
            bootstyle=SUCCESS,
            command=self.save_file
        )
        b1.pack(padx=5, pady=10)

        b1 = ttk.Button(
            self.root,
            text="Torna indietro",
            bootstyle=SUCCESS,
            command=self.go_back
        )
        b1.pack(padx=5, pady=10)
