from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    titolo="Pagina iniziale"
    testo="Ciao mondo!"
<<<<<<< HEAD
    bottone="Più info"
    return render_template("base.html" ,
             titolo=titolo,
             testo=testo,
             bottone=bottone)   
=======
    bottone
    return "Ciao mondo!"
>>>>>>> blocks

@app.route('/info')
def info():
    titolo="Pagina info"
    testo="Informazioni"
    bottone="Homepage"
    return render_template("base.html" ,
           titolo=titolo,
           testo=testo,
           bottone=bottone)

    
if __name__ == '__main__':
    app.run()
