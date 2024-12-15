import websocket
import json



def start_websocket():
    ws = websocket.WebSocketApp(
        "wss://stream.binance.com:9443/ws", 
        on_open=on_open,
        on_message=on_message,
        on_close=on_close
    )
    ws.run_forever()


    trading_pair = input('')
    interval = input('')

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
    printf(f"Zeit: {kline['t']} | Eröffnung: {kline['o']} | Hoch: {kline['h']} | Tief: {kline['l']} | Schluss: {kline['c']} | Volumen: {kline['v']}")

def on_close(ws, close_status_code, close_msg):
    print("WebSocket-Verbindung geschlossen")


       
