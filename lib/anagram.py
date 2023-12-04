# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, list_poss):
        orig_letters = []
        for letter in self.word :
            orig_letters.append(letter)
        #print(orig_letters)

        match_words = []
        for poss_word in list_poss:
            poss_word_letters = []
            for letter in poss_word:
                poss_word_letters.append(letter)
            if sorted(orig_letters) == sorted(poss_word_letters):
                match_words.append(poss_word)
        
        #print(match_words)
        return match_words

#Anagram("listen").match(["inlets", "goodbye", "hello"])