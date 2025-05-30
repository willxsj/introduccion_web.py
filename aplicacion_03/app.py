import web

urls = (
    '/', 'Index'#llamar clase index
)


render = web.template.render('templates')


app = web.application(urls, globals())

class Index:

    def __init__(self):
        self.text="Este es un texto desde python"
    def GET(self):
        return render.index(self.text) #quiero que renderises la pagina index

if __name__ == "__main__":
    app.run()