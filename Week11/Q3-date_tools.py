import datetime
import calendar
import jdatetime


class Date_tools:
    def __init__(self, first_date, second_date):
        self.first_date = first_date
        self.second_date = second_date


    def time_difference_in_seconds(self):
        time_difference = (self.second_date - self.first_date).total_seconds()
        print(f"time difference in seconds: {time_difference}")


    def number_of_leap_years(self):
        count = 0
        for year in range(self.first_date.year, self.second_date.year + 1):
            if calendar.isleap(year):
                count += 1
        print(f"number of leap years: {count}")


    def number_of_daylight_saving(self):
        pass


    def convert_to_jalali(self):
        j_first_date = jdatetime.datetime.fromgregorian(datetime=self.first_date)
        j_second_date = jdatetime.datetime.fromgregorian(datetime=self.second_date)
        print(f"first date in Hijri: {j_first_date}")
        print(f"second date in Hijri: {j_second_date}")



def main():
    first_date = input("Enter first date and time in this format: 'year-month-day Hour:Minute:Second': ")
    second_date = input("Enter second date and time in this format: 'year-month-day Hour:Minute:Second': ")

    first_date = datetime.datetime.strptime(first_date, '%Y-%m-%d %H:%M:%S')
    second_date = datetime.datetime.strptime(second_date, '%Y-%m-%d %H:%M:%S')

    two_times = Date_tools(first_date, second_date)
    two_times.time_difference_in_seconds()
    two_times.number_of_leap_years()
    two_times.convert_to_jalali()

if __name__ == "__main__":
    main()


# 1997-01-10 12:10:07
# 2023-06-20 11:20:25
