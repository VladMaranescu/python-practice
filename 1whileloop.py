secret= input("Enter the secret word:")  
guess=""
word=""
s=0
i=0
while i<3:
 guess =input("Enter your guess") 
 i=i+1
 if guess == secret :
  print("You win")
  i=0

if i==3:
 print("Let me help you,lets guess each letter indvidualy: ")
 while s<=len(secret):
  guess= input("Enter your guessed letter:")
  if secret[s]==guess:
   word[s]=guess
   s=s+1
  else:
   guess= input("Enter your guessed letter:")
  
print(word)

  


