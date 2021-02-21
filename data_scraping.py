import nn

a = nn.searchnet('Truth.db')

a.train('I did not have sexual relations with that woman, Miss Kravinsky.', 0)
print("Training...")

a.train('I do not believe in god as he is who never was.', 0)
print("Training...")

a.train("I didn't see him go, I promise.", 1)
print("Training...")

a.train('He went in and kissed her ass off.', 1)
print("Training...")

a.train('I am very sorry for your loss, Johnny was like a brother to me.', 1)
print("Training...")

a.train('Did you say something, mister Greene. Because, well I am sorry for saying this but you can go shit your idea.', 1)
print("Training...")

a.train('In all candor, I did not do that murder. This is my plea, not guilty.', 0)
print("Training...")

a.train('Honestly, I am very nice and so good and kind. You all should learn a thing or two from me.', 0)
print("Training...")

a.train("That seems right now, don't it!", 1)
print("Training...")

a.train("I'd know the truth", 1)
print("Training...")

a.train('Honestly, I am very nice and so good and kind. You all should learn a thing or two from me.', 0)
print("Training...")

a.train("We will win, I promise you this much.", 0)
print("Training...")

a.train("I didn't throw my own phone in the pool, mom.", 1)
print("Training...")