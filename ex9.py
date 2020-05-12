import calendar
cal_display = calendar.TextCalendar(calendar.MONDAY)
# Year: 2019
# Column width: 1
# Lines per week: 1 
# Number of spaces between month columns: 0
# No. of months per column: 2
print(cal_display.formatyear(2019, 1, 1, 0, 1))