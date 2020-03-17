import sys, getopt
import core
import os
import matplotlib.pyplot as plt
import pandas as pd
pd.plotting.register_matplotlib_converters(explicit=False)

def plot_cases_by_date(data_dict):
	status_options = ["confirmed", "deaths", "recovered"]
	for status in status_options:
		plt.plot(data_dict[status]["dates"], data_dict[status]["cases"])
	plt.legend(status_options,loc='upper left')
	plt.xticks(rotation='vertical')
	plt.tight_layout()
	plt.show()

opts, args = getopt.getopt(sys.argv[1:],"hc:p:sg",["help","country=","province=","save","graph"])

graph = False
save=False
province = None
country = None
for opt in opts:
	if(opt[0] in ("-h", "--help")):
		print("syntax: --country <country> [--province <province>] [--outfile <outputfile>]")
		print("-g --graph \t Draw a graph")
	if(opt[0] in ("-c", "--country")):
		country = opt[1]
	if(opt[0] in ("-p", "--province")):
		province = opt[1]
	if(opt[0] in ("-s", "--save")):
		save = True
	if(opt[0] in ("-g", "--graph")):
		graph = True

if(country is None):
	print("Must specify a country")
	countries = core.get_all_countries()
	print("Countries are: {0}".format(countries))
	os._exit(1)

if(province is None):
	provinces = core.get_country_provinces(country)
	if(len(provinces) > 1):
		print("FYI provinces of {0} are: {1}".format(country, provinces))
	else:
		print("FYI data for {0} is not broken into provinces".format(country))

data_dict = core.get_cases_by_date(country, province=province)

if(graph):
	plot_cases_by_date(data_dict)

if(save):
	pd.DataFrame(data_dict["deaths"]).to_csv("deaths.csv")
	pd.DataFrame(data_dict["confirmed"]).to_csv("confirmed.csv")
	pd.DataFrame(data_dict["recovered"]).to_csv("recovered.csv")