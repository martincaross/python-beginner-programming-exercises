total = int(input('How much money do you have in your pocket\n'))

# ✅ ↓ YOUR CODE HERE ↓ ✅
if total > 100:
    respuesta = "Give me your money!"
elif total > 50:
    respuesta = "Buy me some coffee, you cheap!"
else:
    respuesta = "You are a poor guy, go away!"

print(respuesta)