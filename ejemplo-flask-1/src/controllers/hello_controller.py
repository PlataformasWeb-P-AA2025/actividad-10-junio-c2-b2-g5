class HelloController:
    def __init__(self, app):
        self.app = app
        self.app.add_url_rule('/', 'hello', self.get_name)

    def get_name(self):
        name = self.app.request.args.get('name', 'Invitado')
        return self.app.render_template('hello.html', name=name)