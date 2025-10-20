from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

# TODO: Connect your broker API here

@app.route('/api/trade', methods=['POST'])
def trade():
    data = request.get_json()
    signal = data.get('signal')
    
    # Example: simple log message
    now = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"[{now}] Received signal: {signal}")

    # TODO: implement broker API logic for BUY/SELL/CLOSE ALL
    message = f"Trade signal {signal} processed successfully"
    return jsonify({'message': message})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
