import web

urls = (
    '/', 'Index'#llamar clase index
)


render = web.template.render('templates')


app = web.application(urls, globals())

class Index:
    def GET(self):
        return render.index() 
    
    def POST(self):
        try:
                print("Recibiendo datos del formulario")
                formulario = web.input()
                print(formulario)

       
                numero1 = float(formulario.numero1)
                numero2 = float(formulario.numero2)
                operacion = formulario.operacion

                if operacion == "sumar":
                    resultado = numero1 + numero2
                elif operacion == "restar":
                    resultado = numero1 - numero2
                elif operacion == "multiplicar":
                    resultado = numero1 * numero2
                elif operacion == "dividir":
                    resultado = numero1 / numero2
                else:
                    resultado = "no valido"


        except Exception as e:
            print(f"Error 001:  {e.arg[0]}")
            print("Error al dividir") 
            


        print(f"Resultado: {resultado}")
        return render.index(resultado)

if __name__ == "__main__":
    app.run()