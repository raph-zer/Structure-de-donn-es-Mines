words = []#list of all the words usable
f = open('frenchssaccent.dic','r')
for ligne in f :
         words.append(ligne[0:len(ligne)-1])
f.close()


#Question 1 : We look through the whole list of words and rule out any word not matching with the set of letters (instead of creating the words)
#Anytime a word fits the letters, we update the new longest word if the word is longer

#Question 2 :
def longest_word(letters, words):
    longest = letters[0]
    length = 1
    for word in words:
        longueur = len(list(word))
        test = True
        for letter in list(word):
            if letter not in letters:
                test = False
        if test == True and longueur > length:
            length = longueur
            longest = word
    return (longest,length)

longest_word(['a', 'r', 'b', 'g', 'e', 's', 'c', 'j'],words) #test

#Question 3 : The structure we're looking to use is that of a dictionary, because we need to link each letter to its set score
scores = dict([(letter,1) for letter in ['a','e','i','l','n','o','r','s','t','u']]+
[(letter,2) for letter in ['d','g','m']]+
[(letter,3) for letter in ['b','c','p']]+
[(letter,4) for letter in ['f','h','v']]+
[(letter,8) for letter in ['j','q']]+
[(letter,10) for letter in ['k','w','x','y','z']])
def score(word):#we simply add the values of the letters together
        s = 0
        for letter in word:
            s += scores[str(letter)]
        return s
    
def max_score(mots):#words rentrerait en conflit avec la liste des mots
    return max([(score(mot),mot) for mot in mots]) #it works because python first compares the first variable, and only the first if it's enough to pick a max (comparaison "paresseuse")

def most_points(letters, words):#we use the same idea as for Question1, but instead of comparing the lengths, we compare the scores (a particular type of length)
    top = score(letters[0])
    best = letters[0]
    for word in words:
        new_sco = score(word)
        test = True
        for letter in list(word):
            if letter not in letters:
                test = False
        if test == True and new_sco > top:
            top = new_sco
            best = word
    return (best,top)
most_points(['x','y','l','o','p','h','n','e'], words)


#Question4 : Je ne comprend pas ce qu'est sensé représenter l'exemple.
#Pour ce qui est de l'utilisation d'un joker, on suppose qu'il permet de former des mots à condition qu'une seule des lettres du mot ne soit pas dans la liste des lettres données.


def most_points_joker(letters, words):#similar to most_points, but we need to changer
    top = score(letters[0])
    best = letters[0]
    for word in words:
        joker = 1
        for letter in list(word):
            if letter not in letters:
                joker = letter
                joker_score = scores[letter] #we will need to remove the value of the letter used as a joker
                joker_count -= 1 #Joker keeps count of the letters out of the given set : can replace the old 'test'
        new_sco = score(word) - joker_score #'?' replaces the letter and is of score 0
        if joker_count >= 0 and new_sco > top: #only one joker can be used
            top = new_sco
            best = word
    return (best, top, joker) #to know which letter was used as a joker
