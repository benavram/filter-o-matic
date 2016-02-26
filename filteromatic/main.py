# -*- coding: utf-8 -*-
"""filter-o-matic evaluation and filter
    Copyright (c) 2016 office(ish).com

    https://github.com/benavram/filter-o-matic

    This file is part of filter-o-matic.

    filter-o-matic is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Foobar is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with [app name].  If not, see <http://www.gnu.org/licenses/> or
    <https://github.com/benavram/filter-o-matic/blob/master/LICENSE>

  # Configuration variables

API docs at https://github.com/benavram/filter-o-matic
# Authors:

"""
import re
import random
from .__init__ import PROFANITY, REPLACEMENTS
from .settings import WORD_REPLACE

TEXT = """Look, just because I don't be giving no man a foot massage don't
make it right for Marsellus to throw Antwone into a glass motherfucking
house, fucking up the way the nigger talks. Motherfucker do that shit to
me, he better paralyze my ass, 'cause pass I'll kill the motherfucker,
know what I'm sayin?"""

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
        if self.rep_scheme is not None:
            WORD_REPLACE = self.rep_scheme
        if WORD_REPLACE == 'grawlixes':
            n = random.randint(4,10)
            print('this is a test')
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

    def cleanit(self, reps=None):
        self.rep_scheme = reps
        cleansed = self.re_profanity.sub(self.get_replacements,
                                         self.eval_string)
        return cleansed






