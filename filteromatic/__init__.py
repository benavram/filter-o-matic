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
