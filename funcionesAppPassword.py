import mysql.connector

midb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Panther*',
    database='test'
)
cursor = midb.cursor()

def wellcome():
    print('******************************************')
    print('Bienvenido al Administrador de contraseñas')
    print('******************************************')

def run():

    operacion = int(input('''
    1. Añadir contraseña
    2. Ver Contraseña 
    3. Modificar Contraseña
    4. Eliminar Contraseña
    5. Salir
    > '''))

    if operacion == 1:
        new_password()
        run()
    elif operacion == 2:
        view_password()
        run()
    elif operacion == 3:
        modify_password()
        run()
    elif operacion == 4:
        delete_password()
        run()
    elif operacion == 5:
        print('\nGracias por usar nuestro programa, hasta la proxima\n')
    else:
        print('No ingresaste una opción valida ¿?')
        run()


def new_password():

    cuenta = input('Ingresa la cuenta > ')
    correo_userName = input('Ingresa tu email o user_name > ')
    password = input('Ingresa la contraseña > ')
    description = input('Ingresa la descripción > ')

    sql = 'insert into contrasegna (cuenta, correo_userName, password, description) values (%s, %s, %s, %s)'
    values = (cuenta, correo_userName, password, description)

    cursor.execute(sql, values)
    midb.commit()
    print('\nCuenta añadida con exito!!!')
    print('______________________________________________________\n')


def view_password():
    cursor.execute('select id, description from contrasegna')
    resultado = cursor.fetchall()
    print('\nid  description\n')
    for i in resultado:
        print(i)

    id = int(input('\nIngresa el id de la cuenta > '))
    sql = 'select * from contrasegna where id = %s'
    values = (id, )
    cursor.execute(sql, values)
    resultado = cursor.fetchall()
    print('\nid cuenta  correo_userName  password  description\n')
    print(resultado)
    print('______________________________________________________\n')


def modify_password():
    cursor.execute('select id, description from contrasegna')
    resultado = cursor.fetchall()
    print('\nid  description\n')
    for i in resultado:
        print(i)

    id = int(input('\nIngresa el id de la cuenta > '))

    password = input('Ingresa la nueva contraseña > ')

    sql = 'update contrasegna set password = %s where id = %s'
    values = (password, id)
    cursor.execute(sql, values)
    midb.commit()
    print('Contraseña modificada con exito!!!')

    sql = 'select * from contrasegna where id = %s'
    values = (id, )
    cursor.execute(sql, values)
    resultado = cursor.fetchall()
    print('\nid     cuenta      correo_userName      password      description\n')
    print(resultado)
    print('______________________________________________________\n')


def delete_password():
    cursor.execute('select id, description from contrasegna')
    resultado = cursor.fetchall()
    print('\nid  description\n')
    for i in resultado:
        print(i)

    id = int(input('\nIngresa el id de la cuenta a eliminar > '))
    sql = 'delete from contrasegna where id=%s'
    values = (id, )
    cursor.execute(sql, values)
    midb.commit()
    print('Cuenta elminada con exito!!!')
    print('______________________________________________________\n')


