from zipfile import ZipFile, ZIP_STORED
import pyminizip
import os
import sys
import glob
import getpass

global zip_file
global zip_archive

try:
    if len(sys.argv) != 6:
        print("Usage: python3 compactor.py --path [path] -out [filename] -p")
        sys.exit()
    elif sys.argv[1] == "--path" and sys.argv[3] == "-out" and sys.argv[5] == "-p":
        os.chdir(sys.argv[2])
        zip_file = "{}.zip".format(sys.argv[4])
        zip_archive = ZipFile(zip_file, mode='w', compression=ZIP_STORED, allowZip64=True)

        for file in glob.glob('*'):
            if not os.path.splitext(file)[1] == ".zip":
                zip_archive.write(file)

        zip_archive.close()

        pyminizip.compress_multiple(zip_archive.namelist(), zip_file,
                                    "{}".format(getpass.getpass(prompt="Password: ", stream=None)), 5)

        for arq in glob.glob('*'):
            if not os.path.splitext(arq)[1] == ".zip":
                os.remove(arq)
    else:
        print("Usage: python3 compactor.py --path [path] -out [filename] -p")
        sys.exit()
except Exception as e:
    print(e)