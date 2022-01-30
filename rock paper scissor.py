import random
cmptr = 0
plyr = 0

def rock_paper_scissor():
    global plyr, cmptr
    u = input("Rock[R], Paper[P], Scissor[s] :").lower()
    while (('r' not in u) and ('p' not in u) and ('s' not in u)) or (len(u) > 1):
        u = input("Invalid input, please enter only 'r' or 'p' or 's' :")
    c = random.choice(['r', 'p', 's'])
    v = ['r', 'p', 's']
    b = ["👊 Rock 👊", "🖐 Paper 🖐", "✌ Scissor ✌"]
    u = v.index(u)
    c = v.index(c)
    a = u - c
    print(f"user : {b[u]}   computer : {b[c]}")
    if (a == -2) or (a == 1):
        print("🎆🎆🎆🎆🎆🎊🎊 You Win 🎊🎊🎆🎆🎆🎆🎆")
        plyr += 1
    elif a == 0:
        print("🤜🤜🤜 Tie 🤛🤛🤛")
    else:
        print("😩😩😩😔 You Lose 😔😩😩😩")
        cmptr += 1
    print("")


r = int(input("How many rounds you wish to play : "))

n = r
while r>0:
    rock_paper_scissor()
    r -= 1
if plyr > cmptr:
    print(f"""
        *****You won the Game ******
in this {n} round(s), You won {plyr} games
""")
elif cmptr > plyr:
    print(f"""
        *****You Lose the Game ******
in this {n} round(s), You won {plyr} games
""")
else:
    print(f"""
        *****The Game is tie ******
in this {n} round(s), you won {plyr} games""") 
