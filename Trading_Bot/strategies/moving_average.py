# strategies/moving_average.py
import numpy as np
import pandas as pd
from data_fetcher import get_data

class MovingAverageStrategy:
    def __init__(self, symbol, timeframe="1000 days ago UTC", candlesize="1d", fsma_period=10, ssma_period=100):
        # Marktdaten holen
        self.symbol = symbol
        self.timeframe = timeframe
        self.candlesize = candlesize
        self.fsma_period = fsma_period
        self.ssma_period = ssma_period
        self.df = self.fetch_data()

    def fetch_data(self):
        # Holen der Daten über das data_fetcher-Modul
        df = get_data(self.symbol, self.timeframe, self.candlesize)
        
        # Berechnung der gleitenden Durchschnitte
        df['slow_sma'] = df['close'].rolling(self.ssma_period).mean()
        df['fast_sma'] = df['close'].rolling(self.fsma_period).mean()

        df['prev_fast_sma'] = df['fast_sma'].shift(1)
        df['prev_slow_sma'] = df['slow_sma'].shift(1)

        df.dropna(inplace=True)
        return df

    def find_crossover(self, fast_sma, prev_fast_sma, slow_sma):
        # Bestimmen, ob es sich um ein bullish oder bearish crossover handelt
        if fast_sma > slow_sma and prev_fast_sma < slow_sma:
            return 'bullish crossover'
        elif fast_sma < slow_sma and prev_fast_sma > slow_sma:
            return 'bearish crossover'
        return None

    def analyze_crossovers(self):
        # Suchen nach Crossovers und Hinzufügen zum DataFrame
        self.df['crossover'] = np.vectorize(self.find_crossover)(self.df['fast_sma'], self.df['prev_fast_sma'], self.df['slow_sma'])

        # Bullish und Bearish Signale extrahieren
        bullish_signal = self.df[self.df['crossover'] == 'bullish crossover']
        bearish_signal = self.df[self.df['crossover'] == 'bearish crossover']
        
        return bullish_signal[['time', 'crossover']], bearish_signal[['time', 'crossover']]

