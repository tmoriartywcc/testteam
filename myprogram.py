PASSWORD = 'Waubonsee'

def get_input():
    user_pass = input('Enter Password: ')
    return user_pass

def main():

    user_pass = get_input()

    while(user_pass != PASSWORD):
        print('that\'s not it')
        user_pass = input('Enter Password: ')


    print('you got it')

main()
