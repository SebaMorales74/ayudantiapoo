import cx_Oracle

instantclient = r"RUTA DE INSTANT CLIENT"
cx_Oracle.init_oracle_client(lib_dir=instantclient)

connection = cx_Oracle.connect("NOMBREDEUSUARIO","CLAVEDEUSUARIO","bdpri2021_high")
cursor = connection.cursor()

query = "SELECT * FROM EMPLEADO"
cursor.execute(query)

resultado = cursor.fetchall()
print(resultado)