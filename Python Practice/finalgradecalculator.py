a, b, c, d, e = input("score>").split()

f = int(a)
g = int(b)
h = int(c)
i = int(d)
j = int(e)

k = (f+g+h+i+j)/5

if k > 99:
    print("A등급")
elif k >= 90:
    print("B등급")
elif k >= 80:
    print("C등급")
elif k >= 70:
    print("D등급")
elif k >= 60:
    print("E등급")
else:
    print("F등급")
