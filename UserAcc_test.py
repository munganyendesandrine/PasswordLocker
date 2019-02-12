import pyperclip
import unittest # Importing the unittest module
from userAcc import UserAccount # Importing the UserAccount class

class TestUserAccount(unittest.TestCase):

    '''
    Test class that defines test cases for the UserAccount class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
     # Items up here .......
   
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_account = UserAccount("James","Muriuki12!") # create Account object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_account.userName,"James")
        self.assertEqual(self.new_account.Pword,"Muriuki12!")
       

    def test_save_multiple_account(self):
        '''
        test_save_multiple_account to check if we can save multiple accounts
        objects to our account_list
        '''
        self.new_account.save_account()
        test_account = UserAccount("TestNewAcc","userPword") # new account
        test_account.save_account()
        self.assertEqual(len(UserAccount.account_list),2)

    # setup and class creation up here
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        UserAccount.account_list = []

    # other test cases here
    def test_save_multiple_account(self):
        '''
        test_save_multiple_account to check if we can save multiple accounts
        objects to our account_list
        '''
        self.new_account.save_account()
        test_account = UserAccount("TestNewAcc","userPword") # new account
        test_account.save_account()
        self.assertEqual(len(UserAccount.account_list),2)

    # More tests above
    def test_delete_account(self):
        '''
        test_delete_account to test if we can remove an account from our account list
        '''
        
        self.new_account.save_account()
        test_account = UserAccount("TestNewAcc","userPword") # new account
        test_account.save_account()

        self.new_account.delete_account()# Deleting an account object
        self.assertEqual(len(UserAccount.account_list),1)

    def test_find_account_by_username(self):
        '''
        test to check if we can find an account by username and display information
        '''

        self.new_account.save_account()
        test_account = UserAccount("TestNewAcc","userPword") # new account
        test_account.save_account()

        found_account = UserAccount.find_by_username("TestNewAcc")

        self.assertEqual(found_account.userName,test_account.userName)

    def test_account_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the contact.
        '''

        self.new_account.save_account()
        test_account = UserAccount("TestNewAcc","userPword") # new account
        test_account.save_account()

        account_exists = UserAccount.account_exist("TestNewAcc")

        self.assertTrue(account_exists)    


    def test_display_all_accounts(self):
        '''
        method that returns a list of all accounts saved
        '''

        self.assertEqual(UserAccount.display_accounts(),UserAccount.account_list)


    def test_save_account(self):
        '''
        test_save_account test case to test if the account object is saved into
         the account list
        '''
        self.new_account.save_account() # saving the new account
        self.assertEqual(len(UserAccount.account_list),1)

    def test_copy_userName(self):
        '''
        Test to confirm that we are copying the user name from a found account
        '''

        self.new_account.save_account()
        UserAccount.copy_userName("James")

        self.assertEqual(self.new_account.userName,pyperclip.paste())


if __name__ ==  '__main__':
    unittest.main()