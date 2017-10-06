from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, name, store_id):
        self.name = name
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'id': self.store_id, 'items': [item.json() for item in self.items.all()]}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() # SELECT * FROM stores WHERE name=name LIMIT 1 (first row only)


    def save_to_db(self):  #used for UPDATE and INSERT
        db.session.add(self)
        db.session.commit()


    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
