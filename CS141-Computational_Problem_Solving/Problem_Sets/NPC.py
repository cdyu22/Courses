from random import randint
class NPC (object):
    def __init__(self, name, phrases):
        self.__name = name
        self.__phrases = phrases#Your code here

    def add_phrase(self, phrase):
        self.phrases
        #your one line of code here to add a phrase to the phrases an NPC can say

    def getPhrases(self):
        return self.__phrases

    def speak(self):#Your code here, no more than 2 lines to select a phrase at random and
        n = random.randint()
#return it
    def __str__(self):
        return "Good day, I am " + self.__name

role = NPC('Guard', ['Greetings.','What can I do for you?','Knock it off!'])
role.add_phrase('Light bless you.')
print(role.speak())

#The output could be any one of the above four phrases
