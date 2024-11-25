users: list = [
    {'name': 'Szymon z wąsem', 'posts': 1, 'city': 'Warszawa'},
    {'name': 'Dominik', 'posts': 3, 'city': 'Poznań'},
    {'name': 'Patrycja', 'posts': 5, 'city': 'Toruń'},
    {'name': 'Szymon', 'posts': 7, 'city': 'Łódź'},
    {'name': 'Patryk', 'posts': 9, 'city': 'Kielce'},
    {'name': 'Żerom', 'posts': 11, 'city': 'Radom'},
    {'name': 'Michał', 'posts': 13, 'city': 'Olsztyn'},
    {'name': 'Dominik aka bax', 'posts': 15, 'city': 'Białystok'},
    {'name': 'Kinga', 'posts': 17, 'city': 'Opole'},
    {'name': 'Amelia', 'posts': 19, 'city': 'Wrocław'},

]

print(f'Witaj {users[0]['name']}!!')
for user in users[1:]:
     print(f'Twój znajomy {user['name']}, z miasta {user['city']}, opublikował {user['posts']} postów')
# for idx, _ in enumerate(users[1:]):
#     print(f'Twój znajomy {users[idx]}, opublikował {postow[idx]} postów')
