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
        
            print("Recibiendo datos del formulario")
            formulario = web.input()
            print(formulario)

            try:       
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
                    if numero1 == 0 or numero2 == 0:
                        resultado = "Error: No se pede dividir entre 0 "
                    else:
                        resultado = numero1 / numero2
                else:
                    resultado = "no valido"

            except ValueError:
                resultado = "Error: Todos los campos tienen valor numerico"
            except Exception as e:
                resultado = f"Error 001:  {e.arg[0]}"
                
            print(f"Resultado: {resultado}")
            return render.index(resultado)

if __name__ == "__main__":
    app.run()