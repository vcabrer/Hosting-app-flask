from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hola, esta es mi aplicación web desplegada con Flask en Render</h1>"

if __name__ == "__main__":
    app.run(debug=True)