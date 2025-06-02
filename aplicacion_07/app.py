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
        print("recibiendo datos el formulario")
        formualrio = web.input()
        print(formualrio)

        numero1 = int(formualrio.numero1)
        numero2 = int(formualrio["numero2"])
        resultado = numero1 + numero2
        print(resultado)
        return render.index(resultado)

if __name__ == "__main__":
    app.run()