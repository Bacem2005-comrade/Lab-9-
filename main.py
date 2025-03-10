from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)

# Initialize SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///phonebook.db'
db = SQLAlchemy(app)

# Define your model class
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)

# Create the database tables (if not already created)
with app.app_context():
    db.create_all()

# Insert your name and phone number into the database
with app.app_context():
    # Check if the contact already exists to avoid duplication
    existing_contact = Contact.query.filter_by(name='Абд Али Басем', phone='+7(981)1761378').first()
    if not existing_contact:
        new_contact = Contact(name='Абд Али Басем', phone='+7(981)1761378')
        db.session.add(new_contact)
        db.session.commit()

# Query the database and print the results
with app.app_context():
    contacts = Contact.query.all()
    for contact in contacts:
        print(contact.name, contact.phone)
