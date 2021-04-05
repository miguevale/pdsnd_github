import time
import pandas as pd
from pandas.tseries.offsets import SemiMonthEnd
import numpy as np

CITY_DATA = { 'chicago': 'data/chicago.csv',
              'new york city': 'data/new_york_city.csv',
              'washington': 'data/washington.csv' }

DOW_DATA = {'monday' : 1,
            'tuesday' : 2,
            'wednesday' : 3,
            'thursday' : 4,
            'friday' : 5,
            'saturday' : 6,
            'sunday' : 7}

MONTH_DATA = {'january' : 1,
              'february' : 2,
              'march' : 3,
              'april' : 4,
              'may' : 5,
              'june' : 6,
              'july' : 7,
              'august' : 8,
              'september' : 9,
              'october' : 10,
              'november' : 11,
              'december' : 12}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    while city not in CITY_DATA.keys():
        city = input('select the city: ')

    # get user input for month (all, january, february, ... , june)
    months = ['january','february','march','april','may','june','july','august','september','october','november','december']
    month = ''
    while month not in months + ['all']:
        month = input('select the month: ')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    dows = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    day = ''
    while day not in dows + ['all']:
        day = input('select the day of week: ')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    if month != 'all':
        df = df[df['Start Time'].dt.month == MONTH_DATA[month]]

    if day != 'all':
        df = df[df['Start Time'].dt.dayofweek == DOW_DATA[day]]

    return df


def time_stats(df):
    """
    Displays statistics on the most frequent times of travel.
    
    args:
        (DataFrame) df - dataframe to calculate statistics

    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    comm_mth = df['Start Time'].dt.month.mode()[0]
    comm_mth = list(MONTH_DATA.keys())[list(MONTH_DATA.values()).index(comm_mth)]
    print(f'The most common month is: {comm_mth}')

    # display the most common day of week
    comm_dow = df['Start Time'].dt.dayofweek.mode()[0]
    comm_dow = list(DOW_DATA.keys())[list(DOW_DATA.values()).index(comm_dow)]
    print(f'The most common day of week is: {comm_dow}')

    # display the most common start hour
    comm_hou = df['Start Time'].dt.hour.mode()[0]
    print(f'The most common hour is: {comm_hou}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """
    Displays statistics on the most popular stations and trip.
    
    args:
        (DataFrame) df - dataframe to calculate statistics
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    comm_sta = df['Start Station'].mode()[0]
    print(f'The most commonly used start station is: {comm_sta}')

    # display most commonly used end station
    comm_end = df['End Station'].mode()[0]
    print(f'The most commonly used end station is: {comm_end}')

    # display most frequent combination of start station and end station trip
    comm_comb = (df['Start Station'] + ' - ' + df['End Station']).mode()[0]
    print(f'The most commonly combination is: {comm_comb}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    tot_tt = df['Trip Duration'].sum()
    print(f'The total travel time is: {round(tot_tt,0)} secs')
    print(f'or {round(tot_tt/3600,0)} hours')

    print('-'*20)
    # display mean travel time
    mea_tt = df['Trip Duration'].mean()
    print(f'The mean travel time is: {round(mea_tt,0)} secs')
    print(f'or {round(mea_tt/60,0)} mins')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
