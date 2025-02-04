try:
    fileName = input()

    f = open(fileName)
    text = f.read()
    print(text)
except:
    print("Error!")

