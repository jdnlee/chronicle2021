import requests
from bs4 import BeautifulSoup
import sys
import csv
import re

def Max_Numbers():
    URL = 'http://www.bom.gov.au/act/forecasts/canberra.shtml'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find_all("em", class_='max')
    results_string = str(results)
    return results_string

def rain():
    URL = 'http://www.bom.gov.au/act/forecasts/canberra.shtml'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find_all("em", class_='pop')
    results_string = str(results)
    found = re.findall('\d+(?=\%)', results_string)
    found_string = str(found)
        
    #return results_string
    return found

def summary():
    URL = 'http://www.bom.gov.au/act/forecasts/canberra.shtml'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find_all("dd", class_='summary')
    results_string = str(results)
    found = re.findall('(?<=\>)(.*?)(?=\<)', results_string)

    return found

def day_otw():
    URL = 'http://www.bom.gov.au/act/forecasts/canberra.shtml'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find_all("h2")
    results_string = str(results)
    found = re.findall('(?<=\>)(.*?)(?=\<)', results_string)
    return found

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["temp", "date", "rain", "weather"])
    writer.writerow([Max_Numbers()[17:19], day_otw()[0], rain()[0] ,summary()[0]])
    writer.writerow([Max_Numbers()[42:44], day_otw()[2], rain()[1], summary()[2]])
    writer.writerow([Max_Numbers()[67:69], day_otw()[4], rain()[2], summary()[4]])
    writer.writerow([Max_Numbers()[92:94], day_otw()[6], rain()[3], summary()[6]])
    writer.writerow([Max_Numbers()[117:119], day_otw()[8], rain()[4], summary()[8]])
    writer.writerow([Max_Numbers()[142:144], day_otw()[10], rain()[5], summary()[10]])
    writer.writerow([Max_Numbers()[167:169], day_otw()[12], rain()[6], summary()[12]]) 
    