# ◃─────Bibliotecas──────▹
from flask import Flask 
# ◃──────────────────doc────▹

# ◃─────Variaveis de Controle─────▹
app = Flask(__name__)



# ◃──────────Rotas───────────▹

@app.route('/')
def hello():
    return "Hello, Docker!"



# ◃──────────Run app────────────▹
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090)
