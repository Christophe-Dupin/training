
class PersonnRepository:
    """[summary]."""

    def __init__(self, db):
        """[summary].

        Arguments:
            db {[type]} -- [description]
        """
        self.db = db

    def get_all(self):
        """[summary]."""
        rows = self.db.query("SELECT * FROM personne ")
        return rows

    def create(self, name, forname, email):
        """[summary]."""
        rows = self.db.query(
            """INSERT INTO personne (name, forname,email) VALUES (:name, :forname,:email)""",
            name=name, forname=forname, email=email
        )

    def select_by_field_name(self, field):
        """[summary]."""
        rows = self.db.query("""SELECT (field) FROM personne VALUES (%s)""")
        return
