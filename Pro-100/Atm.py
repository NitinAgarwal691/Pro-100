class Atm(object):
    def __init__(self, atm_card_number, pin_number):
        self.atm_card_number = atm_card_number
        self.pin_number = pin_number
    def moneyMethod(self,card_method):
        self.card_method = card_method
        return('You Money Would Be Transfered Through '+str(card_method)+' Through The Given Atm Card Number And Pin Number.')

mike = Atm(9172071,9138627)

print(mike.moneyMethod('Balance Enquiry'))