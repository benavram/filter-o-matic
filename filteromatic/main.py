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
from .settings import WORD_REPLACE  # pylint: disable = W0611


TEXT = """Look, just because I don't be giving no man a foot massage don't
make it right for Marsellus to throw Antwone into a glass motherfucking
house, fucking up the way the nigger talks. Motherfucker do that shit to
me, he better paralyze my ass, 'cause pass I'll kill the motherfucker,
know what I'm sayin?"""

replacements = iter(REPLACEMENTS)
grawlix = ["$", "#", "@", "!", "*", "&", "%", "~", "}"]
font_awesome_icons = '_fom_item'
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

    def get_replacements(self, i): # pylint: disable = R0914, W0613
        if  self.rep_scheme == 'grawlixes':
            n = random.randint(4, 10)
            g_l = []
            for i in range(n):
                g = random.sample(grawlix, 1)
                g_l.append(g[0])
            glist = ''.join(g_l)
            return glist
        
        elif  self.rep_scheme == 'font_awesome':
            fa_l = []
            f = font_awesome_icons
            fa_l.append(f)
            falist = ''.join(fa_l)
            return falist
        elif  self.rep_scheme == 'hashes':
            n = random.randint(4, 10)
            h_l = []
            for i in range(n):
                h = '#'
                h_l.append(h)
            hlist = ''.join(h_l)
            return hlist
        elif  self.rep_scheme == 'exes':
            n = random.randint(4, 10)
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
        if reps is None:
            self.rep_scheme = 'hashes'
        else:
            self.rep_scheme = reps
            
        cleansed = self.re_profanity.sub(self.get_replacements,
                                         self.eval_string)
        return cleansed
