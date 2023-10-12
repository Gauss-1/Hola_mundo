#representacion de un parametro con dos rutas 
from flask import Flask
from flask import request

app = Flask(__name__) #flask recibe la constante name  #nuevo objeto

#http://127.0.0.1:8000/params?params1=Gaude_Gomez&params2=prueva_2
@app. route("/") # rutas
def index():
    return "Hola mundo Cruel " #regresar un string

@app.route("/params")
def params():    #podemos tener n. cantidad de rutas, pero sin repetir el metodo/parametros
    param = request.args.get("params1", "no contiene parametros")
    param_2 = request.args.get("params2", "no contiene parametros")
    return "El parametro es: {}, {}".format(param, param_2)

if __name__ == "__main__":
    app.run(debug = True, port= 9000) #se encarga de ejecutar el servidor 5000
#se cambiara del puerto 5000 al 8000



#ejercisicio de falsk con una sola ruta 
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/") # rutas
def index():
    return "Hola mundo Cruel " 

@app.route("/params/<name>/")#todo lo que se escriva depues de / se va a almacenar en name
def params(name):   
    return "El parametro es: {}". format(name)

if __name__ == "__main__":
    app.run(debug = True, port= 8000) 






#validar rutas
    #ejemplo de: Ejercicio con varias rutas incluyendo una con numeros 

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/") # rutas
def index():
    return "Hola mundo Cruel " 

@app.route("/params/")  #se garegara una nueva ruta para cuando quede solo name
@app.route("/params/<name>/") 
@app.route("/params/<name>/<int:num>") #con la creaxcion de esta ruta se estan acpeptando numeros enteros
def params(name= "este es un valor por defaul", num = "nada"): #se agrega un texto para que aparesa cuando no hay texto depues del name 
    return "El parametro es:  {}  {}". format(name, num)

if __name__ == "__main__":
    app.run(debug = True, port= 8000)     





#templates 
#renderizar

from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True, port = 8000)





    #templates 
#renderizar

from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route("/user/<name>")
def user(name = "Gau"):
    return render_template("user.html", nombre=name) #con render_template se renderiza la funcion html

if __name__ == "__main__":
    app.run(debug = True, port = 8000)




#templates, renderizar, 
#ciclos y variables
#mandar variables al template y que renderize las variables

from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route("/user/<name>")
def user(name = "Gau"):
    age= 13
    my_list = [1,2,3,4,5,"seis","siete","ocho..."] #no importa el tipo de valor que ase agregue puede ser de tipo numerico o letra
    return render_template("user.html", name=name, age=age, list= my_list ) #con render_template se mandan las variables de html
if __name__ == "__main__":
    app.run(debug = True, port = 8000)
