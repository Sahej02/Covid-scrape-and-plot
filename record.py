import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

url = 'https://www.mohfw.gov.in/'
source = requests.get(url).text
soup = BeautifulSoup(source, 'lxml')

para = soup.find('div', class_ = 'content newtab')
line1 = str(para.find('p'))
time_obj = re.search(r"\d\d\.\d\d.+\s(PM|AM)", line1)
time = time_obj.group(0)
ind = -1
try:
	trial = para.find_all('tr')[ind].find_all('td')[1].text
except IndexError:
	ind = -2
finally:
	num = para.find_all('tr')[ind].find_all('td')[1].text
	num = re.search(r"\d+", num).group(0)

	# fn = para.find_all('tr')[ind].find_all('td')[2].text
	# fn = re.search(r"\d+", fn).group(0)

	cured = para.find_all('tr')[ind].find_all('td')[2].text
	cured = re.search(r"\d+", cured).group(0)

	death = para.find_all('tr')[ind].find_all('td')[3].text
	death = re.search(r"\d+", death).group(0)

	finsum = int(num) + int(cured) + int(death) #+ int(fn)

	with open("covid_data.csv",'a') as file_1:
	    file_1.write(time+","+num+","+cured+","+death+ "," + str(finsum) +"\n")