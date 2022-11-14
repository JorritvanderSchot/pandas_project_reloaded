#%% Importing modules
import pandas as pd
import matplotlib.pyplot as plt

#%% Defining the function to plot monthly anomalies
def monthly_T_anomalies(data, savedirectory, station, variable, 
                        start, end):
    """
    Calculates the monthly temperature anomalies from AWS data.

    Parameters:
    data (pd.DataFrame): Panda dataframe from AWS data. 
    savedirectory (string): Path to directory where figure will be saved.
    station (string or int): Select station from the data by name.
    variable (string): Select 't', 'tmin' or 'tmax'.
    start (string): Select the start of the time series 'yyyy-mm-dd'.
    end (string): Select the end of the time series 'yyyy-mm-dd'.
    
    Returns:
    figure: Figure showing the monthly anomalies of the chosen variable.
   """
    subset = data[data["station"] == station][start:end]
    df_clim = subset["1991-01":"2020-12"]
    clim = df_clim.groupby(df_clim.index.month).mean()
    clim.index.name = "month"
    monthly_means = subset.groupby([subset.index.year, subset.index.month]).mean()
    monthly_means.index.names = ["year", "month"]
    anom = monthly_means - clim
    years = anom.index.get_level_values(0).astype(str)
    months = anom.index.get_level_values(1).astype(str)
    dates = pd.to_datetime(years + "-" + months + "-01")
    anom = anom.set_index(dates)
    anom[[variable]].plot(title='Monthly anomalies of ' + str(variable) +
    '\n compared to the climate normal 1991-2020')
    plt.show()
    plt.savefig(savedirectory + 'monthly_anomalies.jpg')