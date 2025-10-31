
def marginOnCost(cP, sP, VAT=12.5):
    margin = (sP/(1+(VAT/100))-cP)/(sP/(1+(VAT/100)))
    return margin

def markUp(cP, sP, VAT=12.5):
    markup = (sP/(1+(VAT/100))-cP)/cP
    return markup

def discount(sP, newPrice):
    disc = (sP-newPrice)/sP
    return disc

def retail(Cost, Margin = 0.25):
    retailPrice =-1.125*Cost/(Margin-1)
    return retailPrice

def mgnafterSupp(cP, sP, disc, support, VAT=12.5):
    margin = (((sP-(disc-support))/(1+(VAT/100)))-cP)/((sP-(disc-support))/(1+(VAT/100)))
    return margin

