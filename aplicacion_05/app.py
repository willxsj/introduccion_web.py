import web

urls = (
    '/', 'Index'#llamar clase index
)


render = web.template.render('templates')


app = web.application(urls, globals())

class Index:
    
    def __init__(self):
        pass

    def GET(self):
    
        clientes = ["Ale","willam","nose"]
        return render.index(clientes) #quiero que renderises la pagina index

if __name__ == "__main__":
    app.run()