# -*- coding: utf-8 -*-
"""filter-o-matic settings
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
import redis

app_name = 'filter-o-matic',
licensed = """
        licensed in accordance with terms of the GNU General Public
        License
        """
lic_loc = 'https://github.com/benavram/filter-o-matic/blob/master/LICENSE'
docs = 'https://github.com/benavram/filter-o-matic'
copy_r = '2016 office(ish).com'

REDIS_CONN = redis.Redis(host="localhost", port=20888, db=1)

S = 0
O = 1
G = 2
H = 3
X = 4

REPLACE_CHOICES = (
    ('S', 'silly'),
    ('O', 'onomatopoeia'),
    ('G', 'grawlixes'),
    ('H', 'hashes'),
    ('X', 'exes')
    )

WORD_REPLACE = REPLACE_CHOICES[S][1]

