import math
import os
os.system("")

class style():
    YELLOW = '\033[93m'
    BLUE = '\033[34m'
    CYAN = '\033[36m'
    PURPLE ='\033[35m'
    RED = '\033[31m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

print(style.UNDERLINE + style.YELLOW  + "EXERCISE ONE - PRINTING FIRST TWENTY NARCISSISTIC NUMBERS." + style.RESET + style.CYAN + "\n" )

CountCheck, x = int(0), int(1)
while CountCheck < 21:    
    z, y, length = x, int(0), int(1)
    while x % (10 ** length) != x :
        length += 1    
    for i in range(length-1, -1, -1):
        y += (z // (10 ** (i) )) ** length
        z = z % (10 ** i)        
    if (x == y):
        print(x, " IS A NARCISSISTIC NUMBER.")
        CountCheck += 1        
    x += 1
        

print("\n" + style.UNDERLINE + style.YELLOW + "EXERCISE TWO - PRINTING 2000 PRIME NUMBERS WITH TWENTY ON EACH LINE." + style.RESET +style.CYAN + "\n")

CountCheck = 0
for PrimeNumbers in range(1000):
   if PrimeNumbers > 1:
       for i in range(2, PrimeNumbers):
           if (PrimeNumbers % i) == 0:
               break
       else:       
            if CountCheck % 20 == 0:
                print('')        
            print(PrimeNumbers, end = " ")
            CountCheck += 1        
            
            
print("\n\n" + style.UNDERLINE + style.YELLOW + "EXERCISE THREE - CALCULATING THE GREATEST COMMON DIVISOR OF TWO GIVEN POSITIVE INTEGER." + style.RESET +style.PURPLE + "\n")

while True:
    x = int(input("PLEASE WRITE YOUR FIRST POSITIVE INTEGER: "+style.BLUE))
    y = int(input(style.PURPLE+ "PLEASE WRITE YOUR SECOND POSITIVE INTEGER: "+ style.BLUE))
    z = int(0)
    if(x < 0 or y < 0):
        print(style.RED + "\nERROR!!!!")
        print("PLEASE ENTER POSITIVE INTEGER ONLY.\n")
        print(style.PURPLE)
    else:
        break
        
print(style.CYAN)
if x < y:
    z = x
    x = y
    y = z     
while True:
    z = x % y 
    if z == 0:
        break   
    x = y 
    y = z 
print(y, " IS THE GREATEST COMMON DIVISOR.")

print("\n" + style.UNDERLINE + style.YELLOW + "EXERCISE FOUR - CALCULATING SIN(X) USING TAYLOR SERIES." + style.RESET +style.PURPLE + "\n")

def Factorial(n):
    CountCheck = 1
    for i in range(2, n + 1):
        CountCheck *= i
    return CountCheck 


while True:
    sinx = int(0)
    print(style.PURPLE)
    x = int(input("PLEASE TYPE IN THE VALUE OF X IN DEGREES: " + style.BLUE))
    print(style.CYAN)
    for i in range(16):
        sinx += ( ( (-1) ** i) / Factorial( (2 * i) + 1) ) * ( math.radians(x) ** ( (2 * i) + 1 ) )
    print("SIN(", x, ") = ", sinx)
    print(style.PURPLE)
    Retry = input("ENTER Y TO TRY DIFFERENT VALUE OR OTHER PRESS ANYTHING TO CANCEL: " + style.BLUE)
    if(Retry == 'y' or Retry == 'Y'):
        Retry=''
    else:
        break