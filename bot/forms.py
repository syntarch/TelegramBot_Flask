from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class AddForm(FlaskForm):
    name = StringField("Enzyme name", validators=[DataRequired()])
    catalogue_number = StringField("Catalogue number", validators=[DataRequired()])
    quantity = StringField("Quantity", validators=[DataRequired()])
    submit = SubmitField("Submit")