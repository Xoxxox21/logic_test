#!/bin/python3

import math
import os
import random
import re
import sys

def perform(n):
    if n %2!= 0:
        return print('Weird')
    elif 2 <= n <= 5:
        return print('Not Weird')
    elif 6 <= n <= 20:
        return print('Weird')
    elif n > 20:
        return print('Not Weird')
y = int(input(''))
perform(y)