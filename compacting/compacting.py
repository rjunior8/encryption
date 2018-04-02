import chilkat
import os

os.chdir("path/to/folder")

z1 = chilkat.CkZip()
z1.UnlockComponent("Anything for 30-day trial")
z1.NewZip("strong_encrypted.zip")
z1.put_Encryption(4)
z1.put_EncryptKeyLength(256)
z1.SetPassword("secret")
z1.AppendFiles("file.txt", True)
z1.WriteZip()
