from app import db


class Employee(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "employee"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    full_name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    # registered_on = db.Column(db.DateTime, nullable=False)
    # admin = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, email, full_name, address, admin=False):
        self.email = email
        self.full_name = full_name
        self.address = address
        # self.registered_on = datetime.datetime.now()
        # self.admin = admin

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Employee.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "".format(self.email)
