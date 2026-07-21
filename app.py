from flask import Flask, jsonify, render_template
import ping3

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

#net_stat = psutil.net_io_counters(nowrap=True)
#net_in_1 = net_stat.bytes_recv
#net_out_1 = net_stat.bytes_sent
#
#time.sleep(5)
#net_stat = psutil.net_io_counters(nowrap=True)
#net_in_2 = net_stat.bytes_recv
#net_out_2 = net_stat.bytes_sent
#
#net_in = round((net_in_2 - net_in_1) / 1024 / 1024, 3)
#net_out = round((net_out_2 - net_out_1) / 1024 / 1024, 3)

@app.route("/ping/<host>")
def ping(host):
    try:
        tempo = ping3.ping(host, timeout=0.5)
    except Exception:
        tempo = None

    if tempo is None:
        return jsonify({
            "host": host,
            "alive": False,
            "rtt_ms": None
        }), 404

    return jsonify({
        "host": host,
        "alive": True,
        "rtt_ms": tempo * 1000
    })

if __name__ == "__main__":
    app.run(debug=True)