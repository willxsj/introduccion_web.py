# Realizar una lista ordenada y usar un for



## 1. Agrega una lista ordenada en el html

lista ordenada en html


````html
<ul>
            <li style="color: cadetblue; ">Dejah</li>
            <li style="color: cadetblue;">John</li>
            <li style="color: cadetblue;">Carthoris</li>
</ul>
````

## 2. Agregar un array a la clase index en el app.py

se agrega un array llamado  clientes a la clase index   

````python
class Index:
    
    def __init__(self):
        pass

    def GET(self):
    
        clientes = ["Ale","willam","nose"]
        return render.index(clientes) 

````

## 3. Agrear un for para que jale lo que tiene el array al html

    agrgas un for en lugar de la lista ordenada para que agrge tus datos de tu lista ordenada

    ````html
<ul>
            $for cliente in clientes:
            <li style="color: cadetblue;">$cliente</li>
</ul>
````

    

