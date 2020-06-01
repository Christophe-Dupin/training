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
    data = {
        "name": b.name,
        "forname": b.forename,
        "email": b.email,
    }
    # b.objects.create(data)
    a = b.objects.get_all()
    c = b.objects.select_by_field_name("name")
    for r in c:
        print(r)
