import numpy as np
import matplotlib.dates as mpdt
import matplotlib.pyplot as plt 
import pandas as pd 
import re
from datetime import datetime
from pandas.plotting import register_matplotlib_converters


def dt(dates):
	dtimes = []
	for x in dates:
		dtime = re.sub(r'\sat\s', " ", x)
		date_obj = datetime.strptime(dtime, "%d.%m.%Y %I:%M %p")
		dtimes.append(date_obj)
	return dtimes

register_matplotlib_converters()
df = pd.read_csv("covid_data.csv", header = 0, index_col = False)
dates = df['Time']
dtimes = dt(dates)

final_dates = mpdt.date2num(dtimes)
plt.xlabel("Time")
plt.ylabel("Number of Cases")
plt.title("Cases v Time")
plt.plot_date(final_dates, df['IN'], '-', label = "Indian Nationals")
plt.plot_date(final_dates, df['"Total"'], '-', label = "Total")
plt.legend()
plt.grid(which = 'both')
plt.show()