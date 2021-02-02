import pymysql

conexion = pymysql.connect(host= 'localhost',user='root',password='',db='EMPLEADOS')
cur=conexion.cursor()
print("conexión establecida correctamente")

def empleados_may_salar(salar):
    sql= "SELECT NUMEM, NOMEM, NUMDE, SALAR FROM TEMPLE WHERE SALAR > {}".format(salar)

    try:
        cur.execute(sql)

        empleados= cur.fetchall()

        for emp in empleados:
            print("Numem: ", emp[0])
            print("Nomem: ", emp[1])
            print("Numde: ", emp[2])
            print("Salar: ", emp[3])
            print("________\n")

    except Exception as e:
        raise

def insertar_datos_buses(matricula, asientos, fecha):
    sql="INSERT INTO AUTOBUSES (MATRIC,NASIENTOS,ITV) VALUES ('{0}',{1},'{2}')" .format(matricula,asientos,fecha)

    try: 
        cursor.execute(sql)
        conexion.commit()

        print("datos insertados")
    except Exception as e:
        raise

def actualizar_sueldo_4000(numero):
    sql="UPDATE TEMPLE SET SALAR=4000 WHERE NUMEM = %s" %(numero)

    try: 
        cursor.execute(sql)
        conexion.commit()

        print("datos actualizados")
    except Exception as e:
        raise