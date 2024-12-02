
def hello(users:str)->None:
    print (f'Witaj! {users}!!')

def read_users(users:list)->None:
    for user in users[1:]:
        print(f'Twój znajomy {user['Name']}, {user['city']}, opublikował {user['posts']} postów')

def add_user(users:list)->None:
    new_name:str=input('Proszę podać imię nowego znajomego: ')
    new_posts:int=int(input('Proszę podać liczbę postów: '))
    new_city:str=input('Proszę podać miasto nowego znajomego: ')
    new_user: dict = {'name': new_name, 'posts': new_posts, 'city': new_city}
    users.append(new_user)

def remove_user(users) -> None:
     user_to_find: str = input('Podaj imię do usunięcia: ')
     for user in users:
         if user['Name'] == user_to_find:
            print(f'usuwam: {user}')
            users.remove(user)