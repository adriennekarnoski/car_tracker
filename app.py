from flask import Flask, redirect, url_for, request, render_template
import os
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, TextField
from wtforms.validators import DataRequired
from sqlalchemy import desc

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.secret_key = os.environ.get('SECRET_KEY')
db = SQLAlchemy(app)


class MyForm(FlaskForm):
    date = StringField('date', validators=[DataRequired()])
    mileage = IntegerField('mileage', validators=[DataRequired()])
    service = StringField('service', validators=[DataRequired()])
    description = TextField('cleared_date', validators=[DataRequired()])
    cost = FloatField('cost', validators=[DataRequired()])
    performed = StringField('performed', validators=[DataRequired()])

from models import Maintenance, Preventive, Periodic, MaintenanceForm, ProductForm, Vehicle, VehicleForm

 
@app.route('/')
def home():
    vehicle = db.session.query(Vehicle).get(1)
    return render_template('index.html', vehicle=vehicle)


@app.route('/vehicle', methods=['GET', 'POST'])
def vehicle():
    form = VehicleForm()
    if request.method == 'POST':
        year = request.form['year']
        make = request.form['make']
        model = request.form['model']
        mileage = request.form['mileage']
        vin = request.form['vin']
        license = request.form['license']
        v = Vehicle(
            year=year,
            make=make,
            model=model,
            mileage=mileage,
            vin=vin,
            license=license,
            )
        db.session.add(v)
        db.session.commit()
        return redirect(url_for('home'))
    # if len(Vehicle.query.all()) != 0:
    #     records = Maintenance.query.order_by(desc(Maintenance.id)).all()
    return render_template('vehicle.html', form=form)


@app.route('/add', methods=['GET', 'POST'])
def add():
    # form = MyForm()
    form = MaintenanceForm()
    if request.method == 'POST':
        date = request.form['date']
        mileage = request.form['mileage']
        service = request.form['service']
        description = request.form['description']
        cost = request.form['cost']
        performed = request.form['performed']
        m = Maintenance(
            date=date,
            mileage=mileage,
            service=service,
            description=description,
            cost=cost,
            performed=performed,
            )
        db.session.add(m)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template(
        'add_entry.html',
        form=form)


@app.route('/record')
def record():
    if len(Maintenance.query.all()) != 0:
        records = Maintenance.query.order_by(desc(Maintenance.id)).all()
    return render_template('record.html', records=records)

if __name__ == '__main__':
    app.run()
