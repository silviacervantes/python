from flask import Flask 
from flask import render_template #render de html
from flaskext.mysql import MySQL


app = Flask(__name__)
mysql = MySQL()

#Configuracion de la conexion de MySQL
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'sistema'

mysql.init_app(app)

@app.route('/')
def index():
    #conexion de MySQL
    conn = mysql.connect()
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM empleados LIMIT 10')
    empleados = cursor.fetchall() # Trae todos los registros de la tabla
    
    print(empleados) # Muestra en la consola el resultado, (tupla de tuplas)
    
    #return 'HOLA MUNDO MODO DEBUG!'
    mensaje = 'Este es un mensaje'
    return render_template('index.html',mensaje = mensaje)

if __name__ =='__main__':
    app.run(debug=True) # El proyecto esta en modo debug - desarrollo (muestra los cambios sin reiniciar el servidor)