guests = ['mama','papa','brat','devushka']
del_item = 'brat'
guests.remove(del_item)
guests.append('drug')
info = f"ya kupil noviy stol, tak chto pridet ewe 3 moih druga"
print(info)
guests.insert(2, 'drug1')
guests.insert(0, 'drug2')
guests.append('drug3')
invite = f"prihodite na moi obed na 14:00"
print(guests)
print(guests[0], invite)
print(guests[1].title(), invite)
print(guests[2].title(), invite)
print(guests[3], invite)
print(guests[4].title(), invite)
print(guests[5], invite)
print(guests[6], invite)
print(guests)
guests.pop(0)
sry = f"izvini, u menya problemi i ne poluchitsya provesti obed, tak chto sorry"
print('drug2', sry)
guests.pop(2)
sry = f"izvini, u menya problemi i ne poluchitsya provesti obed, tak chto sorry"
print('drug1', sry)
guests.pop(2)
sry = f"izvini, u menya problemi i ne poluchitsya provesti obed, tak chto sorry"
print('devushka', sry)
guests.pop(2)
sry = f"izvini, u menya problemi i ne poluchitsya provesti obed, tak chto sorry"
print('drug', sry)
guests.pop(2)
sry = f"izvini, u menya problemi i ne poluchitsya provesti obed, tak chto sorry"
print('drug3', sry)
otvet1 = f"ya budu na obede P.S. {guests[0].title()}"
otvet2 = f"ya budu na obede P.S. {guests[1].title()}"
print(otvet1)
print(otvet2)
print(guests)
del guests[0]
del guests[0]
print(guests)
