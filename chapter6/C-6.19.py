"""
In Code Fragment 6.5 we assume that opening tags in HTML have form
<name>, as with <li>. More generally, HTML allows optional attributes
to be expressed as part of an opening tag. The general form used is
<name attribute1="value1" attribute2="value2">; for example,
a table can be given a border and additional padding by using an opening
tag of <table border="3" cellpadding="5">. Modify Code Fragment
6.5 so that it can properly match tags, even when an opening tag
may include one or more such attributes.
"""

from ArrayStack import ArrayStack

def check_atributes(data):
    print('checking for atr:', data)
    if len(data) == 0:
        return True
    for atr in data:
        if atr.find('=') < 0:

            return False
        name, value = atr.split('=')
        if not name[0].isalpha():
            return False
        if len(name) > 1 and not name[1:].isalnum():
            return False

        value = value[1:-1]
        if not value.isalnum():
            return False
        return True




def is_matched_html(raw):
    S = ArrayStack()
    j = raw.find('<')
    while j != -1:
        k = raw.find('>', j+1)
        if k == -1:
            return False
        tag = raw[j+1:k]
        many = tag.split(" ")
        if len(many) > 1:
            if not check_atributes(many[1:]):
                return False
            tag = many[0]

        if not tag.startswith('/'):
            # its opening tag
            S.push(tag)
        else:
            # its ending tag
            if S.is_empty():
                return False
            if tag[1:] != S.pop():
                return False
        j = raw.find('<', k+1)
    return S.is_empty()

x = open('test', 'r')
data = x.read()
# print(data)
print(is_matched_html(data))