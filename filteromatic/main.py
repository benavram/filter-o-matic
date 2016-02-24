""" stuff
    asdfasd
"""
import re
import random
from .__init__ import PROFANITY, REPLACEMENTS
from .settings import WORD_REPLACE

TEXT = """Look, just because I don't be givin' no man a foot massage don't
make it right for Marsellus to throw Antwone into a glass motherfucking
house, fucking up the way the nigger talks. Motherfucker do that shit to
me, he better paralyze my ass, 'cause pass I'll kill the motherfucker,
know what I'm sayin'?"""

replacements = iter(REPLACEMENTS)
grawlix = ["$", "#", "@", "!", "*", "&", "%", "~", "}"]
grawlix_e = { "\\$", "\\#", "@", "!", "*", "\\&", "\\%" }

class Filter_o_matic(object):
    """  docstring

    """
    def __init__(self, eval_string):
        """
        eval_string:  dictionary, strings to be validated
        """
        # self.eval_list = eval_string.split()
        self.eval_string = eval_string
        p_expr = '(%s)' %'|\\b'.join(PROFANITY)
        self.re_profanity = re.compile(p_expr, re.I|re.M)
        

    def get_replacements(self, i):
        if WORD_REPLACE == 'grawlixes':
            n = random.randint(4,10)
            g_l = []
            for i in range(n):
                g = random.sample(grawlix, 1)
                g_l.append(g[0])
            glist = ''.join(g_l)
            return glist
        
        elif WORD_REPLACE == 'hashes':
            n = random.randint(4,10)
            h_l = []
            for i in range(n):
                h = '#'
                h_l.append(h)
            hlist = ''.join(h_l)
            return hlist
        
        elif WORD_REPLACE == 'exes':
            n = random.randint(4,10)
            x_l = []
            for i in range(n):
                x = 'X'
                x_l.append(x)
            xlist = ''.join(x_l)
            return xlist       

        else:
            random.shuffle(REPLACEMENTS)
            # r_word = random.sample(REPLACEMENTS, 1)
            return next(replacements)            

    def cleanit(self):
        # cleaned = [w.replace(str(item[0]), str(item[1])) for w in clean_list]
        replacement_string = "++==++==++"
        cleansed = self.re_profanity.sub(self.get_replacements,
                                         self.eval_string)

        return cleansed






