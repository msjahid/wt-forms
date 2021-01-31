from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from wtforms import SelectField
from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired
from flask import session
from wtforms import Form, IntegerField, FloatField, StringField
from datetime import date
import pandas as pd
from flask import request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:jahid0439@localhost/dushanbe'
app.config['SECRET_KEY'] = 'msjahid-Ludwig'

db = SQLAlchemy(app)
df = pd.read_csv("C:/Users/User/Documents/bill1-ew.csv")

class earthWork(db.Model):
    __tablename__ = 'earth_work'
    No = db.Column(db.Integer, primary_key=True)
    Name_materials = db.Column(db.String(2000))
    Units = db.Column(db.String(7))
    Quantity = db.Column(db.Float)

class Form(FlaskForm):
    No = IntegerField('No')
    Name_materials = SelectField('Name_materials', choices=[], validators=[DataRequired()])
    Units = StringField('Units')
    Quantity = FloatField('Quantity')
    Date = DateField('date',  validators=[DataRequired()], format='%Y-%m-%d')
    Work_Done = FloatField('Work_Done')

@app.route('/')
def index():
    form = Form()
    # form.No.choices = [(No.No) for No in earthWork.query.all()]
    form.Name_materials.choices = [(Name_materials.Name_materials) for Name_materials in earthWork.query.all()]
    # form.Units.choices = [(Units.Units) for Units in earthWork.query.all()]
    # form.Quantity.choices = [(Quantity.Quantity) for Quantity in earthWork.query.all()]
    # form.Name_materials =
    Units = 'kg'
    # form.Quantity =
    # print(dict(form.No.choices).get(form.No.data))
    # result_dict = [u.__dict__ for u in earthWork.query.all()]
    # print(result_dict["Name_materials"])

    return render_template('index.html', form=form)
if __name__ == '__main__':
    app.run(debug=True)
