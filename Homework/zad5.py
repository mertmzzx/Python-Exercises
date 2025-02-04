input = input().split(", ")

tickets_sales = 0
count_tickets = 0
total_money = 0

for i in range(len(input)):
    tokens = input[i].split(" -> ")
    row = int(tokens[0])
    tickets = int(tokens[1])

    if row <= 3:
        tickets_sales += 1
        count_tickets += tickets
        total_money += tickets * 20
    else:
        tickets_sales += 1
        count_tickets += tickets
        total_money += tickets * 15

print(f"Sales: {tickets_sales}")
print(f"Theatre tickets sold {count_tickets}")
print(f"Total money: {total_money} lv")