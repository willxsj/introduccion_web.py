import web

urls = (
    '/', 'Index',#llamar clase index
    '/bienvenida', 'Bienvenida',
)


render = web.template.render('templates')


app = web.application(urls, globals())

class Index:

    def __init__(self):
        #self.text="Este es un texto desde python"
        pass
    def GET(self):
        texto = "Hola desde el index"
        return render.index(texto) #quiero que renderises la pagina index

class Bienvenida:

    def __init__(self):
        pass
    def GET(self):
        texto = "holaaaaaa"
        return render.bienvenida(texto) #quiero que renderises la pagina index

if __name__ == "__main__":
    app.run()