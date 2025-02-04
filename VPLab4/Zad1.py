n = int(input())

underage = list()
eligible = list()

for i in range(n):
    age = int(input())

    if age == 0:
        underage.append(age)
    elif age < 18:
        underage.append(age)
    elif age >= 18:
        eligible.append(age)

countAdults = len(eligible)
countChildren = len(underage)
avg = sum(eligible) / countAdults
print(f"Count of children: {countChildren}")
print(f"Count of adults: {countAdults}")
print(f"Average age of adults: {int(avg)}")