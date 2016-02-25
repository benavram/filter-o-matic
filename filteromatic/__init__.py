# -*- coding: utf-8 -*-
"""Module Name - Module Purpose
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
from .settings import REDIS_CONN, WORD_REPLACE

PROFANITY = []
REPLACEMENTS = []
REPLACE_TYPE = WORD_REPLACE + ':*'

for key in REDIS_CONN.scan_iter('profanity:*'):
    p_item = REDIS_CONN.hscan(key)
    p_word = p_item[1]['word'.encode('utf-8')].decode('utf-8')
    PROFANITY.append(p_word)

if WORD_REPLACE == 'grawlixes':
    pass
elif WORD_REPLACE == 'hashes':
    pass
elif WORD_REPLACE == 'exes':
    pass
else:
    for key in REDIS_CONN.scan_iter(REPLACE_TYPE):
        r_item = REDIS_CONN.hscan(key)
        r_word = r_item[1]['word'.encode('utf-8')].decode('utf-8')
        REPLACEMENTS.append(r_word)
