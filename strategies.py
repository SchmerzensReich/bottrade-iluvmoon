def strategy_1(kline_data):
    # Beispiel für eine einfache Strategie
    print(f"Strategie 1: Verarbeite Kline-Daten: {kline_data}")
    if float(kline_data['c']) > float(kline_data['o']):
        print("Strategie 1: Kauf!")
    else:
        print("Strategie 1: Verkauf!")

def strategy_2(kline_data):
    # Beispiel für eine zweite Strategie
    print(f"Strategie 2: Verarbeite Kline-Daten: {kline_data}")
    if float(kline_data['v']) > 100:
        print("Strategie 2: Hohe Volatilität!")
