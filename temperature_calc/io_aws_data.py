#%% Importing modules
import os
import pandas as pd

#%% Function definition
def io_aws_data(fn):
    """ Function to import downloaded AWS data."""
    df = pd.read_csv(fn, parse_dates=["time"], index_col="time")
    return df