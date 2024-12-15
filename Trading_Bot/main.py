# main.py
from strategies.moving_average import MovingAverageStrategy
import plotly.io as pio
import plotly.express as px

pio.renderers.default = "browser"

def plot_signals(df, bullish_signal, bearish_signal):
    # Plotting der Daten und Signale
    fig = px.line(df, x='time', y=['close', 'slow_sma', 'fast_sma'])

    fig.update_xaxes(range=[df['time'].min(), df['time'].max()])

    # Hinzufügen der bullischen Signale
    for i, row in bullish_signal.iterrows():
        fig.add_vline(x=row['time'].timestamp(), line=dict(color='green', width=2, dash='dash'), 
                      annotation_text="Buy Signal", annotation_position="top left")

    # Hinzufügen der bärischen Signale
    for i, row in bearish_signal.iterrows():
        fig.add_vline(x=row['time'].timestamp(), line=dict(color='red', width=2, dash='dash'), 
                      annotation_text="Sell Signal", annotation_position="top right")

    fig.show()

def main(symbol):
    # Erstelle die MovingAverageStrategy Instanz
    strategy = MovingAverageStrategy(symbol)

    # Bullish und Bearish Signale analysieren
    bullish_signal, bearish_signal = strategy.analyze_crossovers()

    # Signale ausgeben
    print("Bullish Signals:")
    print(bullish_signal[['time', 'crossover']])  # Ausgabe nur der Zeit und des Signals
    print("\nBearish Signals:")
    print(bearish_signal[['time', 'crossover']])  # Ausgabe nur der Zeit und des Signals

    # Plot der Signale
    plot_signals(strategy.df, bullish_signal, bearish_signal)

if __name__ == '__main__':
    symbol = 'BTCUSDT'  # Beispiel: BTC/USDT, kann auf beliebige Kryptowährung geändert werden
    main(symbol)
