from cryptography.fernet import Fernet
import os, sys
import glob
from colorama import Fore, Style, init
from PyPDF2 import PdfFileWriter, PdfFileReader

bb = Style.BRIGHT + Fore.BLUE
bw = Style.BRIGHT + Fore.WHITE
by = Style.BRIGHT + Fore.YELLOW
bg = Style.BRIGHT + Fore.GREEN
br = Style.BRIGHT + Fore.RED
g = Fore.GREEN
y = Fore.YELLOW
b = Fore.BLUE
w = Fore.WHITE
r = Fore.RED
d = Style.BRIGHT + Fore.BLUE + "[*]"
d2 = Style.BRIGHT + Fore.YELLOW + "[!]"
d3 = Style.BRIGHT + Fore.GREEN + "[*]"
d4 = Style.BRIGHT + Fore.RED + "[-]"

def decrypt():
    try:
        init(autoreset=True)
        print(d, bw + "Inicialiting Decryption...")
        key = sys.argv[2]
        os.chdir(sys.argv[1])
        print(d, bb + "Into on directory:", "{}".format(b + sys.argv[1]))
        cipher_suite = Fernet(key)

        print(d, bw + "Decrypting .txt files...")

        for files in glob.glob("*.txt"):
            with open(files, 'r') as arq:
                file = arq.read()
                if file.startswith("gAAAAA"):
                    print(d, bw + "Decrypting ", "{} ...".format(w + files))
                    plain_text = cipher_suite.decrypt(bytes(file.encode("utf-8"))).decode("utf-8")
                    with open(files, 'w') as file_decrypted:
                        file_decrypted.write(plain_text)
                else:
                    print(d2, "{}".format(y + files), by + "is not encrypted!")

        print(d, bw + "Decrypting .pdf files...")

        for fls in glob.glob("*.pdf"):
            arqs = PdfFileReader(open(fls, "rb"), strict=True)
            if arqs.isEncrypted:
                arqs.decrypt(password=key)
                print(d, bw + "Decrypting ", "{} ...".format(w + fls))
                path, filename = os.path.split(fls)
                output_file = os.path.join(path, "temp_" + filename)
                output = PdfFileWriter()
                for i in range(0, arqs.getNumPages()):
                    output.addPage(arqs.getPage(i))
                output_stream = open(output_file, "wb")
                output.write(output_stream)
                output_stream.close()
                os.rename(output_file, fls)
            else:
                print(d2, "{}".format(y + fls), by + "is not encrypted!")

        print(d3,  bg + "DECRYPTION COMPLETED!")
		sys.exit(0)
    except Exception as e:
        print(r + "[-] {}".format(e))
        print(d4, br + "ERROR when decrypt!")
        print(d, "Program finished.")
		sys.exit(2)

if __name__ == "__main__":
    decrypt()
