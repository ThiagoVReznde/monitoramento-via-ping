from flask import Flask, jsonify, render_template
import ping3

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ping/<host>")
def ping(host):
    import datetime

    sent = datetime.datetime.now()
    tempo = ping3.ping(host)
    received = datetime.datetime.now()

    delta = received - sent

    return jsonify({
        "host": host,
        "alive": tempo is not None,
        "rtt_ms": tempo * 1000 if tempo else None,
        "diff_ms": delta.microseconds if tempo else None
    })

if __name__ == "__main__":
    app.run(debug=True)