#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""Does absolutely nothing useful but print garbage to standard output."""

from __future__ import print_function

import random

def make_rand_int_str(length):
    rand_int_str = ''.join(['{}'.format(random.randrange(10)) for x in
                            range(length)])
    return rand_int_str


while True:
    print(make_rand_int_str(80))

