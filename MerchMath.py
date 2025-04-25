
def marginOnCost(cP, sP, VAT=12.5):
    margin = (sP/(1+(VAT/100))-cP)/(sP/(1+(VAT/100)))
    return margin

def discount(sP, newPrice):
    disc = (sP-newPrice)/sP
    return disc

