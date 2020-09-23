from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Barcelona1@localhost:3306/FACTURACIONDB'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DB_CON']
db = SQLAlchemy(app)

class cobro_actual(db.Model):
    numero = db.Column(db.Integer, primary_key=True )
    nombre = db.Column(db.String)
    mes = db.Column(db.Integer)
    monto = db.Column(db.Numeric)
    impuesto = db.Column(db.Numeric)
    mora = db.Column(db.Numeric)
    total = db.Column(db.Numeric)
    pagado = db.Column(db.Integer)

    def __repr__(self):
        return '<cobro_actual %r>' % self.numero



@app.route('/')
def hello_world():
    cobros = cobro_actual.query.all()
    return render_template('index.html', cobros = cobros)
    
#if __name__ == '_main_':
    #app.run(debug=True,host=0.0.0.0)