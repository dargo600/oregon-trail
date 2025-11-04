#!/usr/bin/env python

from dataclasses import dataclass
from classes.utils import gen_zoning
from classes.ui import UI


@dataclass
class Traveller:
    MIN_FOOD = 13
    gun_skill: int
    oxen: int
    food: int
    ammo: int
    clothes: int
    misc: int
    cash: int
    ui: UI
    need_clothes: bool = False
    sick: bool = False
    injury: bool = False

    # 1740 - 1820 Ensure that F, B, C, M1 are above 0
    def ensure_globals_are_positive(self) -> None:
        self.food = 0 if self.food < 0 else self.food
        self.ammo = 0 if self.ammo < 0 else self.ammo
        self.clothes = 0 if self.clothes < 0 else self.clothes
        self.misc = 0 if self.misc < 0 else self.misc

    def see_doctor(self):
        self.cash = self.cash - 20
        if self.cash < 0:
            self.ui.display("YOU CAN'T AFFORD A DOCTOR")
            self.ui.display("YOU DIED OF ")
            if self.sick:
                self.ui.display("PNEMONIA")
            else:
                self.ui.display("INJURIES")
            return False
        self.ui.display("DOCTOR'S BILL IS $20")
        self.sick = 0
        self.injury = 0
        return True

    def check(self) -> bool:
        """
        Check Traveller status and see if he requires medical attention
        """
        self.ensure_globals_are_positive()
        if self.food < self.MIN_FOOD:
            self.ui.display("YOU'D BETTER DO SOME HUNTING OR BUY FOOD SOON!!!!")
        if self.sick or self.injury:
            if not self.see_doctor():
                return False
        return True

    #BASIC self.ui.display_zoning
    #2040 self.ui.display "FOOD","BULLETS","CLOTHING","MISC. SUPP.","CASH"
    # https://archive.org/details/bitsavers_cdccyberlaBASICOct80_41102953/page/n85/mode/2up
    def show_stats(self) -> None:
        """
            Displays player stats similar to original Basic code
        """
        result = gen_zoning(["FOOD", "BULLETS", "CLOTHING", "MISC. SUPP.",
                             "CASH"])
        self.ui.display(result)
        result = gen_zoning([self.food, self.ammo, self.clothes,
                                    self.misc, self.cash])
        self.ui.display(result)

    def visit_fort(self):
        pass

    def hunt(self):
        if self.ammo >= 40:
            self.ammo -= 45
            return True
        else:
            self.ui.display("TOUGH---YOU NEED MORE BULLETS TO GO HUNTING")
            return False

    def travel(self):
        pass

