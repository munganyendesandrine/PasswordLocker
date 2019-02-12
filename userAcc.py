class UserAccount:
    """
    Class that generates new instances of contacts.
    """

    account_list = [] # Empty account list
    # Init method up here
    def save_account(self):

        '''
        save_account method saves account objects into account_list
        '''
    
        UserAccount.account_list.append(self)

    def delete_account(self):

        '''
        delete_account method deletes a saved account from the account_list
        '''
        UserAccount.account_list.remove(self)

    @classmethod
    def find_by_username(cls,userName):
        '''
        Method that takes in a username and returns an acount that matches that username.

        Args:
            userName: User Name to search for
        Returns :
            Account of person that matches the user name.
        '''

        for account in cls.account_list:
            if account.userName == userName:
                return account
  
    @classmethod
    def account_exist(cls,userName):
        '''
        Method that checks if an account exists from the account list.
        Args:
            number: User Name to search if it exists
        Returns :
            Boolean: True or false depending if the account exists
        '''
        for account in cls.account_list:
            if account.userName == userName:
                    return True

        return False

    def __init__(self,userName,Pword):

      # docstring removed for simplicity

        self.userName = userName
        self.Pword = Pword
       