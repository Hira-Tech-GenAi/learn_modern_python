#? Final Value: After the loop completes, magician holds the last value it was assigned, which is 'carolina'.

magicians:list[str] = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
print(f"I can't wait to see your next trick, {magician.title()}.\n")