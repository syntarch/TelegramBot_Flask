from bot import db


class Enzyme(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, nullable=False)
    catalogue_number = db.Column(db.String(64), index=True, unique=True, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Enzyme {self.name}>'
