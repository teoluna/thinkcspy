year = int(input("Please enter the year (from 1900 to 2099)."))

if year >= 1900 and year <= 2099:
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19*a + 24) % 30
    e = (2*b + 4*c + 6*d + 5) % 7
    dateofeaster = 22 + d + e
      
    if year == 1954 or year == 1981 or year == 2049 or year == 2076:
        dateofeaster = dateofeaster - 7
        
    if dateofeaster > 31:
        print("April", dateofeaster - 31)
    if dateofeaster < 31:
        print("March", dateofeaster)
else:
    print("Error. Please enter a valid year.")