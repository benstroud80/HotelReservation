from datetime import datetime
import locale

print("The Hotel Reservation program\n")

again = "y"
while again.lower() == "y"
    # get arrival date
    while True:
        date_str = input("Enter arrival date (YYY-MM-DD): ")
        try:
            arrival_date = datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Try again.")
            print()
            continue # skip next if statement and re-start loop
