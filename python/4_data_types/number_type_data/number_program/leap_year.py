# Every four years, we add an extra day, February 29, to our calendars. These extra days – called leap days
#
class LeapYear:

    def find_leap_year(self):

        year= int (input("Enter year"))

        if year % 4 ==0:
            if year % 100 ==0:
                if year % 400 ==0:
                    print("{0} is a leap year".format(year))
            else:
                print("{0} is a leap year".format(year))
        else:
            print("{0} is not a leap year".format(year))


obj = LeapYear()
obj.find_leap_year()