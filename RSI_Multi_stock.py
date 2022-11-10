import RSI_Divergence



def main():
    m = RSI_Divergence.Master(5, 25)
    symbol_list = ['SPY', 'GOOG']
    for symbol in symbol_list:
        print("---------")
        m.RSI_divergence(symbol)


if __name__ == '__main__':
    main()