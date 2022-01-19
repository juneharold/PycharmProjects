user_num = int(input("type in a number>"))

if user_num % 2 == 0 and user_num>100:
    print("even and very large")
elif user_num % 2 == 0:
    print("even")
else:
    print("odd")


