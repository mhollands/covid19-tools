# Quick script to plot cases with the dates aligned to first death

import core
import matplotlib.pyplot as plt
import numpy as np

countries = ["Italy", "China", "Korea, South", "US", "United Kingdom", "France", "Spain", "Germany"]
populations = [60.48e6, 1386e6, 51.47e6, 327.2e6, 66.44e6, 66.99e6, 46.66e6, 82.79e6]
status_options = ["confirmed", "deaths", "recovered"]
normalise_by_population = False;
ax_dict = {}
for status in status_options:
	ax_dict[status] = plt.subplots()[1]
	ax_dict[status].set_title(status)
	ax_dict[status].set_xlabel("Days since first death")
	if(normalise_by_population):
		ax_dict[status].set_ylabel("Population /%")

for country, population in zip(countries, populations):
	data_dict = core.get_cases_by_date(country)
	data_dict_since_thresh = {}
	threshold_date = np.min([data_dict["deaths"]["dates"][i] for i in range(len(data_dict["deaths"]["dates"])) if data_dict["deaths"]["cases"][i] >= 1])
	for status in status_options:
		if(normalise_by_population):
			ax_dict[status].plot([(data_dict[status]["dates"][i]-threshold_date).days for i in range(len(data_dict[status]["dates"]))], 100*np.array(data_dict[status]["cases"])/population)
		else:			
			ax_dict[status].plot([(data_dict[status]["dates"][i]-threshold_date).days for i in range(len(data_dict[status]["dates"]))], np.array(data_dict[status]["cases"]))

for status in status_options:
	ax_dict[status].legend(countries)

plt.show()