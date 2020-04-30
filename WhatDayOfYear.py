

def calcDayNum(month, day, year):  # function to calculate the day number
    dayNum = 31 * (month - 1) + day  # step 1 of day calc formula
    if (month > 2):  # check if month is after Feb and perform extra step if so
        dayNum = dayNum - ((4 * month + 23) // 10)
    if (year % 4 == 0) and (month > 2):  # check if month after Feb 29 and year divisible by 4, if so check for leap yr
        if (year % 400 == 0):  # if year is divisible by 400, it's a leap year
            dayNum = dayNum + 1
        elif (year % 4 == 0) and (year % 100 != 0):  # if year is divisible by 4 but not divisible by 100, also leap year
            dayNum = dayNum + 1
    return dayNum  # return the day number


def leapYear(year):  # Define function for determining if year is a leap year
    # If year is divisible by 4
    if year % 4 == 0:  # If year is divisible by 100
        if year % 100 == 0:  # If year is divisible by 400
            if year % 400 == 0:  # Return True. Year is a leap year.
                return True  # If year is not divisible by 400
            else:  # Return False. Year is not a leap year.
                return False  # If year is not divisible by 100
        else:  # Return True. Year is a leap year.
            return True  # If year is not divisible by 4
    else:  # Return False. Year is not a leap year.
        return False


def main():  # begin main method
    print("This program computes the sequential day of the year.")  # states purpose of this program

    dateValid = False  # initiate dateValid variable as false for while loop

    while dateValid == False:
        userDate = input("Enter the date to calculate (mm/dd/yyyy): ")  # gets user input for date value
        try:
            monthStr, dayStr, yearStr = userDate.split("/")  # try converting userDate to split ints
            monthStr, dayStr, yearStr = int(monthStr), int(dayStr), int(yearStr)
        except ValueError:
            monthStr, dayStr, yearStr = 0, 0, 0  # if it fails on doing that, set all three to zero so loop can repeat
        if (0 < monthStr <= 12) and (0 < dayStr <= 31) and (0 < yearStr < 9999):  # check that all three nums are usable
                if ((monthStr == 2) and (leapYear(yearStr) == False) and (dayStr > 28)):
                    print("Not a valid date.")  # check that feb can't have 29 days using LeapYear function
                elif (monthStr == 4 or monthStr == 6 or monthStr == 9 or monthStr == 11) and (dayStr > 30):
                    print("Not a valid date.")  # check that 4,6,9,11 can't have 31 days
                else:
                    dateValid = True  # set dateValid to true if all three are usable so loop can exit
        else:  # inform user that date entry was invalid and loop continues until valid entry is made
            print("Not a valid date.")

    print("Today is day", calcDayNum(monthStr, dayStr, yearStr), "of the year", yearStr)  # prints what day of the year it is

    input("Press any key to exit.")  # user prompt so the program stays open


main()  # end main method
