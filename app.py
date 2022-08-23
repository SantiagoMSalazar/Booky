#from sqlite3 import Cursor
from flask import Flask
from flask import render_template,request,redirect
from flaskext.mysql import MySQL
from datetime import datetime
import os

app= Flask(__name__)
mysql=MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_PORT'] =23306
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='54321.#'
app.config['MYSQL_DATABASE_DB']='Tecnologiadb'
mysql.init_app(app)


@app.route('/')
def index():
    sql="SELECT * FROM `Clientes`;"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    
    Clientes=cursor.fetchall()
    print(Clientes)
    conn.commit()
    return render_template('empleados/index.html', Clientes=Clientes)

@app.route('/destroy/<int:id>')
def destroy(id):
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute("DELETE FROM Clientes WHERE id=%s",(id))
    conn.commit()

    return redirect("/")

@app.route('/edit/<int:id>')
def edit(id):
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM Clientes WHERE id=%s;",(id))
    Clientes=cursor.fetchall()
    conn.commit()
    print(Clientes)
    return render_template('empleados/edit.html',Clientes=Clientes)


@app.route('/update',methods=['POST'])
def update():
    _nombre=request.form['txtNombre']
    _correo=request.form['txtCorreo']
    _Telefono=request.form['txtTelefono']
    id=request.form['txtID']

    sql="UPDATE `Clientes` SET `Nombre`=%s, correo=%s, Telefono=%s WHERE id=%s;"
    datos=(_nombre,_correo,_Telefono,id)
    conn=mysql.connect()
    cursor=conn.cursor()

    cursor.execute(sql,datos)
    conn.commit()
    return redirect('/')

@app.route('/create')
def create():
    return render_template('empleados/create.html')

@app.route('/store', methods=['POST'])
def storage():
    _nombre=request.form['txtNombre']
    _correo=request.form['txtCorreo']
    _Telefono=request.form['txtTelefono']

    sql="INSERT INTO `Clientes` (`Id`, `Nombre`, `Correo`, `Telefono`) VALUES (NULL,%s,%s,%s);"

    datos=(_nombre,_correo,_Telefono)
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()

    return redirect('/')



if __name__=='__main__':
    app.run(debug=True)
