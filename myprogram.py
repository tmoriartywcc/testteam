PASSWORD = 'Waubonsee'

def get_input():
    user_pass = input('Enter Password: ')
    return user_pass


def main():

    user_pass = get_input()

    if(user_pass == PASSWORD):
        print('You got it')
    else:
        print('Not quite right')

main()
