import websocket
import json


def on_open(ws):
    print("Connection opened")
    payload = {
        "method": "SUBSCRIBE",
        "params": [f"{trading_pair}@kline_{interval}"],
        "id": 1
    }
    ws.send(json.dumps(payload))

def on_message(ws, message):
    data = json.loads(message)
    kline = data['k']
    print(f"Zeit: {kline['t']} | Eröffnung: {kline['o']} | Hoch: {kline['h']} | Tief: {kline['l']} | Schluss: {kline['c']} | Volumen: {kline['v']}")

def on_close(ws, close_status_code, close_msg):
    print("WebSocket-Verbindung geschlossen")

def start_websocket():
    global trading_pair, interval
    trading_pair = input('Gib das Handelspaar ein (z.B. btcusdt): ')
    interval = input('Gib das Intervall ein (z.B. 1m, 5m): ')
    
    ws = websocket.WebSocketApp(
        "wss://stream.binance.com:9443/ws", 
        on_open=on_open,
        on_message=on_message,
        on_close=on_close
    )
    ws.run_forever()

if __name__ == "__main__":
    start_websocket()


       