m = []
for i in r.scan_iter('profanity:*'):
    e = r.hscan(i)
    m.append(e[1]['word'.encode('utf-8')])