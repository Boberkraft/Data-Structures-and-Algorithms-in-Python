"""
Use recursion to write a Python function for determining if a string s has
more vowels than consonants.
"""
vovels = 'aeyiou'
consonats = 'bcdfghjklmnpqrstvwxyz'


def more_vovels(word, vo=0, cons=0):
    global vovels, consonats

    if len(word) > 0:
        # counts vovels and consonats on first
        if word[0] in vovels:
            vo += 1
        elif word[0] in consonats:
            cons += 1
        # check other
        return more_vovels(word[1:], vo, cons)
    return vo > cons

if __name__ == '__main__':
    word = 'adam'
    print(more_vovels(word))

