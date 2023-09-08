#Leap year

" " " 
Year % 4 == 0 &
Year % 100 ! = 0 /
Year % 400 == 0

" " "
def isleapyear(year):
    if(year % 4 == 0 and year % 100 !=)
       return True
else:
     return False

Year=int(input("enter a year:"))

if isleapyear(year):
  Print('{} is a leap year.'.format(year))
else:
    Printf('{} is not a leap year.'.format (year))
