
def hello(users:str)->None:
    print (f'Witaj! {users}!!')

def read_users(users:list)->None:
    for user in users[1:]:
        print(f'Twój znajomy {user['Name']}, {user['city']}, opublikował {user['posts']} postów')