import string

def orthmap(item):
    return ''.join([ str(seq_map[i]) for i in item ])

def lexsort(args):
    global seq_map, lc_letters
    lc_letters = list(string.ascii_lowercase)
    seq_map = { c: lc_letters[args[1].index(c)] for c in args[1] }
    return sorted(args[0], key=orthmap)

if __name__ == '__main__':
    
    test_cases = [
        { 'example': ( ["acb", "abc", "bca"], "abc"), 'output': ["abc","acb","bca"] },
        { 'example': (["acb", "abc", "bca"], "cba"), 'output': ["bca", "acb", "abc"]},
        { 'example': (["aaa","aa",""], "a"), 'output': ["", "aa", "aaa"] }
    ]

    for t in test_cases:
        hyp = lexsort(t['example'])
        ref = t['output']
        print ref, "\t", hyp
