from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Optional, ValidationError
import os

def validate_root_directory(form, field):
    root_directory = field.data
    if root_directory and not os.path.exists(root_directory):
        raise ValidationError('Directory does not exist.')

class MyForm(FlaskForm):
    filename = StringField('File Name', validators=[DataRequired()])
    root_directory = StringField('Root Directory (Optional)', validators=[Optional(), validate_root_directory])
    check_field = BooleanField('Advanced search (Optional)')
    submit = SubmitField('Submit')
