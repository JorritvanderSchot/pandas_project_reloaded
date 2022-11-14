import argparse
import os
from . import hotfrostdays
from . import io_aws_data
from . import monthly_anomalies

#Define type 'dir_path'
def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)

def temperature_calc():
    """Entry point for the function temperature_calc"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--fn",
        required=True,
        help="Absolute path of the file that contains AWS data."
    )
    parser.add_argument(
        "--savedirectory",
        type=dir_path,
        required=True,
        help="Directory where the figure for monthly anomalies will be stored."   
    )
    parser.add_argument(
        "--station",
        required=True,
        help="Select if you want AWS data from 'Graz' or 'Innsbruck'."
    )
    parser.add_argument(
        "--hotorfrost",
        default='hot',
        required=False,
        help="Do you want to calculate 'hot' or 'frost' days?"   
    )
    parser.add_argument(
        "--threshold",
        default=25,
        required=False,
        help="Threshold temperature used for calculation of hot or frost days."   
    )
    parser.add_argument(
        "--start",
        default='1900-01-01',
        required=False,
        help="Start of the period to analyze (default = '2022-10-31')"   
    )
    parser.add_argument(
        "--end",
        default='2022-10-31',
        required=False,
        help="End of the period to analyze (default = '1900-01-01')"   
    )
    parser.add_argument(
        "--variable",
        default='t',
        required=False,
        help="Variable for which the monthly anomalies will be plotted ('t', 'tmin' or 'tmax')."   
    )

    args = parser.parse_args()

    #Convert stations into station numbers
    if args.station == 'Graz':
        station_no = 30
    elif args.station == 'Innsbruck':
        station_no = 39
    else:
        raise argparse.ArgumentTypeError(
            "Please select either 'Graz' or 'Innsbruck'")   

    i_data = io_aws_data.io_aws_data(args.fn)

    hotfrostdays.hotfrostdays(data = i_data, station = station_no, variable = args.variable, hotorfrost = args.hotorfrost, 
                start = args.start, end = args.end, threshold = args.threshold, 
                savedirectory = args.savedirectory)
    
    monthly_anomalies.monthly_T_anomalies(data = i_data, savedirectory = args.savedirectory, 
                                            station = args.station, variable = args.variable,
                                            start = args.start, end = args.end)