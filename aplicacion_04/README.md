# Crear dos paginas y viajar entre ellas 



## 1. Crea la pagina de bienvenida y viaja hacia ella

Agrega un vinculo a la pagina index para ir a bienvenida


````html
<a href="/bienvenida">bienvenida</a>
````

## 2. En el codigo fuente 'app.py'

Agregar la nueba ckase bienvenida 


````python
'/bienvenida', 'Bienvenida',
````

## 3. crear la clase bienvenida en el app.py

````python
class Bienvenida:

    def __init__(self):
        pass
    def GET(self):
        texto = "holaaaaaa"
        return render.bienvenida(texto)
````

