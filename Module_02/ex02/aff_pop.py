from load_csv import load
import sys
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import pandas as pd


def millions_formatter(x, pos):
    """
    Formatter function to display population in millions with 'M' suffix.
    """
    return f'{x/1e6:.0f}M'


def main():
    """
    """
    try:
        # df_belgium = df[df['country'] == 'Belgium']
        # df_belgium_years = df_belgium.columns[1:]
        # df_belgium_population = df_belgium.values[0][1:]
        path = sys.argv[1]
        df = load(path)
        df_france = df[df['country'] == 'France']
        index_2050 = df_france.columns.get_loc('2050')
        df_france_years = df_france.columns[1:index_2050 + 1]
        df_france_population = df_france.values[0][1:index_2050 + 1].flatten()
        df_france_population = [float(value[:-1]) * 1e6 for value in df_france_population]
        print(df_france_population)

        plt.plot(df_france_years, df_france_population)
        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.xticks(df_france_years[::40])
        plt.ylabel("Population")
        plt.yticks()
        plt.tight_layout()
        plt.show()
        # print(df_france_population)
        # print(df_belgium)

        return
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)


if __name__ == "__main__":
    main()