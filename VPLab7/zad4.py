with open("document.bin", "rb") as binary_file:
    data = binary_file.read(4)
    decoded_data = data.decode("ascii")
    print(decoded_data)