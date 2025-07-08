cid = str(input('Cidade: ')).strip()
cid1 = cid.title()
cidspl = cid1.split()
cid2 = 'Santo' in cidspl[0]
print(cid2)