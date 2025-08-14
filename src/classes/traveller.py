#!/usr/bin/env python

from classes.utils import print_zoning

class Traveller:
    MIN_FOOD = 13
    def __init__(self, gun_skill, oxen, food, ammo, clothes, misc, cash):
        self.gun_skill = gun_skill
        self.oxen = oxen
        self.food = food
        self.ammo = ammo
        self.clothes = clothes
        self.misc = misc
        self.cash = cash
        self.need_clothes = False
        self.sick = False
        self.injury = False

    # 1740 - 1820 Ensure that F, B, C, M1 are above 0
    def ensure_globals_are_positive(self): 
        self.food = 0 if self.food < 0 else self.food
        self.ammo = 0 if self.ammo < 0 else self.ammo
        self.clothes = 0 if self.clothes < 0 else self.clothes
        self.misc = 0 if self.misc < 0 else self.misc

    def see_doctor(self):
        self.cash = self.cash - 20
        if self.cash < 0:
            print("YOU CAN'T AFFORD A DOCTOR")
            print("YOU DIED OF ")
            if self.sick:
                print("PNEMONIA")
            else:
                print("INJURIES")
            return False
        print("DOCTOR'S BILL IS $20")
        self.sick = 0
        self.injury = 0
        return True

    def check(self):
        """
        Check Traveller status and see if he requires medical attention
        """
        self.ensure_globals_are_positive()
        if self.food < self.MIN_FOOD:
            print("YOU'D BETTER DO SOME HUNTING OR BUY FOOD SOON!!!!")
        if self.sick or self.injury:
            if not self.see_doctor():
                return False
        return True

    #BASIC print_zoning
    #2040 PRINT "FOOD","BULLETS","CLOTHING","MISC. SUPP.","CASH"
    # https://archive.org/details/bitsavers_cdccyberlaBASICOct80_41102953/page/n85/mode/2up
    def show_stats(self):
        """
            Displays player stats similar to original Basic code
        """
        print_zoning([ "FOOD", "BULLETS", "CLOTHING", "MISC. SUPP.", "CASH" ])
        print_zoning([self.food, self.ammo, self.clothes, self.misc, self.cash])

    def visit_fort(self):
        pass

    def hunt(self):
        if self.ammo >= 40:
            self.ammo -= 45
            return True
        else:
            print("TOUGH---YOU NEED MORE BULLETS TO GO HUNTING")
            return False
    
    def travel(self):
        pass
 