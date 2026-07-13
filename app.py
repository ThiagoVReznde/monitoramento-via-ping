from flask import Flask, jsonify, render_template
import ping3

app = Flask(__name__)

# Rota que entrega o seu HTML para o navegador
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ping/<host>")
def ping(host):
    tempo = ping3.ping(host)
    return jsonify({
        "host": host,
        "alive": tempo is not None,
        "rtt_ms": tempo * 1000 if tempo else None
    })

if __name__ == "__main__":
    app.run(debug=True)