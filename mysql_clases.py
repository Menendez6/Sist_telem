import pymysql

class Database:
    def __init__(self,BD):

        self.connection= pymysql.connect(host='localhost',user='root',password='',db=BD)
        self.cursor = self.connection.cursor()
        print("conexión establecida exitósamente")

    def empleados_may_salar(self,salar):

        sql= "SELECT NUMEM, NOMEM, NUMDE, SALAR FROM TEMPLE WHERE SALAR > {}".format(salar)

        try:
            self.cursor.execute(sql)

            empleados= self.cursor.fetchall()

            for emp in empleados:
                print("Numem: ", emp[0])
                print("Nomem: ", emp[1])
                print("Numde: ", emp[2])
                print("Salar: ", emp[3])
                print("________\n")
        
        except Exception as e:
            raise

    def insertar_datos_buses(self, matricula, asientos, fecha):
        sql="INSERT INTO AUTOBUSES (MATRIC,NASIENTOS,ITV) VALUES ('{0}',{1},'{2}')" .format(matricula,asientos,fecha)

        try: 
            self.cursor.execute(sql)
            self.connection.commit()

            print("datos insertados")
        except Exception as e:
            raise
    
    def actualizar_sueldo_4000(self, numero):
        sql="UPDATE TEMPLE SET SALAR=4000 WHERE NUMEM = %s" %(numero)

        try: 
            self.cursor.execute(sql)
            self.connection.commit()

            print("datos actualizados")
        except Exception as e:
            raise

database = Database("EMPLEADOS")
database.actualizar_sueldo_4000(280)