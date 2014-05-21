#/usr/bin/python
# -*- coding: utf-8 -*-

'''
  -------------
 * Caitlin Rivers
 * [cmrivers@vbi.vt.edu](cmrivers@vbi.vt.edu)
  -------------
'''

import requests
import csv
import pandas as pd
import urllib
import xml.etree.ElementTree as ET


def _detailed_query(query, apikey, loc_type, disease=None, event='cases', city=None, state=None,  start=None, end=None):


    url = 'http://www.tycho.pitt.edu/api/{}?'.format(query)
    parameters = {'event':event, 'disease':disease, 'loc_type':loc_type, 'loc':city, 'state':state, 'start':start, 'end':end}
    for key, value in parameters.iteritems():
        if value is not None:
            part = '{}={}&'.format(key, value)
            url = url+part

    url = url+'apikey='+apikey+'.csv'
    url = requests.get(url)
    api_response = url.text

    try:
        reader =  csv.reader(api_response.split('\n'), delimiter=',')
        headers = reader.next()
        dat = pd.DataFrame([row for row in reader], columns=headers)

        return dat
    except:
        print('API error: {}'.format(url.text))



def get_data(apikey, loc_type, disease, event='cases', city=None, state=None,  start=None, end=None):
    """
    Fetches data from Tycho API.

    REQUIRED PARAMETERS:
    apikey: api key
    loc_type: values are city or state
    event: options are cases or deaths. defaults to cases
    disease: see get_diseases() for available options

    city: name of city
    OR
    state: two letter abbreviation for state

    OPTIONAL PARAMETERS
    start: start year
    end: end year

    RETURNS
    pandas dataframe of results
    """
    query = 'query'
    data = _detailed_query(query, apikey, loc_type, disease, event, city, state,  start, end)

    return data



def get_cities(apikey):
    """
    Returns list of available cities for Tycho MMWR data.
    """
    query = 'cities'
    url = 'http://www.tycho.pitt.edu/api/{}?apikey={}.xml'.format(query, apikey)
    root = ET.parse(urllib.urlopen(url)).getroot()

    dat = {}
    row = 0
    for item in root.findall('row'):
        loc = item.find('loc').text
        states = item.find('state').text
        entry = {'state':states, 'citiy':loc}
        row += 1

        dat[row] = entry

    df = pd.DataFrame(dat).T

    return df



def get_states(apikey):
    """
    Returns list of states and territories available for Tycho MMWR data
    """
    query = 'states'
    url = 'http://www.tycho.pitt.edu/api/{}?apikey={}.xml'.format(query, apikey)
    root = ET.parse(urllib.urlopen(url)).getroot()

    entries = {}
    row = 0
    for item in root.findall('row'):
        loc = item.find('loc').text
        states = item.find('state').text
        entry = {'abrv':states, 'state':loc}
        row += 1

        entries[row] = entry

    df = pd.DataFrame(entries).T

    return df


def get_disease(apikey):
    """
    Returns list of diseases available for Tycho MMWR data
    """
    query = 'diseases'
    results = _get_options(query, apikey)

    return results



def get_info(apikey, loc_type, event, disease=None, state=None, city=None):
    """
    Returns data availability, e.g.first date data were collected, most
    recent collection date, and number of available records by disease and location.
    REQUIRED
    apikey: api key
    loc_type: options are city or state
    event: options are cases or deaths

    disease: see get_diseases() for available options
    OR
    state: two letter abbreviate for state
    OR
    city: name of city

    RETURNS
    pandas dataframe
    """
    query = 'info'
    data = _detailed_query(query=query, apikey=apikey, loc_type=loc_type, event=event, disease=disease, state=state, city=city)

    return data
