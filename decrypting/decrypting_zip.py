from zipfile import ZipFile

zf = ZipFile("/home/boka/test3/aaa.zip")
pass_file = open("/home/boka/test3/dictionary.txt")

for line in pass_file.readlines():
  password = line.strip("\n")

  try:
    zf.extractall(pwd=password.encode("cp850", "replace"))
    print("\nPassword Found: {}\n".format(password))
    exit(0)
  except Exception as e:
    print("Searching... Bad password: {}".format(password))
    continue
