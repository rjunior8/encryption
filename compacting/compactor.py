from zipfile import ZipFile, ZIP_STORED
import pyminizip
import os
import sys
import glob
import getpass
import argparse

global zip_file
global zip_archive

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True, help="Folder to be encrypt")
ap.add_argument("-o", "--output", required=True, help="File name as output")
ap.add_argument("-p", "--passwd", help="Define a password [You'll to be prompted]", action="store_false")
args = vars(ap.parse_args())

try:
  if len(sys.argv) != 6:
    ap.print_help()
    sys.exit(2)
  elif not args["input"] is None and not args["output"] is None and not args["passwd"] is None:
    os.chdir(sys.argv[2])
    zip_file = "{}.zip".format(sys.argv[4])
    zip_archive = ZipFile(zip_file, mode='w', compression=ZIP_STORED, allowZip64=True)

    for file in glob.glob('*'):
      if not os.path.splitext(file)[1] == ".zip":
        zip_archive.write(file)

    zip_archive.close()

    pyminizip.compress_multiple([item for item in zip_archive.namelist()], [os.path.abspath(args["input"])], zip_file, "{}".format(getpass.getpass(prompt="Password: ", stream=None)), 5)

    for arq in glob.glob('*'):
      if not os.path.splitext(arq)[1] == ".zip":
        os.remove(arq)
  else:
    ap.print_help()
    sys.exit(2)
except argparse.ArgumentError as exc:
  print(exc.message, "\n", exc.argument)
except Exception as e:
  print("\n{}\nError on line: {}\n".format(e, sys.exc_info()[-1].tb_lineno))
  sys.exit(2)


