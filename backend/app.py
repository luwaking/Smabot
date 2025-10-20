from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/trade', methods=['POST'])
def trade():
    data = request.get_json()
    signal = data.get('signal')
    # TODO: Halkan ku dar broker API calls
    print(f"Received signal: {signal}")
    return jsonify({'message': f'Trade signal {signal} processed successfully'})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
