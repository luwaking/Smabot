from flask import Flask, request, jsonify
import datetime
import random  # Tusaale ahaan signal generator (SMA crossover simulation)

app = Flask(__name__)

# -----------------------------
# CONFIGURATION
# -----------------------------
SMA_FAST = 10
SMA_SLOW = 30
LOT_SIZE = 0.1
STOP_LOSS_PIPS = 30
TAKE_PROFIT_PIPS = 60

# TODO: Replace with your broker API logic
# Example: MetaTrader5, Binance, etc.

# In-memory trade log
trade_log = []

# -----------------------------
# HELPER FUNCTIONS
# -----------------------------
def calculate_lot_size():
    # Placeholder for risk calculation
    return LOT_SIZE

def execute_trade(signal):
    """Simulate trade execution (replace with broker API)"""
    now = datetime.datetime.now().strftime("%H:%M:%S")
    lot = calculate_lot_size()
    trade = {
        "time": now,
        "signal": signal,
        "lot": lot,
        "SL": STOP_LOSS_PIPS,
        "TP": TAKE_PROFIT_PIPS
    }
    trade_log.append(trade)
    print(f"[{now}] Executed {signal} trade: {lot} lots, SL {STOP_LOSS_PIPS}, TP {TAKE_PROFIT_PIPS}")
    return f"{signal} trade executed: {lot} lots"

# -----------------------------
# API ROUTES
# -----------------------------
@app.route('/api/trade', methods=['POST'])
def trade():
    data = request.get_json()
    signal = data.get('signal', None)
    
    if signal in ['BUY', 'SELL', 'CLOSE']:
        message = execute_trade(signal)
        return jsonify({'message': message})
    else:
        return jsonify({'message': 'Invalid signal'}), 400

@app.route('/api/auto_signal', methods=['GET'])
def auto_signal():
    """Simulate SMA crossover signal (replace with real SMA logic)"""
    # Random example: BUY or SELL
    signal = random.choice(['BUY', 'SELL'])
    message = execute_trade(signal)
    return jsonify({'signal': signal, 'message': message})

@app.route('/api/log', methods=['GET'])
def get_log():
    """Return all executed trades"""
    return jsonify(trade_log)

# -----------------------------
# MAIN
# -----------------------------
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
