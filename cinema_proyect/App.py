from flask import Flask, render_template, request, redirect, url_for, flash,session 
from flask_mysqldb import MySQL
from datetime import datetime
# initializations
app = Flask(__name__)

# Mysql Connection
app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_USER'] = 'usuario_cine'
app.config['MYSQL_PASSWORD'] = 'cine'
app.config['MYSQL_DB'] = 'proyecto_cine'
mysql = MySQL(app)

# settings
app.secret_key = "masterkey"

# routes
@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT codigo_contenido FROM contenido')
    data = cur.fetchall()
    
    cur.close()
    if 'ident' in session:
       if session['type']=='cliente':
            cur = mysql.connection.cursor()
            cur.execute('SELECT saldo FROM cliente where identificacion={}'.format(session['ident']))
            data2 = cur.fetchall()
            return render_template('index.html',ident=session['ident'], fullname=session['nombres']+' '+session['apellidos'],email=session['email'],movies=data,saldo=data2[0])
       else:
            return redirect(url_for('Index_Control'))
    else:
       return render_template('index.html', movies=data)

@app.route('/videos')
def view_videos():
    if 'ident' in session:
       return render_template('videos.html',ident=session['ident'], fullname=session['nombres']+' '+session['apellidos'],email=session['email'])
    else:
       return render_template('videos.html')

@app.route('/reviews')
def view_reviews():
    cur = mysql.connection.cursor()
    cur.execute('SELECT C.*, (SELECT avg(calificacion) from opinion WHERE fk_codigo_contenido=C.codigo_contenido) as prom FROM contenido as C ')
    data = cur.fetchall()
    cur.close()
    if 'ident' in session:
       return render_template('reviews.html',ident=session['ident'], fullname=session['nombres']+' '+session['apellidos'],email=session['email'],movies=data)
    else:
       return render_template('reviews.html',movies=data)

@app.route('/single/<id>', methods = ['POST', 'GET'])
def view_single(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT C.*, (SELECT avg(calificacion) from opinion WHERE fk_codigo_contenido=C.codigo_contenido) as prom,(SELECT count(*) from opinion WHERE fk_codigo_contenido=C.codigo_contenido) as cantidad FROM contenido as C WHERE codigo_contenido='{}'".format(id))
    data = cur.fetchall()
    cur.execute("SELECT O.* from opinion as O WHERE fk_codigo_contenido={}".format(id))
    data2 = cur.fetchall()
    cur.execute("SELECT S.nombre, P.fecha, P.hora_inicio, P.hora_fin, A.soporte from proyecta as P INNER JOIN sala as A ON A.codigo_sala=P.fk_codigo_sala INNER JOIN sede_cine as S ON A.fk_nombre=S.nombre WHERE P.fk_codigo_contenido={}".format(id))
    data3 = cur.fetchall()
    cur.execute('SELECT C.*, (SELECT avg(calificacion) from opinion WHERE fk_codigo_contenido=C.codigo_contenido) as prom FROM contenido as C ')
    data4 = cur.fetchall()
    cur.close()
    if 'ident' in session:
       return render_template('single.html',ident=session['ident'], edad=session['edad'], fullname=session['nombres']+' '+session['apellidos'],email=session['email'],movie=data[0],opiniones=data2,funciones=data3,movies=data4)
    else:
       return render_template('single.html',movie=data[0],opiniones=data2,funciones=data3,movies=data4)

@app.route('/contact')
def view_contact():
    if 'ident' in session:
       cur = mysql.connection.cursor()
       cur.execute('SELECT concat(nombres," ",apellidos), email, celular FROM persona where identificacion={}'.format(session['ident']))
       data = cur.fetchall()
       return render_template('contact.html',ident=session['ident'], fullname=session['nombres']+' '+session['apellidos'],email=session['email'],info_c=data[0])
    else:
       return render_template('contact.html')

@app.route('/consulta_recargas')
def view_recargas():
    if 'ident' in session:
       return render_template('consulta_recargas.html',ident=session['ident'], fullname=session['nombres']+' '+session['apellidos'],email=session['email'])
    else:
       return redirect(url_for('log_in'))

@app.route('/consultar_recarga', methods = ['POST'])
def consultar_recarga():
    if 'ident' in session:
       desde = request.form['fecha_i']
       hasta = request.form['fecha_f']
       cur = mysql.connection.cursor()
       cur.execute("SELECT codigo,fecha_hora,valor FROM recarga WHERE fk_identificacion='{}' AND fecha_hora BETWEEN '{}' AND '{}'".format(session['ident'],desde,hasta))
       data1 = cur.fetchall()
       return render_template('consulta_recargas.html',ident=session['ident'], fullname=session['nombres']+' '+session['apellidos'],email=session['email'],recargas=data1)
    else:
       return redirect(url_for('log_in'))

@app.route('/consulta_tiquetes')
def view_tiquetes():
    if 'ident' in session:
       return render_template('consulta_tiquetes.html',ident=session['ident'], fullname=session['nombres']+' '+session['apellidos'],email=session['email'])
    else:
       return redirect(url_for('log_in'))

@app.route('/consultar_tiquete', methods = ['POST'])
def consultar_tiquete():
    if 'ident' in session:
       desde = request.form['fecha_i']
       hasta = request.form['fecha_f']
       cur = mysql.connection.cursor()
       cur.execute("SELECT C.titulo,V.fecha_hora,V.cantidad,V.total FROM visualiza as V INNER JOIN proyecta as P ON V.fk_codigo_proyecta=P.codigo_f INNER JOIN contenido as C ON P.fk_codigo_contenido=C.codigo_contenido WHERE fk_identificacion='{}' AND fecha_hora BETWEEN '{}' AND '{}'".format(session['ident'],desde,hasta))
       data1 = cur.fetchall()
       return render_template('consulta_tiquetes.html',ident=session['ident'], fullname=session['nombres']+' '+session['apellidos'],email=session['email'],tiquetes=data1)
    else:
       return redirect(url_for('log_in'))

@app.route('/actualizar_datos')
def actualizar_datos():
    if 'ident' in session:
       cur = mysql.connection.cursor()
       cur.execute('SELECT nombres,apellidos,direccion, email, celular FROM persona where identificacion={}'.format(session['ident']))
       data = cur.fetchall()
       return render_template('actualizar_datos.html',ident=session['ident'], nombres=session['nombres'],apellidos=session['apellidos'],email=session['email'],perfil=data[0])
    else:
       return redirect(url_for('log_in'))

@app.route('/actualizar_datos2',methods=['POST'])
def actualizar_datos2():
    if 'ident' in session:
        celular = request.form['celular']
        email = request.form['email']
        direccion = request.form['direccion']
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE persona SET celular=%s, email=%s,direccion=%s,nombres=%s,apellidos=%s WHERE identificacion=%s ", (celular,email,direccion,nombres,apellidos,session['ident']))
        mysql.connection.commit()
        return redirect(url_for('actualizar_datos'))
    else:
        return redirect(url_for('log_in'))

@app.route('/actualizar_datos3',methods=['POST'])
def actualizar_datos3():
    if 'ident' in session:
        pass_act = request.form['pass_act']
        pass1 = request.form['pass1']
        pass2 = request.form['pass2']
        cur = mysql.connection.cursor()
        cur.execute('SELECT contraseña FROM persona where identificacion={}'.format(session['ident']))
        data = cur.fetchall() 
        if pass_act==data[0][0]:
            cur.execute("UPDATE persona SET contraseña=%s WHERE identificacion=%s ", (pass1,session['ident']))
            mysql.connection.commit()
            flash("Contraseña actualizada correctamente")
            return redirect(url_for('actualizar_datos'))
        else:
            flash("Error en contraseña actual")
            return redirect(url_for('actualizar_datos'))
    else:
        return redirect(url_for('log_in'))

@app.route('/log_in',methods=['POST','GET'])
def log_in():
    return render_template('admin/index.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('log_in'))

@app.route('/login_check', methods=['POST'])
def login_in():
    if request.method == 'POST':
        user = request.form['username']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM persona WHERE email='{}' AND contraseña='{}'".format(user,password))
        data1 = cur.fetchall()
        if data1:
            valid=data1[0]
            session['ident'] = valid[0]
            session['nombres'] = valid[6]
            session['apellidos'] = valid[7]
            session['email'] = valid[4]
            session['edad'] = valid[2]
            cur.execute("SELECT * FROM cliente WHERE identificacion='{}'".format(valid[0]))
            data2=cur.fetchall()
            if data2:
                session['type'] = "cliente"
                cur.close()
                return redirect(url_for('Index_Cliente'))
            else:
                cur.execute("SELECT cargo FROM empleado WHERE identificacion='{}'".format(valid[0]))
                data3=cur.fetchall()
                empleado=data3[0]
                if empleado[0]=="Administrador":
                    session['type'] = "admin"
                else:
                    session['type'] = "empleado"
                cur.close()
                return redirect(url_for('Index_Control'))
        else:
            flash('Datos Incorrectos')
            return redirect(url_for('log_in'))
        
@app.route('/Index_Cliente', methods=['GET', 'POST'])
def Index_Cliente():
    return redirect(url_for('Index'))

@app.route('/Index_Control', methods=['GET', 'POST'])
def Index_Control():

    return render_template('admin/index3.html', fullname=session['nombres']+' '+session['apellidos'],tipo=session['type'],module='home',action='view')

@app.route('/module/<pagina>', methods=['GET', 'POST'])
def cargar_modulos(pagina):
    if pagina=='sedes':
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM sede_cine WHERE nombre!="Cine"')
        data = cur.fetchall()
        cur.close()
        return render_template('admin/index3.html', fullname=session['nombres']+' '+session['apellidos'],tipo=session['type'],module=pagina,action='view',datos=data)
    if pagina=='salas':
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM sala ')
        data = cur.fetchall()
        cur.execute('SELECT * FROM sede_cine WHERE nombre!="Cine"')
        data2 = cur.fetchall()
        cur.close()
        return render_template('admin/index3.html', fullname=session['nombres']+' '+session['apellidos'],tipo=session['type'],module=pagina,action='view',datos=data,cines=data2)
    if pagina=='empleados':
        cur = mysql.connection.cursor()
        cur.execute('SELECT P.*,E.* FROM persona as P,empleado as E WHERE P.identificacion!="0000000000" and P.identificacion=E.identificacion')
        data = cur.fetchall()
        cur.execute('SELECT * FROM sede_cine WHERE nombre!="Cine"')
        data3 = cur.fetchall()
        cur.close()
        return render_template('admin/index3.html', fullname=session['nombres']+' '+session['apellidos'],tipo=session['type'],module=pagina,action='view',datos=data,cines=data3)
    if pagina=='clientes':
        cur = mysql.connection.cursor()
        cur.execute('SELECT P.*,E.* FROM persona as P,cliente as E WHERE  P.identificacion=E.identificacion')
        data = cur.fetchall()
        cur.close()
        return render_template('admin/index3.html', fullname=session['nombres']+' '+session['apellidos'],tipo=session['type'],module=pagina,action='view',datos=data)
    if pagina=='contenidos':
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM contenido')
        data = cur.fetchall()
        cur.close()
        return render_template('admin/index3.html', fullname=session['nombres']+' '+session['apellidos'],tipo=session['type'],module=pagina,action='view',datos=data)
    if pagina=='comidas':
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM comidas')
        data = cur.fetchall()
        cur.close()
        return render_template('admin/index3.html', fullname=session['nombres']+' '+session['apellidos'],tipo=session['type'],module=pagina,action='view',datos=data)
    if pagina=='r_comidas':
        return render_template('admin/index3.html', fullname=session['nombres']+' '+session['apellidos'],tipo=session['type'],module=pagina,action='view')
    if pagina=='r_contenidos':
        return render_template('admin/index3.html', fullname=session['nombres']+' '+session['apellidos'],tipo=session['type'],module=pagina,action='view')

@app.route('/resultado/<pagina>', methods=['GET', 'POST'])
def resultado_modulo(pagina):
    if request.method == 'POST':
        if pagina=='r_comidas':
            desde = request.form['desde']
            hasta = request.form['hasta']
            cur = mysql.connection.cursor()
            cur.execute('SELECT C.fk_codigo_comida, O.nombre, sum(C.cant_com), sum(total) FROM compra as C INNER JOIN comidas as O ON fk_codigo_comida=codigo_comida WHERE C.fecha_com BETWEEN %s AND %s group by C.fk_codigo_comida order by sum(C.cant_com) DESC',(desde,hasta))
            data = cur.fetchall()
            cur.close()
            return render_template('admin/index3.html', fullname=session['nombres']+' '+session['apellidos'],tipo=session['type'],module=pagina,action='view',datos=data)
        if pagina=='r_contenidos':
            desde = request.form['desde']
            hasta = request.form['hasta']
            cur = mysql.connection.cursor()
            cur.execute('SELECT C.titulo, sum(V.cantidad), sum(V.total) FROM visualiza as V INNER JOIN proyecta as P ON V.fk_codigo_proyecta=P.codigo_f INNER JOIN contenido as C ON P.fk_codigo_contenido=C.codigo_contenido WHERE v.fecha_hora BETWEEN %s AND %s group by C.codigo_contenido order by sum(V.cantidad) DESC',(desde,hasta))
            data = cur.fetchall()
            cur.close()
            return render_template('admin/index3.html', fullname=session['nombres']+' '+session['apellidos'],tipo=session['type'],module=pagina,action='view',datos=data)

@app.route('/registro/<pagina>', methods=['GET', 'POST'])
def registro_modulo(pagina):
    if request.method == 'POST':
        if pagina=='sedes':
            nombre = request.form['nombre']
            zona = request.form['zona']
            h_a = request.form['h_a']
            h_c = request.form['h_c']
            cur = mysql.connection.cursor()
            cur.execute('INSERT INTO sede_cine VALUES(%s,%s,%s,%s)',(nombre,zona,h_a,h_c))
            mysql.connection.commit()
            cur.close()
            return redirect(url_for('cargar_modulos',pagina=pagina))
        if pagina=='salas':
            codigo = request.form['codigo']
            capacidad = request.form['capacidad']
            soporte = request.form['soporte']
            estado = request.form['estado']
            n_sede = request.form['n_sede']
            cur = mysql.connection.cursor()
            cur.execute('INSERT INTO sala VALUES(%s,%s,%s,%s,%s)',(codigo,capacidad,soporte,estado,n_sede))
            mysql.connection.commit()
            cur.close()
            return redirect(url_for('cargar_modulos',pagina=pagina))
        if pagina=='empleados':
            ident = request.form['ident']
            fecha_n = request.form['fecha_n']
            edad = request.form['edad']
            nombres = request.form['nombres']
            apellidos = request.form['apellidos']
            celular = request.form['celular']
            email = request.form['email']
            direccion = request.form['direccion']
            fecha_i = request.form['fecha_i']
            cargo = request.form['cargo']
            salario = request.form['salario']
            contraseña=request.form['contraseña']
            n_sede = request.form['n_sede']
            cur = mysql.connection.cursor()
            cur.execute('INSERT INTO persona VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)',(ident,fecha_n,edad,celular,email,direccion,nombres,apellidos,contraseña))
            mysql.connection.commit()
            cur.execute('INSERT INTO empleado VALUES(%s,%s,%s,%s,%s)',(ident,fecha_i,cargo,salario,n_sede))
            mysql.connection.commit()
            cur.close()
            return redirect(url_for('cargar_modulos',pagina=pagina))
        if pagina=='clientes':
            ident = request.form['ident']
            fecha_n = request.form['fecha_n']
            edad = request.form['edad']
            nombres = request.form['nombres']
            apellidos = request.form['apellidos']
            celular = request.form['celular']
            email = request.form['email']
            direccion = request.form['direccion']
            cod_tar = request.form['cod_tar']
            saldo = request.form['saldo']
            contraseña=request.form['contraseña']
            cur = mysql.connection.cursor()
            cur.execute('INSERT INTO persona VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)',(ident,fecha_n,edad,celular,email,direccion,nombres,apellidos,contraseña))
            mysql.connection.commit()
            cur.execute('INSERT INTO cliente VALUES(%s,%s,%s)',(ident,cod_tar,saldo))
            mysql.connection.commit()
            cur.close()
            return redirect(url_for('cargar_modulos',pagina=pagina))
        if pagina=='contenidos':
            codigo = request.form['codigo']
            clasificacion = request.form['clasificacion']
            pais = request.form['pais']
            titulo = request.form['titulo']
            genero = request.form['genero']
            duracion = request.form['duracion']
            idioma = request.form['idioma']
            fecha_e = request.form['fecha_e']
            tipo = request.form['tipo']
            director = request.form['director']
            sinopsis=request.form['sinopsis']
            cur = mysql.connection.cursor()
            cur.execute('INSERT INTO contenido VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(codigo,clasificacion,pais,titulo,genero,duracion,idioma,fecha_e,tipo,director,sinopsis))
            mysql.connection.commit()
            cur.close()
            return redirect(url_for('cargar_modulos',pagina=pagina))
        if pagina=='comidas':
            codigo = request.form['codigo']
            valor = request.form['valor']
            nombre = request.form['nombre']
            descripcion = request.form['descripcion']
            cur = mysql.connection.cursor()
            cur.execute('INSERT INTO comidas VALUES(%s,%s,%s,%s)',(codigo,valor,nombre,descripcion))
            mysql.connection.commit()
            cur.close()
            return redirect(url_for('cargar_modulos',pagina=pagina))


@app.route('/editar/<pagina>/<id>', methods=['GET', 'POST'])
def editar_modulo(pagina,id):
    if pagina=='sedes':
        cur = mysql.connection.cursor()
        cur.execute('SELECT nombre,zona,hora_apertura,hora_cierre FROM sede_cine WHERE nombre=%s',[id])
        data=cur.fetchall()
        cur.close()
        return render_template('admin/index3.html', fullname=session['nombres']+' '+session['apellidos'],tipo=session['type'],module=pagina,action='editar',datos=data[0])
    if pagina=='salas':
        cur = mysql.connection.cursor()
        cur.execute('SELECT codigo_sala,capacidad,soporte,estado,fk_nombre FROM sala WHERE codigo_sala=%s',[id])
        data=cur.fetchall()
        cur.execute('SELECT * FROM sede_cine WHERE nombre!="Cine"')
        data2 = cur.fetchall()
        cur.close()
        return render_template('admin/index3.html', fullname=session['nombres']+' '+session['apellidos'],tipo=session['type'],module=pagina,action='editar',datos=data[0],cines=data2)
    if pagina=='empleados':
        cur = mysql.connection.cursor()
        cur.execute('SELECT P.*,E.* FROM persona as P,empleado as E WHERE P.identificacion=%s AND E.identificacion=%s',(id,id))
        data = cur.fetchall()
        cur.execute('SELECT * FROM sede_cine WHERE nombre!="Cine"')
        data3 = cur.fetchall()
        cur.close()
        return render_template('admin/index3.html', fullname=session['nombres']+' '+session['apellidos'],tipo=session['type'],module=pagina,action='editar',datos=data[0],cines=data3)
    if pagina=='clientes':
        cur = mysql.connection.cursor()
        cur.execute('SELECT P.*,E.* FROM persona as P,cliente as E WHERE P.identificacion=%s AND E.identificacion=%s',(id,id))
        data = cur.fetchall()
        cur.close()
        return render_template('admin/index3.html', fullname=session['nombres']+' '+session['apellidos'],tipo=session['type'],module=pagina,action='editar',datos=data[0])
    if pagina=='contenidos':
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM contenido WHERE codigo_contenido=%s',[id])
        data = cur.fetchall()
        cur.close()
        return render_template('admin/index3.html', fullname=session['nombres']+' '+session['apellidos'],tipo=session['type'],module=pagina,action='editar',datos=data[0])
    if pagina=='comidas':
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM comidas WHERE codigo_comida=%s',[id])
        data=cur.fetchall()
        cur.close()
        return render_template('admin/index3.html', fullname=session['nombres']+' '+session['apellidos'],tipo=session['type'],module=pagina,action='editar',datos=data[0])

@app.route('/edicion/<pagina>/<id>', methods=['GET', 'POST'])
def edicion_modulo(pagina,id):
    if request.method == 'POST':
        if pagina=='sedes':
            nombre = request.form['nombre']
            zona = request.form['zona']
            h_a = request.form['h_a']
            h_c = request.form['h_c']
            cur = mysql.connection.cursor()
            cur.execute('UPDATE sede_cine SET nombre=%s,zona=%s,hora_apertura=%s,hora_cierre=%s WHERE nombre=%s',(nombre,zona,h_a,h_c,nombre))
            mysql.connection.commit()
            cur.close()
            return redirect(url_for('cargar_modulos', pagina=pagina))
        if pagina=='salas':
            codigo = request.form['codigo']
            capacidad = request.form['capacidad']
            soporte = request.form['soporte']
            estado = request.form['estado']
            n_sede = request.form['n_sede']
            cur = mysql.connection.cursor()
            cur.execute('UPDATE sala SET capacidad=%s,soporte=%s,estado=%s,fk_nombre=%s WHERE codigo_sala=%s',(capacidad,soporte,estado,n_sede,codigo))
            mysql.connection.commit()
            cur.close()
            return redirect(url_for('cargar_modulos', pagina=pagina))
        if pagina=='empleados':
            ident = request.form['ident']
            fecha_n = request.form['fecha_n']
            edad = request.form['edad']
            nombres = request.form['nombres']
            apellidos = request.form['apellidos']
            celular = request.form['celular']
            email = request.form['email']
            direccion = request.form['direccion']
            fecha_i = request.form['fecha_i']
            cargo = request.form['cargo']
            salario = request.form['salario']
            contraseña=request.form['contraseña']
            n_sede = request.form['n_sede']
            cur = mysql.connection.cursor()
            cur.execute('UPDATE persona set fecha_nac=%s,edad=%s,celular=%s,email=%s,direccion=%s,nombres=%s,apellidos=%s,contraseña=%s WHERE identificacion=%s',(fecha_n,edad,celular,email,direccion,nombres,apellidos,contraseña,ident))
            mysql.connection.commit()
            cur.execute('UPDATE empleado SET fecha_inicio=%s,cargo=%s,salario=%s,fk_nombre=%s WHERE identificacion=%s',(fecha_i,cargo,salario,n_sede,ident))
            mysql.connection.commit()
            cur.close()
            return redirect(url_for('cargar_modulos', pagina=pagina))
        if pagina=='clientes':
            ident = request.form['ident']
            fecha_n = request.form['fecha_n']
            edad = request.form['edad']
            nombres = request.form['nombres']
            apellidos = request.form['apellidos']
            celular = request.form['celular']
            email = request.form['email']
            direccion = request.form['direccion']
            cod_tar = request.form['cod_tar']
            saldo = request.form['saldo']
            contraseña=request.form['contraseña']
            cur = mysql.connection.cursor()
            cur.execute('UPDATE persona set fecha_nac=%s,edad=%s,celular=%s,email=%s,direccion=%s,nombres=%s,apellidos=%s,contraseña=%s WHERE identificacion=%s',(fecha_n,edad,celular,email,direccion,nombres,apellidos,contraseña,ident))
            mysql.connection.commit()
            cur.execute('UPDATE cliente SET cod_tarjeta=%s,saldo=%s WHERE identificacion=%s',(cod_tar,saldo,ident))
            mysql.connection.commit()
            cur.close()
            return redirect(url_for('cargar_modulos', pagina=pagina))
        if pagina=='contenidos':
            codigo = request.form['codigo']
            clasificacion = request.form['clasificacion']
            pais = request.form['pais']
            titulo = request.form['titulo']
            genero = request.form['genero']
            duracion = request.form['duracion']
            idioma = request.form['idioma']
            fecha_e = request.form['fecha_e']
            tipo = request.form['tipo']
            director = request.form['director']
            sinopsis=request.form['sinopsis']
            cur = mysql.connection.cursor()
            cur.execute('UPDATE contenido set clasificacion=%s,pais=%s,titulo=%s,genero=%s,duracion=%s,idioma=%s,fecha_estreno=%s,tipo=%s,director=%s,sinopsis=%s WHERE codigo_contenido=%s',(clasificacion,pais,titulo,genero,duracion,idioma,fecha_e,tipo,director,sinopsis,codigo))
            mysql.connection.commit()
            cur.close()
            return redirect(url_for('cargar_modulos', pagina=pagina))
        if pagina=='comidas':
            codigo = request.form['codigo']
            valor = request.form['valor']
            nombre = request.form['nombre']
            descripcion = request.form['descripcion']
            cur = mysql.connection.cursor()
            cur.execute('UPDATE comidas SET valor_comida=%s,nombre=%s,descrip_comida=%s WHERE codigo_comida=%s',(valor,nombre,descripcion,codigo))
            mysql.connection.commit()
            cur.close()
            return redirect(url_for('cargar_modulos', pagina=pagina))

@app.route('/eliminar/<pagina>/<id>', methods=['GET', 'POST'])
def eliminar_modulo(pagina,id):
    if pagina=='sedes':
        cur = mysql.connection.cursor()
        cur.execute('DELETE FROM contenido WHERE codigo_contenido=%s',[id])
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('cargar_modulos', pagina=pagina))
    if pagina=='salas':
        cur = mysql.connection.cursor()
        cur.execute('DELETE FROM sala WHERE codigo_sala=%s',[id])
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('cargar_modulos', pagina=pagina))
    if pagina=='empleados':
        cur = mysql.connection.cursor()
        cur.execute('DELETE FROM persona WHERE identificacion=%s',[id])
        mysql.connection.commit()
        cur.execute('DELETE FROM empleado WHERE identificacion=%s',[id])
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('cargar_modulos', pagina=pagina))
    if pagina=='clientes':
        cur = mysql.connection.cursor()
        cur.execute('DELETE FROM persona WHERE identificacion=%s',[id])
        mysql.connection.commit()
        cur.execute('DELETE FROM cliente WHERE identificacion=%s',[id])
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('cargar_modulos', pagina=pagina))
    if pagina=='contenidos':
        cur = mysql.connection.cursor()
        cur.execute('DELETE FROM contenido WHERE codigo_contenido=%s',[id])
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('cargar_modulos', pagina=pagina))
    if pagina=='comidas':
        cur = mysql.connection.cursor()
        cur.execute('DELETE FROM comidas WHERE codigo_comida=%s',[id])
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('cargar_modulos', pagina=pagina))



@app.route('/cargar_opinion', methods=['POST'])
def cargar_opinion():
    if request.method == 'POST':
        edad = request.form['edad']
        calificacion = request.form['calificacion']
        comentario = request.form['comentario']
        contenido = request.form['contenido']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO opinion (fecha, comentario,edad,calificacion,fk_codigo_contenido) VALUES (NOW(),%s,%s,%s,%s)", (comentario,edad,calificacion,contenido))
        mysql.connection.commit()
        return redirect(url_for('view_single',id=contenido))

@app.route('/registro_mensaje', methods=['POST'])
def registro_mensaje():
    if request.method == 'POST':
        nombre = request.form['nombre']
        if 'ident' in session:
            ident=session['ident']
        else:
            ident=""
        email = request.form['email']
        celular = request.form['telefono']
        mensaje = request.form['mensaje']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO mensajes (ident,fecha_hora,nombre,email,celular, mensaje) VALUES (%s,NOW(),%s,%s,%s,%s)", (ident,nombre,email,celular,mensaje))
        mysql.connection.commit()
        return redirect(url_for('view_contact'))

# starting the app
if __name__ == "__main__":
    app.run(port=3000, debug=True)
