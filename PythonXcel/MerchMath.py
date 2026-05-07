def vatEXcl(P, VAT=12.5):
    vatEXL = P/(1+(VAT/100))
    return vatEXL

def marginOnCost(cP, sP, VAT=12.5):
    if cP == 0 or sP == 0:
        return 0
    else:
        margin = ((sP/(1+(VAT/100)))-cP)/(sP/(1+(VAT/100)))
        return margin

def mrgnOnCost(cP, sP, VAT=12.5):
    if cP == 0 or sP == 0:
        return 0
    else:
        margin = ((vatEXcl(sP, VAT=12.5))-cP)/(vatEXcl(sP, VAT=12.5))
        return margin

def markUp(cP, sP, VAT=12.5):
    markup = (vatEXcl(sP, VAT=12.5)-cP)/cP
    return markup

def discount(sP, newPrice):
    disc = (sP-newPrice)/sP
    return disc

def retail(Cost, Margin = 0.25):
    retailPrice =-1.125*Cost/(Margin-1)
    return retailPrice

def mrgnafterSupp(cP, sP, disc, support, VAT=12.5):
    margin = (((sP-(disc-support))/(1+(VAT/100)))-cP)/((sP-(disc-support))/(1+(VAT/100)))
    return margin

def disc(sP,Cost, Mrgn):
    disc = sP-((Cost*1.125)/(1-Mrgn))
    return disc

def combo(cp1, cp2, sp1, sp2, disc, VAT=12.5):
    totComboCst = cp1 + cp2
    totComboPrice = sp1 + sp2
    ComboPrice = totComboPrice-disc
    mrkp = ((ComboPrice/1+(VAT/100))-totComboCst)/(ComboPrice/1+(VAT/100))
    return totComboCst, totComboPrice, ComboPrice, mrkp
    