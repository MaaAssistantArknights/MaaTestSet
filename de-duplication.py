
#! /usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
from importlib.resources import path
import os


def de(working_dir):
    md5_set = set()
    for file_name in os.listdir(working_dir):
        with open(working_dir + file_name, 'rb') as fp:
            data = fp.read()
        file_md5 = hashlib.md5(data).hexdigest()
        if file_md5 in md5_set:
            print('Duplicate found: {}'.format(file_name))
            os.remove(working_dir + file_name)
        else:
            md5_set.add(file_md5)


de('./drops/screenshots/')
de('./depot/screenshots/')
