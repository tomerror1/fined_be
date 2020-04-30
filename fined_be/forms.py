from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from fined_be.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', 
        validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('E-Mail', 
        validators=[DataRequired(), Email()])
    password = PasswordField('Password', 
        validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', 
        validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    # create a custom validation with wtform
    def validate_username(self, username):
        # check if the user is already in the database
        user = User.query.filter_by(username=username.data).first()
        # if user is anything else then none (=True), then i want an error
        if user:
            raise ValidationError('Dieser Benutzername ist bereits in Verwendung.')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Für diese Email ist bereits ein Account vorhanden.')
    


class LoginForm(FlaskForm):
    email = StringField('E-Mail', 
        validators=[DataRequired(), Email()])
    password = PasswordField('Password', 
        validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')



class UpdateAccountForm(FlaskForm):
    username = StringField('Username', 
        validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('E-Mail', 
        validators=[DataRequired(), Email()])
    submit = SubmitField('Update')

    # only check if data is different from current user
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            # if user is anything else then none (=True), then i want an error
            if user:
                raise ValidationError('Dieser Benutzername ist bereits in Verwendung.')
    
    def validate_email(self, email):
        if email.data != current_user.email:        
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Für diese Email ist bereits ein Account vorhanden.')