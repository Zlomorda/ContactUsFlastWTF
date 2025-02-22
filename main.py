from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email


app = Flask(__name__)

app.secret_key = 'lkjaghsdfglhlwu4euh8439hgl;dszhfgv'


class contactForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired()])
    email = StringField(label='Email', validators=[
        DataRequired(),
        Email(granular_message=True)
    ])
    message = StringField(label='Message')
    submit = SubmitField(label='Sent message')


@app.route('/', methods=['GET', 'POST'])
def home():
    cfmorm = contactForm()
    if cfmorm.validate_on_submit():
        print(f'''Name: {cfmorm.name.data},
              E-mail: {cfmorm.email.data},
              Message: {cfmorm.message.data}''')
    else:
        print('Invalid Credentials')

    return render_template('contact.html', form=cfmorm)


if __name__ == '__main__':
    app.run()
