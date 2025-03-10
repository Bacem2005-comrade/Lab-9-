from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///phonebook.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)

def init_db():
    with app.app_context():
        db.create_all()
        if not Contact.query.filter_by(name='Басем', phone='+7(981)1761378').first():
            db.session.add(Contact(name='Басем', phone='+7(981)1761378'))
            db.session.commit()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        if name and phone:
            new_contact = Contact(name=name, phone=phone)
            db.session.add(new_contact)
            db.session.commit()
        return redirect('/')
    contacts = Contact.query.all()
    return render_template('index.html', contacts=contacts)

@app.route('/clear', methods=['POST'])
def clear():
    db.session.query(Contact).delete()
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)