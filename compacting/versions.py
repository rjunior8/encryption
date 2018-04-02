import chilkat

z1 = chilkat.CkZip()
print("Zip: {}".format(z1.version()))

imap = chilkat.CkImap()
print("IMAP: {}".format(imap.version()))

ftp = chilkat.CkFtp2()
print("FTP: {}".format(ftp.version()))

mailman = chilkat.CkMailMan()
print("POP3/SMTP: {}".format(mailman.version()))

ssh = chilkat.CkSsh()
print("SSH: {}".format(ssh.version()))

sftp = chilkat.CkSFtp()
print("SFTP: {}".format(sftp.version()))

rsa = chilkat.CkRsa()
print("RSA: {}".format(rsa.version()))

http = chilkat.CkHttp()
print("HTTP: {}".format(http.version()))

crypt = chilkat.CkCrypt2()
print("Crypt: ".format(crypt.version()))

xml = chilkat.CkXml()
print("XML: {}".format(xml.version()))

sock = chilkat.CkSocket()
print("Socket/SSL/TLS: {}".format(sock.version()))

tar = chilkat.CkTar()
print("TAR: {}".format(tar.version()))