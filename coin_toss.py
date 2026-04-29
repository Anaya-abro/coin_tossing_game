import random
print('Welcome to Coin tossing game🪙\n')

coin = ['heads','tails']
while True:
 user = input('please enter toss to toss the coin:').lower()
#  result = random.choice
 if user == 'toss':
   result = random.choice(coin)
   if result == 'heads':
    print('you got heads🎉')

   else:
    print('you got tails🎉')



   play_again = input('Do you want to play again(yes/no)').lower()
   if play_again == 'no':
    print('Thank you for playing🎮 ')
    break

 else:
  print('Invalid text! (please write toss)')



