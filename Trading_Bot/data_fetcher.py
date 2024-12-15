# data_fetcher.py
from binance.client import Client
import pandas as pd

client = Client()

def get_data(symbol, timeframe="1000 days ago UTC", candlesize=Client.KLINE_INTERVAL_1DAY):
    # Abrufen der historischen Daten für das angegebene Symbol
    candles = client.get_historical_klines(symbol, candlesize, timeframe)
    
    data = []
    for candle in candles:
        data.append({
            'time': pd.to_datetime(candle[0], unit='ms'),
            'open': float(candle[1]),
            'high': float(candle[2]),
            'low': float(candle[3]),
            'close': float(candle[4]),
            'volume': float(candle[5]),
        })
    
    # DataFrame erstellen
    df = pd.DataFrame(data)[['time', 'open', 'high', 'close']]
   
    return df
