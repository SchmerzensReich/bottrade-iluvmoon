from GetData import start_websocket
import strategies
import json

# Diese Funktion wird für die Weiterverarbeitung der abgerufenen Kline-Daten aufgerufen
def data_callback(kline_data):
    # Hier kannst du entscheiden, welche Strategie verwendet werden soll
    strategies.strategy_1(kline_data)  # Beispiel für Strategie 1
    strategies.strategy_2(kline_data)  # Beispiel für Strategie 2

# Anpassung der WebSocket-Funktionen, um die Daten an den Callback weiterzugeben
def on_message(ws, message):
    print("Nachricht empfangen:", message)
    data = json.loads(message)
    kline = data['k']
    # Rufe den Callback mit den Kline-Daten auf
    data_callback(kline)

if __name__ == "__main__":
    # Hier startet der WebSocket
    start_websocket()



