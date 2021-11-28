guests = ['mama','papa','brat','devushka']
invite = f"brat ne smojet priiti, poetomu prihodi na 14:00"
del_item = 'brat'
guests.remove(del_item)
guests.append('drug')
print(guests)
print(guests[0].title(), invite)
print(guests[1].title(), invite)
print(guests[2].title(), invite)
print(guests[3].title(), invite)
