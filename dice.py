import copy

numDice = 5
rolls = []
for d in range(numDice):
    rolls.append(int(1))
combos = [rolls]

for r in range(6 ** len(rolls)):
    rolls[-1] += 1
    for s in range(len(rolls)):
        if(rolls[len(rolls)-s-1] >6):
            rolls[len(rolls)-s-1] = 1
            rolls[len(rolls)-s-2] += 1

    roll = copy.deepcopy(rolls)
    roll.sort()
    if roll not in combos:
        combos.append(roll)
    else:
        isHom = True
        fNum = roll[0]
        for num in roll:
            if num != fNum:
                isHom = False
        if isHom:
            combos.append(roll)
print(len(combos))
