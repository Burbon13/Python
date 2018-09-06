months = [31,28,31,30,31,30,31,31,30,31,30,31]

current_month = 1

starting_year = int(input())
days_to_proceed = int(input())

while days_to_proceed > 0:
    if(months[current_month-1] < days_to_proceed):
        days_to_proceed = days_to_proceed - months[current_month]
        current_month = current_month + 1
    else:
        break
    if current_month > 12:
        current_month = 1
        starting_year = starting_year + 1

print("Year %d Month %d Day %d" % (starting_year, current_month, days_to_proceed))

