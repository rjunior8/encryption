from zipfile import ZipFile

zf = ZipFile("file.zip")
pass_file = open("dictionary.txt")

attempts = 0

for line in pass_file.readlines():
    password = line.strip("\n")

    try:
        zf.extractall(pwd=password.encode("cp850", "replace"))
        print("Password Found: {}\n".format(password))
        exit(0)
    except Exception as e:
        attempts += 1
        print("Searching... {} {}".format(attempts, e))
        pass
