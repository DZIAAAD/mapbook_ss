from mapbook.users import users
from mapbook.crud import hello,read_users

def main():
     hello(users[0]['Name'])
     read_users(users)

if __name__ == '__main__':
     main()
