with open("text_file.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line)
    file.close()