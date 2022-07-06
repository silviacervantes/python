from flask import Flask 
from flask import render_template #render de html

app = Flask(__name__)

@app.route('/')
def index():
    #return 'HOLA MUNDO MODO DEBUG!'
    return render_template(index.html)

if __name__ =='__main__':
    app.run(debug=True) # El proyecto esta en modo debug - desarrollo (muestra los cambios sin reiniciar el servidor)