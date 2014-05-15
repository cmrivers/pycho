pycho
=====

Python wrapper for [Project Tycho](http://www.tycho.pitt.edu/) Nationally Notifiable Disease Surveillance System database.

According to their [website](http://www.tycho.pitt.edu/), "the Project Tycho™ database includes data from all weekly notifiable disease reports for the United States dating back to 1888. These data are freely available to anybody interested. Additional U.S. and international data will be released twice yearly."

### Before using pycho

You must register for an account at [Project Tycho](http://www.tycho.pitt.edu/), then request an api key [here.](http://www.tycho.pitt.edu/apikey.php)


### Installation and requirements

To install pycho:

    git clone https://github.com/cmrivers/pycho.git
    cd ./pycho
    python setup.py install

[Pandas](http://pandas.pydata.org/) is the only requirement.

### Basic usage

First things first:

    apikey = 'YOUR API KEY'

The core function returns all data matching specific parameters. Required parameters are the api key,
loc_type (values are city or state), event (values are deaths or cases), and either a disease or a location (either city parameter or state parameter). Optional arguments are state and end years. The function returns a pandas dataframe of the results


    In[0]: pycho.get_data(apikey, loc_type='state', event='cases', disease='measles', state='fl')
    Out[0]:
        year week      loc state country loc_type number  event
    0   1927   47  FLORIDA    FL      US    STATE      2  CASES
    1   1927   48  FLORIDA    FL      US    STATE      1  CASES
    2   1927   49  FLORIDA    FL      US    STATE      3  CASES
    3   1927   51  FLORIDA    FL      US    STATE      5  CASES

Find which diseases are available by location and time period:

    In[1]: california_data = pycho.get_info(apikey, 'state', 'cases', state='ca')
    Out[1]:
                                   disease       start         end records
    0                              ANTHRAX  1942-01-04  1945-01-13     144
    1                             BOTULISM  1951-12-30  1952-12-06       6
    2         BRUCELLOSIS [UNDULANT FEVER]  1945-01-14  1981-07-04     711
    3               CHICKENPOX [VARICELLA]  1975-03-09  2013-04-27      40
    4                            CHLAMYDIA  2006-01-01  2013-08-10     371

List all available states:

    In [2]: pycho.get_states(apikey)
    Out[2]:
    ['alaska',
     'alabama',
     'arkansas',
     'american samoa',
     'arizona',
     'california']

List all available cities:

    In [3]: pycho.get_cities(apikey)
    Out[3]:
    ['ketchikan',
     'alameda',
     'anniston',
     'berkley',
     'bessemer''

List all available diseases:

    In [4]: pycho.get_disease(apikey)
    Out[4]:
    ['anthrax',
     'botulism',
     'brucellosis [undulant fever]',
     'chickenpox [varicella]',
     'chlamydia']
