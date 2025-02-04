input = input()

text = list(input)
d = {}
for i in range(len(text)):
    d[text[i]] = text.count(text[i])

dKeys = list(d.keys())
dKeys.sort()

for key in dKeys:
    print("{0}:{1}".format(key, d[key]), end=" ")