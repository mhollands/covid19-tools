from urllib.request import urlopen
from urllib.parse import quote
from datetime import datetime

def get_text_from_url(url):
	text = urlopen(url).read().decode()
	return str.join('',text)

# Return a list of locals, containing information of country name, slug and provinces
def get_all_locals():
	url = "https://api.covid19api.com/countries"
	text = get_text_from_url(url)
	entries = eval(text)
	return entries

# return slug for a given country
def get_all_countries():
	entries = get_all_locals()
	return [x["Country"] for x in entries]

# return slug for a given country
def get_country_slug(country):
	entries = get_all_locals()
	matching_entries = [x for x in entries if x["Country"] == country]
	if(len(matching_entries) < 1):
		print("No country matches '{0}'".format(country))
		return None
	return matching_entries[0]["Slug"]

# Return list of provinces for given country
def get_country_provinces(country):
	entries = get_all_locals()
	matching_entries = [x for x in entries if x["Country"] == country]
	if(len(matching_entries) < 1):
		print("No country matches '{0}'".format(country))
		return None
	return matching_entries[0]["Provinces"]

#For a given country and optionally province, for each status get the number of cases for each category
def get_cases_by_date(country, province=None):
	case_status = ["confirmed", "deaths", "recovered"]
	country =  get_country_slug(country)
	data_dict = {}	
	for status in case_status:
		if(province is None):
			url = "https://api.covid19api.com/total/country/{0}/status/{1}".format(quote(country), quote(status))
		else:
			url = "https://api.covid19api.com/country/{0}/status/{1}".format(quote(country), quote(status))
		data = get_text_from_url(url)
		data = eval(data)

		if(province is not None):
			data = [x for x in data if x["Province"] == province]
		data_dict[status] = {"dates":[datetime.strptime(x["Date"], "%Y-%m-%dT%H:%M:%SZ") for x in data], "cases": [x["Cases"] for x in data]}
	return data_dict