#!/usr/bin/env python3.6
from userAcc import UserAccount # Importing the UserAccount class

def create_account(userName,Pword):
    '''
    Function to create a new account
    '''
    new_account = UserAccount(userName,Pword)
    return new_account

def save_account(account):
    '''
    Function to save account
    '''
    account.save_account()

def delete_account(account):
    '''
    Function to delete an account
    '''
    account.delete_account()   
    
def find_by_username(userName):
    '''
    Function that finds an account by username and returns the account
    '''
    return UserAccount.find_by_username(userName)     

def account_exist(userName):
    '''
    Function that check if an account exists with that username and return a Boolean
    '''
    return UserAccount.account_exist(userName)

def display_accounts():
    '''
    Function that returns all the saved accounts
    '''
    return UserAccount.display_accounts()    

def main():
    print("Hello Welcome to your account list. What is your name?")
    userName = input()

    print(f"Hello {userName}. what would you like to do?")
    print('\n')

    while True:
                    print("Use these short codes : ca - create a new account, da - display accounts, fa -find an account, ex -exit the account list, del -delete an account you no longer want to use ")
                    print('\n')
                    short_code = input().lower()

                    if short_code == 'ca':
                            print("New Account")
                            print("-"*10)

                            print ("User name ....")
                            userName = input()

                            print("Password ...")
                            Pword = input()


                            save_account(create_account(userName,Pword)) # create and save new account.
                            print ('\n')
                            print(f"New Account {userName} {Pword} created")
                            print(f"The Password length is {len(Pword)} for the password you created")
                            print ('\n')

                    elif short_code == 'da':

                            if display_accounts():
                                    print("Here is a list of all your accounts")
                                    print('\n')

                                    for account in display_accounts():
                                            print(f"{account.userName} {account.Pword}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any account saved yet")
                                    print('\n')

                    elif short_code == 'fa':

                            print("Enter the user name you want to search for")

                            search_account = input()
                            if account_exist(search_account):
                                    search_account = find_by_username(search_account)
                                    print(f"{search_account.userName} {search_account.Pword}")
                                    print('-' * 20)

                                    print(f"User Name.......{search_account.userName}")
                                    print(f"Password.......{search_account.Pword}")
                                    print ('\n')
                            else:
                                    print("That account does not exist")
                                    print ('\n')

                    elif short_code == 'del':

                            print("Enter the user name you want to delete")

                            search_account = input()
                            if account_exist(search_account):
                                   search_account = find_by_username(search_account)
                                   delete_account(search_account)
                                   print("Account deleted successfully!")
                                   print ('\n')
                            else:
                                   print("Account not deleted !")   
                                   print ('\n')             

                    elif short_code == "ex":
                            print("Bye .......")
                            break
                            print ('\n')
                    else:
                            print("I really didn't get that. Please use the short codes")
                            print ('\n')

if __name__ == '__main__':

    main()