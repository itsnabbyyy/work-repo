spam_amount = 0
print(spam_amount)

# ordering Spam, egg, Spam, Spam, Bacon and Spam (4 more servings of Spam)
spam_amount = spam_amount + 4

if spam_amount > 0:
    print("But I don't want ANY spam!")

viking_song = "Spam " * spam_amount
print(viking_song)

type(spam_amount)

type(19.95)

hat_height_cm = 25
my_height_cm = 190

# how tall am I, in metres, when wearing my hat ?
total_height_meters = (hat_height_cm + my_height_cm) / 100
print("Height in meters =", total_height_meters)
