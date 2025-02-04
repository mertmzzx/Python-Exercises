from urllib.parse import DefragResult

floors = int(input())

for i in range(floors):
    data = input()
    lData = data.split(" ")
    dressingRooms = lData[0].count("#")
    busyClients = int(lData[1])
    waitingClients = int(lData[2])



    print(f"Етаж №{i + 1}:")
    if dressingRooms > (busyClients + waitingClients):
        print(f"Има {dressingRooms - (busyClients + waitingClients)} свободни пробни")
    elif busyClients + waitingClients == dressingRooms:
        print("Всички пробни са заети")
    elif busyClients + waitingClients > dressingRooms:
        print(f"Има {(busyClients + waitingClients) - dressingRooms} чакащи клиенти за пробни")


