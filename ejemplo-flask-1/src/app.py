from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    name = request.args.get('name', 'Invitado')
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)