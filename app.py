#******************************************
# author: Crozemarie Jean-Pierre
# Date: January 2024
# Version: 1.0
#
#*******************************************

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm 
from wtforms import StringField, TextAreaField, validators, PasswordField, SubmitField 
from wtforms.validators import DataRequired, Email 
import email_validator 

app = Flask(__name__)
# tokens used for CSRF protection
app.config['SECRET_KEY'] = 'fqsfBdQd4bpqzXokVjgSvtj3V'

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired(), validators.Regexp('^\+?\d{10}$', message='Valid 10 digit phone number required.')]) 
    # Notes for phone number validation: 
    #  ^  : Asserts the start of the string.
    # \+? : Matches a plus sign (+) optional.
    # \d{10}: Matches exactly 10 digits.
    # $     : Asserts the end of the string.
    message = TextAreaField('Message', validators=[DataRequired()])    


@app.route('/')
def index():
    return render_template ('index.html')

@app.route('/about')
def about():
    h2_text = "About Design"
    return render_template('about.html', h2_text = h2_text)

@app.route('/portfolio')
def portfolio():
    h2_text = "Our Portfolio"
    return render_template('portfolio.html', h2_text= h2_text)

@app.route('/service')
def service():
    h2_text = "What we do" 
    return render_template("service.html", h2_text = h2_text)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    cform = ContactForm()
    
    if request.method == 'POST':
        if cform.validate_on_submit():
            # Get data from form
            print(f"Name: {cform.name.data}, E-mail: {cform.email.data}, Phone: {cform.phone.data}, Message: {cform.message.data}")
            # 
            # Here add code to send message 
            #
            return redirect(url_for('submitted'))
        else:
            print("Validation error:", cform.errors)
    
    return render_template("contact.html", form=cform)

@app.route('/submitted')
def submitted():
    h2_text = "Thank you for your submission!"
    return render_template('submitted.html', h2_text = h2_text)


@app.errorhandler(404)
def not_found_error(error):
    h2_text = "Page not found...!" 
    return render_template('404.html', h2_text = h2_text), 404

if __name__ == '__main__':
    app.run(debug=True)
