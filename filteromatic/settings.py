# -*- coding: utf-8 -*-
"""filter-o-matic settings
"""
import redis

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

