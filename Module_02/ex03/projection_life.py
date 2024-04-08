from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    This main display a point graph.
    It load 2 .csv with loader.
    We search the values for 1900.
    We make the graph with plt.
    scatter is use for cloud points graph.
    xscale is use to change the scale(logarithme here).
    xticks to select what markers we wanted."""
    try:
        path = ["income_per_person_gdppercapita_ppp_inflation_adjusted.csv",
                "life_expectancy_years.csv"]
        print(path[0], path[1])
        gdp = load(path[0])
        life_exp = load(path[1])
        if gdp is None or life_exp is None:
            raise AssertionError("Loading failed.")
        gdp_1900 = gdp.loc[:, '1900']
        life_exp_1900 = life_exp.loc[:, '1900']
        plt.title("1900")
        plt.scatter(gdp_1900, life_exp_1900)
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life Expectancy")
        plt.xscale('log')
        plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
        plt.show()
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
        return


if __name__ == "__main__":
    main()
