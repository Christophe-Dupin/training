
from .repositories import AdresseRepository, PersonnRepository

from .database import db


class Personne:
    objects = PersonnRepository(db)

    def __init__(self, name, forename, phone_number, email, adresse):
        self.name = name
        self.forename = forename
        self.phone_number = phone_number
        self.email = email
        self.adresse = adresse
        self.id = None


class Adresse:
    objects = AdresseRepository(db)

    def __init__(self, street, country, postal_code, number, persons):
        self.street = street
        self.country = country
        self.postal_code = postal_code
        self.number = number
        self.persons = persons
        self.id = None
        self


if __name__ == "__main__":
    # new_adresse = AdresseRepository.create()
    new_personne = Personne.objects.create(
        "Dupin",
        "Christophe",
        "0644182848",
        "mail@moi.com",
        "189 avenue Jean Jaures",
    )
