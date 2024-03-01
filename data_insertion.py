""" Manage the subscribers data. """
from datetime import datetime

from pandas import DataFrame


class SubscriberManager:
    """
    Manage gym subscribers data

    Methods:
    add_subscription : Add a new subscriber to the database.
    """
    def __init__(self) -> None:
        self.sub_data = {
            "Nome": [],
            "Cognome": [],
            "Data di nascita": [],
            "Data di iscrizione": [],
            "Codice fiscale": [],
            "Certificato medico": [],
            "Scadenza certificato medico": [],
            "Pagamenti mensili":[],
            "Quantita' pagamento mensile": [],
            "Corso di iscrizione": []
        }

    def add_subscription(
        self,
        name: str,
        surname: str,
        byrthday: str,
        subscription_date: str,
        tax_code: str,
        medical_certificate: str,
        medical_certificate_expiration_date: str,
        monthly_payment: str,
        monthly_payment_amount: str,
        enrolment_course: str
    ) -> None:
        """
        Add a new subscriber to the data dictionary.

        Parameters
        ----------
        name : str, The subscriber's name.
        surname : str, The subscriber's surname.
        byrthday : str, The subscriber's byrthday.
        subscription_date : str, The subscriber's subscription date.
        tax_code : str, The subscriber's tax code.
        medical_certificate : str, The subscriber's medical certificate.
        medical_certificate_expiration_date : str, The subscriber's'
        medical certificate expiration date.
        monthly_payment : str, The subscriber's monthly payment.
        monthly_payment_amount : str, The subscriber's monthly payment amount.
        enrolment_course : str, The subscriber's enrolment course.
        """
        self.sub_data["Codice fiscale"].append(tax_code)
        self.sub_data["Nome"].append(name)
        self.sub_data["Cognome"].append(surname)
        self.sub_data["Data di nascita"].append(byrthday)
        self.sub_data["Data di iscrizione"].append(subscription_date)
        self.sub_data["Certificato medico"].append(medical_certificate)
        self.sub_data["Scadenza certificato medico"].append(
            medical_certificate_expiration_date
        )
        self.sub_data["Pagamenti mensili"].append(monthly_payment)
        self.sub_data["Quantita' pagamento mensile"].append(
            monthly_payment_amount
        )
        self.sub_data["Corso di iscrizione"].append(enrolment_course)


def create_excel_file(data: dict, path: str):
    """
    Create an excel file with the subscribers data.

    Parameters
    ----------
    data : dict, The subscribers data.
    path : str, The path where the file will be saved.
    """
    df = DataFrame(data)
    df.to_excel(path, index=False)
