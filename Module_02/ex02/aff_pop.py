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
        path = sys.argv[1]
        df = load(path)

        df_france = df[df['country'] == 'France']
        df_belgium = df[df['country'] == 'Belgium']
        index_2050 = df_france.columns.get_loc('2050')
        
        df_france_years = df_france.columns[1:index_2050 + 1]
        df_belgium_years = df_belgium.columns[1:index_2050 + 1]
        df_france_population = df_france.values[0][1:index_2050 + 1].flatten()
        df_france_population = [float(value[:-1]) * 1e6 for value in df_france_population]
        df_belgium_population = df_belgium.values[0][1:index_2050 + 1].flatten()
        df_belgium_population = [float(value[:-1]) * 1e6 for value in df_belgium_population]

        plt.plot(df_belgium_years, df_belgium_population, label='Belgium')
        plt.plot(df_france_years, df_france_population, label='France')
        plt.title("Population Projections of {} and {}".format("France", "Belgium"))
        plt.xlabel("Year")
        plt.xticks(df_france_years[::40])
        plt.ylabel("Population")
        y_ticks = [int(val / 1000000) for val in range(0, 70000001, 10000000)]
        y_ticks_labels = [f"{val}M" for val in y_ticks]
        print(y_ticks_labels)
        plt.yticks([val * 1e6 for val in y_ticks], y_ticks_labels)
        plt.tight_layout()
        plt.legend(loc='lower right')
        plt.show()
        return

    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)


if __name__ == "__main__":
    main()