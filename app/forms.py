from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

class UploadForm(FlaskForm):
    image = FileField("Image", validators=[InputRequired(), FileRequired(), FileAllowed(['jpg','jpeg', 'png', 'gif', 'tiff', 'ai', 'raw', 'eps'], 'Images only')])