import web

urls = (
    '/', 'Index'
)
app = web.application(urls, globals())

class Index:
    def GET(self):
        return 'Hola mundo desde web.py '

if __name__ == "__main__":
    app.run()