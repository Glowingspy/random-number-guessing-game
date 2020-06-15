import random
import time




print('This is a GAME where you choose RANDOM numbers to START and END from, and then GUESS the one RANDOM NUMBER!!!!!!!')

def main_code():
    time.sleep(3)
    print('From what integer do you want to start from ?')
    time.sleep(1)
    print('Type your first integer where you want to start from')
    print('You have 5 chances')
    
    #print(len(varible))
    #first value
    
    a = float(input())
    if a != int(a):
        print('Invalid.You typed something other than an integer. The program will restart in 3 seconds ')
        time.sleep(3)
        main_code()
    elif a == str(a):
        print('Invalid.You typed something other than an integer. The program will restart in 3 seconds ')
        time.sleep(3)
        main_code()    
   
    
    
    
    
    
    #second value
    
    
    
    
    print('TYPE your second integer where you want the set of numbers to end.(This number must be higher than your first input)')
    b = float(input())
    if b != int(b):
        print('Invalid.You typed something other than an integer. The program will restart in 3 seconds')
        time.sleep(3)
        main_code()
        
    if b <= a:
        print('Invalid. The second number must be greater than the first numnber.')
        time.sleep(3)
        print('The program will start in about 5 seconds')
        
        main_code()
    
    
   
    
    
    
    x = random.randint(int(a), int(b))
    print('Guess an integer between ' + (str(a)) + ' and ' + (str(b)))
    y = int(input())
    if y == int(x) :
        print('You got the number. Do you want to play again')
        
    
    system = []    
    
    
      

    

   
    
    while y != x:
        if y > x:
            print('Think lower')
            y = int(input())
            system.extend('1')
            
        elif y < x:
            print('Think higher')
            y = int(input())
            system.append('1')
                       
        while len(system) != (7):
            system.extend('1')
            break
        if len(system) == 7:
            print('STOP!! You have reached your maximum number of chances.')
            time.sleep(0.5)
            print('Do you want to play again')
            print('Type "yes" or "no" ')
            re = input()
            
            if re == 'no':
                print('Get out of here!!!')
            
            elif re == 'yes':
                print('OK. ')
                time.sleep(0.5)
                main_code()
            else:
                print('Your answer was INVALID. Restart the program if you wanted to say YES, or exit if you answer was NO!!')
              
     
    
    if y == x :
        print('You got the number. Do you want to play again') 
        time.sleep(1)
        print('Type "yes" or "no" ')
        z = input()
        if z == 'no':
            print('Get out of here!!!')
        elif z == 'yes':
            print('Ok')
            time.sleep(0.5)
            main_code()
        else:
            print('That is an invalid statment. Rerun the program if you wanted to start or exit if you said no.')
        
      
main_code()