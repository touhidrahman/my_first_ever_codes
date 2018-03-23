# LOVE CALCULATOR
# @ TOUHIDUR RAHMAN
# tanimkg@gmail.com
# 07 Jun 2012 1424 F


def calc(he, she, his_bd, her_bd):
    his = []
    her = []
    
    for c in he:
        his.append(ord(c))

    for c in she:
        her.append(ord(c))
        
    avg = (sum(his) + sum(her))//2
    diff = abs(int(his_bd) - int(her_bd))
    his_part = (sum(his) * 100) // avg
    her_part = (sum(her) * 100) // avg
    if diff > 3 and diff < 7:
        his_part = his_part + 5
        her_part = her_part + 5
    elif diff <= 2:
        his_part -= 5
        her_part -= 5
    elif diff == 0:
        his_part -= 10
        her_part -= 10
    else:
        his_part += 5
        her_part -= 7
    print('%s loves %s %s percent' %(he, she, his_part))
    print('%s loves %s %s percent' %(she, he, her_part))
    print("""
======================================================================
""")
    



if __name__ == '__main__':
    again = True
    while again:
        he = input("Enter HIS name: ")
        she = input("Enter HER name: ")
        his_bd = input("The year HE born: ")
        her_bd = input("The year SHE born: ")
        calc(he, she, his_bd, her_bd)
        again = input("Want to play again? Enter 'Y' or 'N': ")
        if again.startswith('Y'):
            again = True
        elif again.startswith('N'):
            again = False
        else:
            again = True
    
