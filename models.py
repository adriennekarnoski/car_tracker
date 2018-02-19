from manage import db, app
from wtforms_alchemy import ModelForm, ModelFormField


class Vehicle(db.Model):
    __tablename__ = 'vehicle'

    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    make = db.Column(db.String(30))
    model = db.Column(db.String(30))
    mileage = db.Column(db.Integer)
    vin = db.Column(db.Integer)
    license = db.Column(db.String(30))


class Maintenance(db.Model):
    __tablename__ = 'maintenance'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(30))
    mileage = db.Column(db.Integer)
    service = db.Column(db.String(30))
    description = db.Column(db.Text)
    cost = db.Column(db.Float)
    performed = db.Column(db.String(64))
    product = db.relationship("Product", uselist=False, backref="maintenance")


class Product(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True)
    maintenance_id = db.Column(db.Integer, db.ForeignKey('maintenance.id'))
    category = db.Column(db.String(30))
    description = db.Column(db.String(64))
    number = db.Column(db.Integer)
    brand = db.Column(db.String(64))
    notes = db.Column(db.Text)


class VehicleForm(ModelForm):
    class Meta:
        model = Vehicle


class MaintenanceForm(ModelForm):
    class Meta:
        model = Maintenance


class ProductForm(ModelForm):
    class Meta:
        model = Product

    maintenance = ModelFormField(MaintenanceForm)


class Preventive(db.Model):
    __tablename__ = 'preventive'

    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String(30))
    mileage = db.Column(db.Integer)
    service = db.Column(db.String(64))
    description = db.Column(db.Text)


class Periodic(db.Model):
    __tablename__ = 'periodic'

    id = db.Column(db.Integer, primary_key=True)
    due = db.Column(db.Integer)
    service = db.Column(db.String(30))
    complete = db.Column(db.Boolean, default=False)
