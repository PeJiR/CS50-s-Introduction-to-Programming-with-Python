list [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
#loop forever
while True:

#get user input
    date =input("Date: ")
    try:
        #split the date by /
        month,day,year = date.split()
        #check if month is between 1 and 12 and if day is between 1 and 31
        if (int(month)>= 1 and int(month)<= 12) and(int(day)>=1 and int(day) <=31):
            break

    except:
        try:
            #split the date by space
            old_month, old_day, year =date.split("")
            #find the number of the month
            for i in range [len(months)]:
                if old_month == months[1]:
                    month = i + 1
            #remove comma from my date
            day = old_date.replace(",","")
            #check if month is between 1 and 12 and if day is between 1 and 31
            if (int(month)>= 1 and int(month)<= 12) and (int(day)>=1 and int(day) <=31):
                break
        except:
            #to go to the next line
            print()
            pass

print(f"{year}-{int(month):02}{int(day):02}")

