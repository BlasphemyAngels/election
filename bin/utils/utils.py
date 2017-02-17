# !/usr/bin/python3
# _*_coding: utf-8_*_
import zipfile
def unzipfile(filename, storedir):
    zfile = zipfile.ZipFile(filename, 'r')
    for fn in zfile.namelist():
        data = zfile.read(fn)
        with open(storedir + fn, 'wb') as f:
            f.write(data)
    return zfile
