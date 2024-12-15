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

# Diese Funktion wird nicht mehr direkt genutzt, weil die Logik bereits in der WebSocket-Verbindung enthalten ist.
if __name__ == '__main__':
    pass
