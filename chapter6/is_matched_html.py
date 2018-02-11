from ArrayStack import ArrayStack

def is_matched_html(raw):
    S = ArrayStack()
    j = raw.find('<')
    while j != -1:
        k = raw.find('>', j+1)
        if k == -1:
            return False
        tag = raw[j+1:k]
        print(tag)
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