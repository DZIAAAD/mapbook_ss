from mapbook.users import users
from mapbook.crud import hello,read_users,add_user

def main():
     hello(users[0]['Name'])
     read_users(users)
     add_user(users)

if __name__ == '__main__':
     main()
