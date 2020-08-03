'''
Created by Noah Robinson
Description: This code will store user names and passwords for the user
8/2/2020 - Present
'''
import random
with open('book.txt', 'a+') as file:
    #file.write('new line\n')

    def Menu():
        print('Passbook Menu Options:')
        print('1. Read all accounts')
        print('2. Add an account')
        print('3. Remove an account(Enter line #)')
        print('4. Delete all entries')
        print('5. Save & Exit')
    
        selec = input('Please enter choice(1-5): ')
        return selec
    Terminate = False
    #def DeleteAcc():
        
        
    while Terminate == False:
        userchoice = Menu()
        error = True
        if userchoice == '1':
            file.flush()
            print('\nDisplaying all accounts: \n(Hash: Username - Password)')
            with open('book.txt','r') as f:
                for line in f:
                    print(line.rstrip('\n'))
            print('Done')
        elif userchoice == '2':
            name = input('Enter username: ')
            password = input('Enter password: ')
            number = random.randint(1111,9999)
            with open('book.txt','r') as f:                                    #Check if new hash has alread exists
                while str(number) in f.read():
                    number = random.randint(1111,9999)
            new = '#' + str(number) +': '+ name + ' - ' + password+'\n'
            file.write(new)
        elif userchoice == '3':
            file.flush()
            print('\nYour accounts are: \n(Username - Password)')
            with open('book.txt','r') as f:
                for line in f:
                    print(line.rstrip('\n'))
            h = input('Which account would you like to delete?(Enter random account number): ')
            #DeleteAcc(h)
            
        elif userchoice == '4':
            file. truncate(0)
        elif userchoice == '5':
            file.flush()
            Terminate = True
            error = False
        else:
            print('Entry invalid')
        while error == True:
            v = input('Would you like to return to menu?(Y/N): ')
            if v == 'N':
                Terminate = True
                error = False
            elif v == 'Y':
                Terminate = False
                error = False
            else:
                print('Invalid Entry')
                error = True
    
print('Your work was saved. Thank you for using Passbook')
