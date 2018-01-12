import pandas as pd


VERBOSE = 0
def read_data(filepath):
    """reads csv file in as pandas data frame
    Args:
      filepath: path to file
    Returns:
      Pandas data frame
    Raises:
      File not found error
    """
    try:
        df = pd.read_csv(filepath)
        return df
    except FileNotFoundError:
        print("Couldn't find data file, check path? You tried", filepath)


def calculate_statistic_over_time(data, category, continent, func, VERBOSE=0):
    """calculate values of a statistic through time

    Args:
        data: a pandas data frame
        category: one of the column headers of the data frame (e.g. 'lifeexp')
        continent: possible value of the continent column of that data frame (e.g. 'asia')
        func: the funtion to apply to data values (e.g. np.mean)
        
    Returns:
        a summary table of value per year.

    """
    
    # Check values
    assert category in data.columns.values
    assert 'continent' in data.columns.values
    assert continent in data['continent'].unique()
    
    # Create a mask that selects the continent of choice
    mask_continent = data['continent'] == continent
    data_continent = data[mask_continent]
    
    
    # Loop through years and calculate the statistic of interest
    years = data_continent['year'].unique()
    if VERBOSE:
        print("years include", years)
    summary = []
    for year in years:
        mask_year = data_continent['year'] == year
        data_year = data_continent[mask_year]
        value = func(data_year[category])
        summary.append((continent, year, value))

    # Turn the summary into a dataframe so that we can visualize easily
    summary = pd.DataFrame(summary, columns=['continent', 'year', category])
    return summary

