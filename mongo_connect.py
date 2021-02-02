import pymongo

try:
    #Para conectarse a la base de datos simplemente utilizando el comando MongoClient realizamos la conexión
    #A este método le pasamos a qué mongo queremos conectarnos (en este caso a nuestro localhost)
    #Además yo le he puesto un tiempo de 1000 ms para que se conecte y en el caso en el que tarde más salta un error
    client=pymongo.MongoClient("mongodb://localhost",serverSelectionTimeoutMS=1000)

    print("Conexion a mongo exitosa")

except pymongo.errors.serverSelectionTimeoutError as errorTiempo:
    print("Tiempo excedido" + errorTiempo)
except pymongo.errors.ConnectionFailure as errorConexion:
    print("Fallo en la conexión")

#Una vez realizada la conexión, vamos a realizar un par de consultas en una nueva db que voy a llamar: tiendatest

#para insertar lo hacemos de la siguiente manera, vamos a utilizar una función para no ejecutar todo el rato el cógido
def insertar():
    db=client.tiendatest
    collection = db.productos
    collection.insert_one({"producto": "ordenador", "precio": 1200})
    #para insert_many es lo mismo, se utiliza la sintaxis de mongo

#para probar el find vamos a utilizar una base de datos más grandes: la de películas

def find():
    db=client.primera
    peliculas=db.peliculas
    americanas=peliculas.find({'pais':"USA"},{'_id':0,'titulo':1,'director':1,'duracion':1,'puntuacion':1})
    #lo limitamos a las 4 primeras (como veis es igual que en mongo)
    americanas=americanas.limit(4)
    americanas=americanas.sort('puntuacion',pymongo.ASCENDING)
    #hay que fijarse en como se pone el ascendente y descendente porque es diferente que en mongo

    for doc in americanas:
        print(doc)

def update_doc(): #para el update la sintaxis es la misma que en mongo
    db=client.primera
    peliculas=db.peliculas
    resultado = peliculas.update_many({'pais':'USA'},{'$set':{'pais':'EEUU'}})
    #Por último que nos diga cuántos ha modificado
    print("Modificados: ", resultado.matched_count)
update_doc()



    
