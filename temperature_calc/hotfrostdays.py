#%%Importing modules
import pandas as pd
import matplotlib.pyplot as plt

#%% Function definition
def hotfrostdays(data, savedirectory, station, variable, hotorfrost, threshold, 
                start='1900-01-01', end='2022-10-31'):
    """
    Calculates the number of hot or frost days from AWS data.

    Parameters:
    data (pd.DataFrame): Panda dataframe from AWS data. 
    savedirectory (string): Path to directory where figure will be saved.
    station (string or int): Select station from the data by name.
    variable (string): Select 't', 'tmin' or 'tmax'.
    hotorfrost (string): Select hot days ('hot') or frost days ('frost').
    threshold (int): Threshold value used for calculation of hot or frost days.
    start (string): Select the start of the time series 'yyyy-mm-dd'.
    end (string): Select the end of the time series 'yyyy-mm-dd'.
    
    Returns:
    string: Statement about the number of hot or frost days.
    figure: Figure showing the annual trend in number of hot or frost days.
   """
    subset = data[data["station"] == station][start:end]
    hot_days = subset[subset["t"] >= int(threshold)]
    frost_days = subset[subset["t"] < int(threshold)]
    no_hot_days = len(hot_days)
    no_frost_days = len(frost_days)
    if hotorfrost == 'hot':
        hot_days[variable].resample("Y").count().plot(title='Days with ' + str(variable) + ' ≥' + str(threshold), 
                                                xlim=(start, end))
        plt.savefig(savedirectory + 'annual_hotdays.jpg')
        plt.show()
        print("{} days with temperature ≥ {} in the period {} until {}".format(
        str(no_hot_days), str(threshold), str(start), str(end)))
    elif hotorfrost == 'frost':
        frost_days[variable].resample("Y").count().plot(title='Days with ' + str(variable) + ' <' + str(threshold))
        plt.savefig(savedirectory + 'annual_frostdays.jpg')
        plt.show()
        print("{} days with temperature < {} in the period {} until {}".format(
        str(no_frost_days), str(threshold), str(start), str(end)))
    else:
        print('Invalid input for "hotorfrost". Please enter "hot" or "frost"')