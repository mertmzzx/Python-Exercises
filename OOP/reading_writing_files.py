def file_operations():
    try:
        with open("demofile.txt", "r") as f:
            txt = f.read()
        print(txt)

        with open("demofile.out.txt", "w") as fout:
             fout.write(txt+"\n")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)


def file_operations1():
    with open("demofile.txt", "r") as f:
        try:
            for line in f.readlines():
                print(line, end="")
        except Exception as e:
            print("An error occurred:", e)

file_operations1()