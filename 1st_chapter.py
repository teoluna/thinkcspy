# question 4 solution

starting_day = int(input("What is the number of the day in a week that you're leaving? (if Sunday is 0)"))
length_of_stay = int(input("How long are you staying? (in days)"))

return_on = (starting_day + length_of_stay) % 7

print("You will return on day", return_on)