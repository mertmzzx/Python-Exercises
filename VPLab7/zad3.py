with open("document.bin", "wb") as binary_file:
    data = "This is good"
    binary_file.write(data.encode("ascii"))
    binary_file.close()