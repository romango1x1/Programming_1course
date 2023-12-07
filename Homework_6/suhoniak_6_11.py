password = input()
defence_lvl = 0
symbols = set("!\"#$%&'()*+")

if any(i.islower() for i in password):
    defence_lvl += 1
if any(i.isupper() for i in password):
    defence_lvl += 1
if any(i.isdigit() for i in password):
    defence_lvl += 1
if any(i in symbols for i in password):
    defence_lvl += 1
if sum(1 for _ in password) >= 8:
    defence_lvl += 1

print(defence_lvl)

# https://www.eolymp.com/uk/submissions/15409628
