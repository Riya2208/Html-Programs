ques = [ ["Which language was used to create fb ?", 'Pyhton', 'french','JavaScript','Php', 'None', 4 ],
["Which language was used to create fb ?", 'Pyhton', 'french','JavaScript','Php', 'None', 4 ],
["Which language was used to create fb ?", 'Pyhton', 'french','JavaScript','Php', 'None', 4 ],
] 

levels = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]

money = 0
for i in range (0,len(ques)):
    que = ques[i]
    print(f'Question for Rs.{levels[i]}')
    print(f'a.{que[1]}          b.{que[2]}')
    print(f'c.{que[3]}          d.{que[4]}')
    reply = int(input('Enter your answer (1-4)'))
    if(reply == ques[-1]):
        print('Correct answer,you have won Rs.{levels[i]}')
        if(i == 4):
            money = 10000
        elif(i == 9):
            money = 320000
        elif(i == 14):
            money = 10000000
    else:
        print('Wrong Answer!')    
        break

print(f'Your take home money is {money}')    