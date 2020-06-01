"""[summary]."""
from .database import db
from .repositories import PersonnRepository


class Personne:
    """[summary]."""

    objects = PersonnRepository(db)

    def __init__(self, name, forename, email):
        """[summary].

        Arguments:
            name {[type]} -- [description]
            forename {[type]} -- [description]
            email {[type]} -- [description]
        """
        self.name = name
        self.forename = forename
        self.email = email
        self.id = None


if __name__ == "__main__":
    b = Personne("antoine", "Dupin", "antoine@moi.fr")
    b.objects.create(b.name, b.forename, b.email)
    a = b.objects.get_all()
