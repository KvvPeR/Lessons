games = ['civilization','valorant','rocket league','cs','dota']
print('Весь список игр', games)
item = f"Покажите мне список без игры {games[1].title()}"
print(item)
del_item = 'valorant'
games.remove(del_item)
print(games)
print(del_item)
item1 = f"Покажите мне список без игры {games[1].title()}"
print(item1)
del_item1 = 'cs'
games.remove(del_item1)
print(games)
print(del_item1)                       