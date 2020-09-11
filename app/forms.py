from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, ValidationError, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange

class CompanyForm(FlaskForm):
    """
    Form for adding and editing companies.
    """
    name = StringField('Company Name', validators=[DataRequired(), Length(1, 256)])
    industry = StringField('Industry', validators=[DataRequired(), Length(1, 128)])
    city = StringField('City', validators=[DataRequired(), Length(1, 128)])
    state = StringField('State or Province', validators=[DataRequired(), Length(1, 128)])
    country = StringField('Country', validators=[DataRequired(), Length(1, 128)])
    phone = StringField('Phone #', validators=[DataRequired(), Length(min=6)])
    revenue = IntegerField('Monthly Revenue (USD)', validators=[NumberRange(min=0)])
    notes = TextAreaField('Notes')
    submit = SubmitField('Add Company')