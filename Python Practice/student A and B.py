a, b, c = input("A학생 국영수 점수>"). split()

d = int(a)
e = int(b)
f = int(c)

g = (d+e+f)/3

if g == 100:
    print("A학생은 A등급")
elif g >= 90:
    print("A학생은 B등급")
elif g >= 80:
    print("A학생은 C등급")
elif g >= 70:
    print("A학생은 D등급")
elif g >= 60:
    print("A학생은 E등급")
else:
    print("A학생은 F등급")

h, i, j = input("B학생 국영수 점수>"). split()

k = int(h)
l = int(i)
m = int(j)

o = (k+l+m)/3

if o == 100:
    print("B학생은 A등급")
elif o >= 90:
    print("B학생은 B등급")
elif o >= 80:
    print("B학생은 C등급")
elif o >= 70:
    print("B학생은 D등급")
elif o >= 60:
    print("B학생은 E등급")
else:
    print("B학생은 F등급")

print()

if g == o:
    print("동급입니다")
elif g >= o:
    print("A가 더 높음")
else:
    print("B가 더 높음")




