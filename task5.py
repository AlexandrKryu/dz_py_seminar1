quarter = int(input("введите номер четверти: "))

if quarter == 1:
    print("X > 0 ; Y > 0")
elif quarter == 2:
    print("X < 0 ; Y > 0")
elif quarter == 3:
    print("X < 0 ; Y < 0")
elif quarter == 4:
    print("X > 0 ; Y < 0")
else:
    print("для 2х координат не подходит")
