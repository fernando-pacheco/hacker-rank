def first_num(credit_card):
    if credit_card[0] == '4' or credit_card[0] == '5' or credit_card[0] == '6':
        return True
    else:
        return False
    

def replace_(credit_card):
    if verif_separator(credit_card) == credit_card:
        return credit_card.replace('-','')
    return credit_card


def count_group(credit_card):
    count_digit = 0
    for i in credit_card:
        if i.isdigit():
            count_digit += 1
        elif count_digit != 4:
            return False
        else:
            count_digit = 0
    return True


def count_validation(credit_card):
    if len(replace_(credit_card)) == 16:
        return True
    
    return False


def consec_digits(credit_card):
    count = 0
    replace = replace_(credit_card)
    for n in replace:
        for i in range(0,len(replace)):
            if n == replace[i]:
                count += 1
                if count == 4:
                    return False
            else:
                count = 0
    
    return True


def is_digit(credit_card):
    if not replace_(credit_card).isdigit():
        return False
    
    return True


def verif_separator(credit_card):
    for i in credit_card:
        if i.isdigit() or i == '-':
            continue
        else:
            return False
        
    return credit_card


n = int(input())
credit_cards = [input() for cd in range(n)]

for credit_card in credit_cards:
    if first_num(credit_card) and is_digit(credit_card) and count_group(credit_card) and verif_separator(credit_card) and consec_digits(credit_card) and count_validation(credit_card):
        print('Valid')
    else:
        print('Invalid')