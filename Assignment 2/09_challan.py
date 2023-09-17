# CHALLAN PROBLEM

speed = int(input("Enter the speed of vehicle: "))
is_today_birthday = int(input("Enter 1 if yes, otherwise 0\nIs today your birthday? "))

def caught(speed , is_today_birthday):
    if is_today_birthday == 0:
        if speed <= 60:
            print("No challan is imposed.")
        elif speed >60 and speed <=80:
            print("Small challan is imposed.")
        elif speed > 80:
            print("Heavy challan is imposed.")
    elif is_today_birthday == 1:
        if speed <=65:
            print("No challan is imposed.")
        elif speed >65 and speed <=85:
            print("Small challan is imposed.")
        elif speed >85:
            print("Heavy challan is imposed.")

caught(speed , is_today_birthday)
