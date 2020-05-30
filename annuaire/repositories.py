class PersonnRepository:
    def __init__(self, db):
        self.db = db

    def get_all(self):
        pass

    def create(self, name, forename, phone_number, email, adresse):
        pass

    def save(self, personne):
        pass

    def remove(self, personne):
        pass


class AdresseRepository:
    def __init__(self, db):
        self.db = db

    def create(self, street, country, postal_code, number, persons):
        pass

    def save(self, adresse):
        pass
