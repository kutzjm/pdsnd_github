import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    input_city=[]
    while input_city not in ('chicago','new york city','washington','Chicago','New York City','Washington','all','All'):
        input_city=input('For which city would you like to receive bikeshare data? Chicago, New York City, or Washington?: ').lower()
        city=input_city

        
    # TO DO: get user input for month (all, january, february, ... , june)
    input_month=[]
    while input_month not in ('january','february','march','april','may','june','july','august','september','october','november','december','January','February','March','April','May','June','July','August','September','October','November','December', 'all', 'All'):
        input_month=input('If you do not want to filter by month, enter all. If you want to filter by month, enter a month: ').lower()
        month=input_month

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    weekdays = ['monday','tuesday','wednesday','thursday','friday','all']
    daycheck = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
    day=input('If you do not want to filter by day, enter all. If you want to filter by day, enter a day of the week: ')
    day=day.lower()
    if day in weekdays:
        print('Input received. Data will be shown for ',city.title(),'\n','And within',month,'month(s)','and on',day,'day(s) of the week.')
    elif day in daycheck:
        print('Please type the name of the day of the week rather than a number. Enter the word all if you do not want to filter by day.\n')
        day=input('Enter day of the week: ')
    else:
        print('Please type the full name of the day of the week.\n')
        day=input('Enter day of the week: ')
        


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
    city=city
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        # gets the integers from the months
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    #filter by month
        df = df[df['month'] == month]
    #filter by day
    if day != 'all':
        df = df[df['day_of_week']==day.title()]
    else:
        print('No selected day')
    

    #df = load_data(city,month,day)
    return df
 

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    print('\n(These will simply display the month and day entered according to your choice to filter by month and/or day.)\n')
    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    month_mode = months[df['month'].mode()[0]-1].title()
    print('Most Frequent Month:', month_mode)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Frequent Day:', popular_day) 

    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    
    popular_hour = df['hour'].mode()[0]
    print('Most Frequent Start Hour:', popular_hour)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Top_Start_Station = df['Start Station'].value_counts(sort=True).head(1)
    Start_Station_Frequency =df['Start Station'].value_counts(normalize=True).head(1)
    
    print('Most Popular Start Station and Count:\n',Top_Start_Station)
    print('\nFrequency Rate:\n',Start_Station_Frequency)


    # TO DO: display most commonly used end station
    Top_End_Station = df['End Station'].value_counts(sort=True).head(1)
    End_Station_Frequency =df['End Station'].value_counts(normalize=True).head(1)
    
    print('\nMost Popular End Station and Count:\n',Top_End_Station)
    print('\nFrequency Rate:\n',End_Station_Frequency)

    # TO DO: display most frequent combination of start station and end station trip
    print('Top Combination:')
    grouped = df.groupby(['Start Station'])['End Station'].value_counts().idxmax()
    print(grouped)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print('Total travel time: ',total_travel,' seconds.')

    # TO DO: display mean travel time
    travel_mean_time = df['Trip Duration'].mean()
    travel_max = df['Trip Duration'].max()
    travel_min = df['Trip Duration'].min()
    print('The mean duration of travel was ',travel_mean_time,' seconds, while the longest trip took ', travel_max,' seconds and the shortest trip took ',travel_min,' seconds.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types=df['User Type'].value_counts()
    print('Total types of users shown below;\n', user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_counts=df['Gender'].value_counts()
        print('\nGender totals shown below;\n', gender_counts)
    else:
        print('Washington does not have gender data.')

    # TO DO: Display earliest, most recent, and most common year of birth
    #birthyr_mode=df['Birth Year'].value_counts().head(1)
    if 'Birth Year' in df.columns:
        birthyr_mode=df['Birth Year'].value_counts().idxmax()
        print('\n',int(birthyr_mode),' is the most common birth year of users.')
    else:
        print('Washington does not have birth year data.')

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

#display_data
        row_count=0
        raw_input=input('Do you want to see raw data?: ')
        if raw_input in ('yes','y', 'Yes','YES'):
            row_count=5
            raw_lines=pd.read_csv(CITY_DATA[city], nrows=row_count)
            print(raw_lines)
        while raw_input not in ('no', 'n', 'No', 'NO'):
            raw_input=input('Do you want to see 5 more lines of raw data?: ')
            raw_lines = pd.read_csv(CITY_DATA[city]).iloc[row_count:row_count+5]
            print(raw_lines)
            row_count+=5
        else:
            print('Okay, no raw data will be shown unless you restart.')
    
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
