import zlib, sys, time, base64, os

######   To compress a file   ######

with open("img.png", "rb") as in_file:
  compressed = zlib.compress(in_file.read(), 9)

with open("img_compressed_file", "wb") as out_file:
  out_file.write(compressed)

######   To descompress a file   ######

with open("flag.enc", "rb") as in_file:
  descompressed = zlib.decompress(in_file.read())

with open("flag_descompressed", "wb") as out_file:
  out_file.write(descompressed)

in_file.close()
out_file.close()
