from flask import Flask 
from flask import render_template #render de html(crear vista). Se crea una carpeta dentro de ser llamada templates.
from flask import request, redirect, url_for 
from datetime import datetime
from flaskext.mysql import MySQL


app = Flask(__name__)
mysql = MySQL()

#Configuracion de la conexion de MySQL
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'sistema'

mysql.init_app(app) #Le paso la app

@app.route('/')
def index():
    #conexion de MySQL
    conn = mysql.connect()
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM empleados')
    empleado = cursor.fetchall() # Trae todos los registros de la tabla
    
    print(empleado) # Muestra en la consola el resultado, (tupla de tuplas)
    
    mensaje = 'Este es un mensaje'
    return render_template('index.html',mensaje = mensaje, empleados = empleado)

@app.route('/create',methods=['GET'])
def create():
    return render_template('create.html')

@app.route('/store', methods=['POST'])
def store():
    print(request.form) # Lo del formulario viene por un lado
    print(request.files)# Los archivos van por otro lado
    
    conn = mysql.connect()
    cursor = conn.cursor()
    
    nombre = request.form['nombre']
    correo = request.form['email']
    
       
    imagen = request.files['imagen']
    
    now = datetime.now()
    time = now.strftime('%Y%m%d%H%M%S')
    
    nombre_imagen = time+'_'+imagen.filename
    
    imagen.save('CRUD/uploads/'+nombre_imagen) # Ojo, toma la raiz del proyecto
     
    sql='INSERT INTO empleados(nombre,correo,foto) VALUES (%s,%s,%s)' #%s Hace un escape a mysql, lo interpreta como TEXTO 
    values = (nombre,correo,nombre_imagen) 
    
    cursor.execute(sql,values)
    
    conn.commit() #Cuando hago cambios en los datos de la BD
    
    #return redirect('/') #Redirecciona
    return redirect(url_for('index')) # Coloco nombre de la funcion (/ es igual a index)

# GET (obtiene informacion) 
# POST(emvia registro x el formulario)
# * GET por defecto en todas las rutas
# PATCH (modidica una parte del regoitro ) ** PARA APIS
# PUT (modifica todo el registro completo) ** PARA APIS
# DELETE (avisar que voy a borrar un registro) ** PARA APIS

if __name__ =='__main__':
    app.run(debug=True) 
    # El proyecto esta en modo debug - desarrollo 
    # (muestra los cambios sin reiniciar el servidor)