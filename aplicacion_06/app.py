import web

urls = (
    '/', 'Index'#llamar clase index
)


render = web.template.render('templates')


app = web.application(urls, globals())

class Index:
    def GET(self):
        return render.index() #quiero que renderises la pagina index

if __name__ == "__main__":
    app.run()