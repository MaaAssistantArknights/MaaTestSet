
#! /usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
from importlib.resources import path
import os


def de(working_dir):
    md5_set = set()
    for client_name in os.listdir(working_dir):
        client_dir = working_dir + client_name + '/'
        for file_name in os.listdir(client_dir):
            filepath = client_dir + file_name
            with open(filepath, 'rb') as fp:
                data = fp.read()
            file_md5 = hashlib.md5(data).hexdigest()
            if file_md5 in md5_set:
                print('Duplicate found: {}'.format(filepath))
                os.remove(filepath)
            else:
                md5_set.add(file_md5)


de('./drops/screenshots/')
de('./depot/screenshots/')
