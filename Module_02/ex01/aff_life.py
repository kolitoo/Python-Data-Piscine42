from load_csv import load
import pandas as pd
import sys
import matplotlib.pyplot as plt

def main():
    """
    This fonction load a .csv with load().
    It search 'france' in the df.DataFrame.
    It search the years who are at column.[:1] mean we start after the first.
    It search the data.[0][1:] mean we search at line 0 and we skip the first.
    It display the graph.
    plt.xticks(years[::40]) means it print all the 40 years.
    plt.yticksmeans it print between 30 and 101 all the 10 values.

    """
    try:
        df = load(sys.argv[1])
        if df is None:
            raise AssertionError("Loading failed.")
        data_france = df[df['country'] == 'France']
        # print(data_france)
        years = data_france.columns[1:]
        life_expectancy = data_france.values[0][1:]

        plt.plot(years, life_expectancy)
        plt.title('France Life expectancy Projections')
        plt.xlabel('Year')
        plt.xticks(years[::40])
        plt.ylabel('Life expectancy')
        plt.yticks(range(30, 101, 10))
        plt.show()
        return
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)


if __name__ == "__main__":
    main()