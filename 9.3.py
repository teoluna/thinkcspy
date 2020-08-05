poem = """Każdy nowy dzień jest kwiatem
Który zakwita w naszych rękach
Tam gdzie się kocha, nigdy nie zapada noc.
Serce to cząstka człowieka,
Które tęskni, kocha i czeka."""

def count(p):
    low = "aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż"
    up = "AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUVWXYZŹŻ"
    totalchar = 0
    e_number = 0
    for char in p:
        if char in low or char in up:
            totalchar = totalchar + 1 # count total alphabetic characters
        if char == "e":
            e_number = e_number + 1 # count the occurrence of letter "e"
        e_percentage = e_number/totalchar*100
    print("Your text contains {} alphabetic characters, of which {} ({:.1f}%) are 'e'.".format(totalchar, e_number, e_percentage))
            
count(poem)