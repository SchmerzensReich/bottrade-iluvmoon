import websocket
import json
import pandas as pd
from strategies.moving_average import MovingAverageStrategy
from main import plot_signals


# Globale Instanz der Strategie
strategy = None

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
    
    # Wenn die Daten vollständig sind (z.B. abgeschlossenes Kline), aktualisiere die Strategie
    if kline['x']:  # "x" ist True, wenn Kline abgeschlossen ist
        new_data = {
            'time': pd.to_datetime(kline['t'], unit='ms'),
            'open': float(kline['o']),
            'high': float(kline['h']),
            'low': float(kline['l']),
            'close': float(kline['c']),
            'volume': float(kline['v']),
        }
        # Daten an die MovingAverageStrategy übergeben
        strategy.update_data(new_data)
        # Crossovers analysieren
        bullish_signal, bearish_signal = strategy.analyze_crossovers()
        
        # Ausgabe der Signale (optional)
        print("Bullish Signals:")
        print(bullish_signal[['time', 'crossover']])
        print("\nBearish Signals:")
        print(bearish_signal[['time', 'crossover']])
        
        # Optional: Plot anzeigen
        plot_signals(strategy.df, bullish_signal, bearish_signal)

def on_close(ws, close_status_code, close_msg):
    print("WebSocket-Verbindung geschlossen")

def start_websocket():
    global trading_pair, interval, strategy
    
    # Eingabe für Handelspaar und Intervall
    trading_pair = input('Gib das Handelspaar ein (z.B. btcusdt): ')
    interval = input('Gib das Intervall ein (z.B. 1m, 5m): ')
    
    # Erstelle eine Instanz der Strategie
    strategy = MovingAverageStrategy(trading_pair)
    
    # Starte WebSocket-Verbindung
    ws = websocket.WebSocketApp(
        "wss://stream.binance.com:9443/ws", 
        on_open=on_open,
        on_message=on_message,
        on_close=on_close
    )
    ws.run_forever()

if __name__ == "__main__":
    start_websocket()



       
