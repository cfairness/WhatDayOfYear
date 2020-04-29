# WhatDayOfYear
A python console app that asks the user to enter today's date, and returns the numbered day of the year.

Notes:

The main method of this application introduces the program to the user via console message, then prompts for date entry in mm/dd/yyyy format.
A TRY/EXCEPT statement and an IF/ELSE statement are used to check for valid user entries and re-prompt the user for another entry if validation fails. Failure can either be due to an exception (entering invalid characters that can't be converted to INTS) or due to entering valid characters but with a month count outside of the 1-12 range, etc.

After input is validated, it is passed to the function CalcDayNum, which employs the rules necessary to return the correct day number based on the day, month, and if this year is a leap year or not.

Python finishes by printing what number day it is for the user, and with an input prompt so that the window stays open until the user presses a key.
