with open('/Users/vladimirmutaf/Documents/IT/files.txt', 'r', encoding='utf-8') as file:
    res = {}
    koef = {'B': 1, 'KB': 1024, 'MB': 1024*1024, 'GB': 1024*1024*1024}
    for row in file:
        name, sive, val = row.strip().split()
        _, r = name.split('.')
        res.setdefault(r, [[],[]])[0].append(int(sive) * koef[val])
        res[r][1].append(name)

    for k, v in sorted(res.items()):
        for i in sorted(v[1]):
            print(i)
        print('----------')
        sm = sum(v[0])
        if sm >= koef['GB']:
            vi = 'GB'
            sm = round(sm / koef['GB'])
        elif sm >=  koef['MB']:
            vi = 'MB'
            sm = round(sm / koef['MB'])
        elif sm >= koef['KB']:
            vi = 'KB'
            sm = round(sm / koef['KB'])
        else:
            vi = 'B'
            sm = round(sm / koef['MB'])

        print('Summary:', sm, vi)
        print()







