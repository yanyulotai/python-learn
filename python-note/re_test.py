# -*- coding: utf-8 -*-
import re

match = re.match(r'[1-9]\d{5}', '100081 BIT')
if match:
    print(match.group(0))

ls = re.findall(r'[1-9]\d{5}', 'BIT1234120 TSU4646')
print(ls)
