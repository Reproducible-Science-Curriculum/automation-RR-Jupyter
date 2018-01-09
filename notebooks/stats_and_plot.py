def calculate_statistic_over_time(data, category, continent, func=None):
    import numpy as np
    import pandas as pd

    if func is None:
        func = np.mean
        
    # Create a mask that selects the continent of choice
    mask_continent = data['continent'] == continent
    data_continent = data[mask_continent]

    # Loop through years and calculate the statistic of interest
    years = data_continent['year'].unique()
    summary = []
    for year in years:
        mask_year = data_continent['year'] == year
        data_year = data_continent[mask_year]
        value = func(data_year[category])
        summary.append((continent, year, value))

    # Turn the summary into a dataframe so that we can visualize easily
    summary = pd.DataFrame(summary, columns=['continent', 'year', category])
    return summary


def plot_statistic_over_time(data, category, func=None, cmap=None, ax=None, legend=True, sort=True):
    if ax is None:
        fig, ax = plt.subplots()
    if cmap is None:
        cmap = plt.cm.viridis
    
    if sort is True:
        # Sort the continents by the category of choice
        mean_values = df.groupby('continent').mean()[category]
        mean_values = mean_values.sort_values(ascending=False)
        continents = mean_values.index.values
    else:
        continents = np.unique(df['continent'])
    n_continents = len(continents)

    # Loop through continents, calculate its stat, and add a line
    for ii, continent in enumerate(continents):
        this_color = cmap(float(ii / n_continents))
        output = calculate_statistic_over_time(data, category, continent)
        output.plot.line('year', category, ax=ax, label=continent,
                         color=this_color)
        if legend is True:
            plt.legend(loc=(1.02, 0))
        else:
            ax.get_legend().set(visible=False)
        ax.set(ylabel=category, xlabel='Year',
               title='{} over time'.format(category))

    plt.setp(ax.lines, lw=4, alpha=.4)
    return ax