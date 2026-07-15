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
    import datetime

    sent_time = datetime.datetime.now()
    tempo = ping3.ping(host)
    received_time = datetime.datetime.now()

    delta = sent_time - received_time

    return jsonify({
        "host": host,
        "alive": tempo is not None,
        "rtt_ms": tempo * 1000 if tempo else None,
        "diff_ms": delta.microseconds if tempo else None
    })

if __name__ == "__main__":
    app.run(debug=True)