PASSWORD = 'WCC'
USER_PROMPT = 'Enter Password: '

def get_input():
    user_pass = input(USER_PROMPT)
    return user_pass

def main():

    user_pass = get_input()

    while(user_pass != PASSWORD):
        print('that\'s not it')
        user_pass = input('USER_PROMPT')


    print('you got it')

main()
