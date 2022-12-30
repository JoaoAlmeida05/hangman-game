from urllib.request import Request, urlopen
import random
import time

#here we are chosing the word for the algorithm
url="https://svnweb.freebsd.org/csrg/share/dict/words?revision=61569&view=co"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

web_byte = urlopen(req).read()

webpage = web_byte.decode('utf-8')
first500 = webpage.split("\n")
random.shuffle(first500)
word = random.choice(first500)
word = word.casefold()
wrong = []
wordLength = len(word)
new = list(word)

indicate = []
for i in range(wordLength):
    indicate += '_'


#start the visual 
def algthm(i):
    letter = input('Try a letter: ')
    
    letter.strip()
    
    
    # add the words to the part that is supposed to be if u answered correct or missed
    if not letter in new:
        i += 1
        wrong.append(letter) 
    else: # make it go to the part that is correct, the letter should appear where it is in the string.
        for a in range(word.count(letter)):
            place = new.index(letter)
            indicate[place] = letter
            new[place] = '.'

            

    time.sleep(.5)

    if i == 0:
        print("  ___________.._______ \n| .__________))______| \n| | / /      || \n| | | / \n| |/ \n| | \n| | | \n| | \n| | \n| | | \n| | \n| | \n| | | \n| | \n|=========|_`-' `-' |===| \n|=|=======\ \       '=|=| \n| |        \ \        | | \n: :         \ \       : : \n. .          `'       . . \n")
        print(indicate)
    elif i == 1:
        print(" ___________.._______ \n| .__________))______| \n| | / /      || \n| | | /        ||.-''. \n| |/         |/  _  \ \n| |          ||  `/,| \n| |          (\\`_.' \n| | | \n| | \n| | \n| | \n| | \n| | \n| | \n| | \n| | \n|=========|_`-' `-' |===| \n|=|=======\ \       '=|=| \n| |        \ \        | | \n: :         \ \       : : \n. .          `'       . . \n")
        print(indicate)
    elif i == 2:
        print(" ___________.._______ \n| .__________))______| \n| | / /      || \n| |/ /       || \n| | /        ||.-''. \n| |/         |/  _  \ \n| |          ||  `/,| \n| |          (\\`_.' \n| |         .-`--'. \n| |           . .    \n| |          |   |    \n| |          | . |     \n| |          |   |      \n| | \n| | \n| | \n| | \n| | \n|=========|_`-' `-' |===| \n|=|=======\ \       '=|=| \n| |        \ \        | | \n: :         \ \       : : \n. .          `'       . . \n")
        print(indicate)    
    elif i == 3:
        print("___________.._______ \n| .__________))______| \n| | / /      || \n| |/ /       || \n| | /        ||.-''. \n| |/         |/  _  \ \n| |          ||  `/,| \n| |          (\\`_.' \n| |         .-`--'. \n| |        /Y . .    \n| |       // |   |    \n| |      //  | . |     \n| |     ')   |   |      \n| | \n| | \n| | \n| | \n| | \n|=========|_`-' `-' |===| \n|=|=======\ \       '=|=| \n| |        \ \        | | \n: :         \ \       : : \n. .          `'       . . \n")
        print(indicate)    
    elif i == 4:
        print(" ___________.._______ \n| .__________))______| \n| | / /      || \n| |/ /       || \n| | /        ||.-''. \n| |/         |/  _  \ \n| |          ||  `/,| \n| |          (\\`_.' \n| |         .-`--'. \n| |        /Y . . Y\ \n| |       // |   | \\ \n| |      //  | . |  \\ \n| |     ')   |   |   (` \n| | \n| | \n| | \n| | \n| | \n|=========|_`-' `-' |===| \n|=|=======\ \       '=|=| \n| |        \ \        | | \n: :         \ \       : : \n. .          `'       . . \n")
        print(indicate) 
    elif i == 5:
        print(" ___________.._______ \n| .__________))______| \n| | / /      || \n| |/ /       || \n| | /        ||.-''. \n| |/         |/  _  \ \n| |          ||  `/,| \n| |          (\\`_.' \n| |         .-`--'. \n| |        /Y . . Y\ \n| |       // |   | \\ \n| |      //  | . |  \\ \n| |     ')   |   |   (` \n| |          ||    \n| |          ||    \n| |          ||    \n| |          ||    \n| |         / |    \n==========|_`-' `-' |===| \n|=|=======\ \       '=|=| \n| |        \ \        | | \n: :         \ \       : : \n. .          `'       . . \n")
        print(indicate) 
    elif i == 6:
        print(" ___________.._______ \n| .__________))______| \n| | / /      || \n| |/ /       || \n| | /        ||.-''. \n| |/         |/  _  \ \n| |          ||  `/,| \n| |          (\\`_.' \n| |         .-`--'. \n| |        /Y . . Y\ \n| |       // |   | \\ \n| |      //  | . |  \\ \n| |     ')   |   |   (` \n| |          || || \n| |          || || \n| |          || || \n| |          || || \n| |         / | | \\ \n==========|_`-' `-' |===| \n|=|=======\ \       '=|=| \n| |        \ \        | | \n: :         \ \       : : \n. .          `'       . . \n")
        print(indicate)    
        time.sleep(.5)
        print('/// YOU LOST... SECRET WORD: {WORD} ///'.format( WORD = word.upper()))

    print(word)
    
    time.sleep(1)
    if len(wrong) != 0:
        print('Wrong letters: ' + str(wrong))

    if indicate.count('_') == 0:
        print('/// CONGRATULATIONS... SECRET WORD: {WORD} ///'.format(WORD = word.upper()))
        i = 6

    if i != 6:
        algthm(i)
    
    
algthm(0)
