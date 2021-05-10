import random
ABCLXC = 'abcdefghijklmnopqrstuvwxyz'
BRAILLELXC = '⠁⠃⠉⠙⠑⠋⠛⠓⠊⠚⠅⠇⠍⠝⠕⠏⠟⠗⠎⠞⠥⠧⠺⠭⠽⠵'
BRAILLEKEY = dict(zip(ABCLXC, BRAILLELXC))
ABCKEY = dict(zip(BRAILLELXC, ABCLXC))
MAXLEN = 10
MINLEN = 3
ALLOWED = 'abcdefghij'

def abctobraille(src):
    return ''.join(BRAILLEKEY[c] if c in ABCLXC else c for c in src)

def readwords():
    with open('words','r') as f:
        raw = f.read()
    words = list(filter(lambda s: MINLEN <= len(s) <= MAXLEN and all(c in ALLOWED for c in s), raw.split('\n')))
    return words

def main():
    words = readwords()
    while True:
        i = random.randint(0,len(words)-1)
        word = words[i]
        wbraille = abctobraille(word)
        for i in range(3):
            print(f'?> {wbraille}')
            response = input('-> ')
            if response == word:
                print('Correct! -----------------------------------------\n')
                break
            if response == '':
                print(word)
                return
            print('x> Try again.')
        else:
            print(f'Wrong. The word was\n  {wbraille}\n  {word}')
            print(    'X X X X X X X X X X X X X X X X X X X X X X X X X \n')

if __name__ == '__main__':
    main()
