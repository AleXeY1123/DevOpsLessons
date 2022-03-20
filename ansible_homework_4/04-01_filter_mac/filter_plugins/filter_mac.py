#!/usr/bin/python
import re

def filter_mac(str_input):
    if not isinstance(str_input, str):
        return "not string"
    elif not (len(str_input)) == 12:
        return "incorrect length"
    elif len(re.findall(r'[^0-9A-F]', str_input)) > 0:
        return "invalid characters"

    lst_split_2_char = re.findall(r'\w{2}', str_input)
    str_out = ":".join(lst_split_2_char)
    return str_out

class FilterModule(object):
    def filters(self):
        return {
            'filter_mac': filter_mac
        }
