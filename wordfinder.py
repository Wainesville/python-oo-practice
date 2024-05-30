"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    ...
    """
    wf = WordFinder('simple.txt')
    5 words read

    wf = random()
    return random word from file
    """





    def __init__(self,path):
        """return number of Items read"""
        dict_file = open(path)

        self.words = self.parse(dict_file)

        print(f"{len(self.words)} words read")

    def parse(self, dict_file):

        return [w.strip() for w in dict_file]
    
    def random(self):
        """return random word"""
        return random.choice(self.words)
    


    
class SpecialWordFinder(WordFinder):

    """ Word finder that skips blank lines and comments

    spw = SpecialWordFinder('specialwords.txt')
    6 words read
    
    spw.random() in ["lion","tiger","tree"]

    TRUE
    """

    def parse(self, dict_file):

        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith('#')]