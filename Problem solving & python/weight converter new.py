weight = int(input('Enter your weight '))
weight_type =  input('lbs(L) or kg(K)? ')
if weight_type=='k':
   print (f'Your weight in lbs is  {weight*2.20462}' )
elif weight_type=='l':
   print(f'Your weight in kg is {weight*0.453592}')
else :
   print('Invalid input')