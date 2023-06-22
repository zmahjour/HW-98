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
        j_first_date = jdatetime.datetime.fromgregorian(datetime=self.first_date.date())
        j_second_date = jdatetime.datetime.fromgregorian(datetime=self.second_date.date())
        d_s = (j_second_date.year - j_first_date.year - 1) * 2

        if j_first_date.month < 7:
            d_s += 1
        if j_second_date.month > 6:
            d_s += 2
        else:
            d_s += 1

        print(f"number of daylight saving: {d_s}")


    def convert_to_jalali(self):
        j_first_date = jdatetime.datetime.fromgregorian(datetime=self.first_date.date())
        j_second_date = jdatetime.datetime.fromgregorian(datetime=self.second_date.date())
        print(f"first date in Jalali: {j_first_date.strftime('%Y/%m/%d')}")
        print(f"second date in Jalali: {j_second_date.strftime('%Y/%m/%d')}")



def main():
    first_date = input("Enter first date and time in this format: 'year-month-day Hour:Minute:Second': ")
    second_date = input("Enter second date and time in this format: 'year-month-day Hour:Minute:Second': ")

    first_date = datetime.datetime.strptime(first_date, '%Y-%m-%d %H:%M:%S')
    second_date = datetime.datetime.strptime(second_date, '%Y-%m-%d %H:%M:%S')

    two_times = Date_tools(first_date, second_date)
    two_times.time_difference_in_seconds()
    two_times.number_of_leap_years()
    two_times.number_of_daylight_saving()
    two_times.convert_to_jalali()

if __name__ == "__main__":
    main()


# for test: 1997-01-9 4:10:07 | 2023-06-20 11:20:25
