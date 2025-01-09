import datetime as dt

def get_date() -> dt.datetime | None:
    date: dt.datetime | None = None

    while date is None:
        raw_date = input("Enter the date you want to travel to in the format YYYY-MM-DD: ").strip()

        if raw_date == "":
            print("[-] Date is required\n")
            continue
        
        try:
            parsed_date = dt.datetime.strptime(raw_date, "%Y-%m-%d")
            if parsed_date > dt.datetime.now():
                print("[-] Date must be in the past\n")
                continue
            date = parsed_date
        except ValueError:
            print("[-] Invalid date\n")
            continue

    return date