# -*- coding: utf-8 -*-
"""filter-o-matic utility functions
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
from .settings import REDIS_CONN

def word_lists(list_type):
    """word lists from db
    """
    return_list = []
    f_str = list_type + ':*'
    for key in REDIS_CONN.scan_iter(f_str):
        list_content = REDIS_CONN.hscan(key)
        list_category = list_content[1]['list_cat'.encode("utf-8")]
        word = list_content[1]['word'.encode("utf-8")]
        rating = list_content[1]['rating'.encode("utf-8")]
        wordtype = list_content[1]['word_type'.encode("utf-8")]
        tmp_lst = (wordtype.decode("utf-8"),
                   word.decode("utf-8"),
                   rating.decode("utf-8"),
                   list_category.decode("utf-8")
                   )
        return_list.append(tmp_lst)
    return return_list


def word_check(word):
    """check word against profanity list and return True if exists
    word: string
    """
    l = []
    
    for key in REDIS_CONN.scan_iter('profanity:*'):
        item = REDIS_CONN.hscan(key)
        mystr = word
        w = item[1]['word'.encode('utf-8')].decode('utf-8')
        l.append(w)

    if mystr in l:
        return True
    else:
        return False
