email = input('Enter your E-mail : ') #g@g.in
k,j,d = 0,0,0

if len(email) >= 6: 
    if email[0].isalpha(): #1
       if ("@" in email) and (email.count('@') == 1): #2
            if (email[-4] == ".") ^ (email[-3] == "."): #3
               for i in email:
                   if i.isspace(): #5
                    k = 1
                   elif i.isalpha():
                       if i.isupper(): # W--W == w #5
                        j = 1
                       elif i.isdigit():
                        continue
                       elif i=="_" or i=="." or i=="@":
                        continue
                       else: #5
                        d = 1
               if k == 1 or j == 1 or d == 1:
                     print('Wrong Email 5')    
               else:
                     print('Right Email ')        
            else:
                print('Wrong Email 4')
       else:
            print('Wrong Email 3')
    else:
        print('Wrong Email 2')
else:
    print('Wrong Email 1')
