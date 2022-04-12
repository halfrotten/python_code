#Paul Otradovec
def CheckLength(password):#chec length 
    pass_len=len(password)
    if pass_len>5 and pass_len<20: #set parameters
                                    #for password more than 5 less than 20
        return True
    else:
        print('incorrect length')
     
def CheckRequiredChars(password):#check for characters
    check_alpha=False#set default arguements
    check_digit=False 
    for i in password:
        if i.isdigit():#if digit character throw a flag for true
            check_digit=True
        if i.isalpha():#if alpha character throw a flag for true
            check_alpha=True
    if check_alpha and check_digit:#if both type of character present
                                   #throw a flag for true
        return True
    elif check_alpha==False:
        print( 'bad character no alpha char')
    else:
        print( 'bad character no numeric char')
       
def CheckProhibited(password):#check for whitespace
    space=True
    for i in password:
        if i.isspace():
            space=False
            print( 'bad character whitespace') #prints if has space
        
    if space==True:
        return True #returns true if clear of space        
if __name__=='__main__':
    entry=input('type in password: ')
    if CheckLength(entry)==True and CheckRequiredChars(entry)==True and CheckProhibited(entry)==True:
            #if all checks true print valid
            print('valid pass')
    
   
