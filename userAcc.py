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

    def __init__(self,userName,Pword):

      # docstring removed for simplicity

        self.userName = userName
        self.Pword = Pword
       