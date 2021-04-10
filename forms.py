from wtforms import Form,StringField,PasswordField,BooleanField,IntegerField,FloatField,SubmitField
from wtforms.validators import DataRequired,Length,InputRequired

class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired()])
    username=StringField('Username',validators=[DataRequired()])
    password=PasswordField('Password',validators=[DataRequired()])

    submit=SubmitField('Log in')

class RegisterForm(Form):
    email = StringField('Email', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

    submit = SubmitField('Register')

class HouseForm(Form):
    type=StringField('Type',validators=[DataRequired()])
    price=FloatField('Price',validators=[DataRequired()])
    area=FloatField('Area',validators=[DataRequired()])
    location=StringField('Location',validators=[DataRequired()])
    # submit=SubmitField()