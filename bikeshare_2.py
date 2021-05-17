#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import pandas as pd
import numpy as np
import sys


# In[2]:


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


# In[3]:


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
    city =input("\n Please select a city from the following:\n Chicago, New York City, Washington \n")
    city = city.strip().lower()
    while True:
        if city not in ("chicago", "new york city", "washington"):
            print("\n City Not found!!!  ")
            sys.exit("Please restart the program... Exiting!!")
        else:
            print("\n Selected City is: '{}' ".format(city.title()))
            break
    # get user input for month (all, january, february, ... , june)
    month = input("\n Please selcet a month from the following:\n January, February, March, April, May, June, All \n")
    month = str(month.strip().lower())
    while True:
        if month not in ("january", "february", "march", "april", "may", "june", "all"):
            print("\n Month Not found!!!")
            sys.exit("Please restart the program... Exiting!!")
        else:
            print("\nSelected Month is: '{}' ".format(month.title()))
            break
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day=input("\n Please selcet a day from the following:\n Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday ,All\n")
    day = str(day.strip().lower())
    while True:
        if day not in ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday" , "sunday", "all"):
            print("\n day Not found!!! ")
            sys.exit("Please restart the program... Exiting!!")
        else:
            print("\n Selected day is: '{}' ".format(day.title()))
            break
    print('-'*40)
    return city, month, day


# In[4]:


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
    df['Hour'] = df['Start Time'].dt.hour
    df['Month'] = df['Start Time'].dt.month
    df['Day'] = df['Start Time'].dt.day_name()
    
    if month != 'all':

        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['Month'] == month]

    if day != 'all':
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        df = df[df['Day'] == day.title()]
    
    return df


# In[5]:


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['Month'].mode()[0]
    print("\n Common Month : '{}' ".format(common_month))

    # display the most common day of week
    common_day = df['Day'].mode()[0]
    print("\n Common Day : '{}' ".format(common_day))
    
    # display the most common start hour
    common_hour = df['Hour'].mode()[0]
    print("\n Common Day : '{}' ".format(common_hour))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[6]:


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print("Commonly used start station was: '{}'".format(start_station))

    # display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print("Commonly used end station was: '{}'".format(end_station))

    # display most frequent combination of start station and end station trip
    df['Start_end_combine'] = (df['Start Station'] + ' - ' + df['End Station'])
    start_end_combination = str(df['Start_end_combine'].mode()[0])
    
    print("For the selected filters, the most common start-end combination "
          "of stations is: " + start_end_combination)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[7]:


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # display total travel time
    
    ######
    
    total_travel_time = df['Trip Duration'].sum()
    Mean_travel_time = df['Trip Duration'].mean()
    print(" \n The total trip duration is is '{}' \n ".format(total_travel_time))
    print("\n Average trip duration is '{}'\n ".format(Mean_travel_time))
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[8]:


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    count_user_type_count = df["User Type"].value_counts()
    print("\n Count of diffrent Users is '{}'\n ".format(count_user_type_count))

    # Display counts of gender
    if "Gender" in df.columns: 
        gender_count = df["Gender"].value_counts()

        print("\n Counts by Gender: '{}'".format(gender_count))
    else:
        print("\n 'Gender' does not exist in this dataset") 
    
    

    # Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        earliest = df['Birth Year'].min()
        most_recent = df['Birth Year'].max()
        most_common = df['Birth Year'].mode()[0]
        
        print("\n Earliest birth year: '{}'".format(earliest))
        print("\n Most recent birth year: '{}'".format(most_recent))
        print("\n Most common birth year: '{}'.".format(most_common))
    else:
        print("\n  'Year of Birth' not present in this dataset")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[9]:


def display_data(df):
    index=0
    user_input=input('would you like to display 5 rows of raw data? ').lower()
    while user_input in ['yes','y','yep','yea'] and index+5 < df.shape[0]:
        print(df.iloc[index:index+5])
        index += 5
        user_input = input('would you like to display more 5 rows of raw data? ').lower()


# In[10]:


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print(df.head())
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":main()


# In[ ]:





# In[ ]:




