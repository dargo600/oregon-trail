#!/usr/bin/env python

"""
The main Game Module
"""

from dataclasses import dataclass
from classes.traveller import Traveller
from classes.ui import UI
from classes.utils import tab

# IDENTIFICATION OF VARIABLES IN THE PROGRAM^*
# t.oxen             A  = AMOUNT SPENT ON ANIMALS
# t.ammo             B  = AMOUNT SPENT ON AMMUNITION
#                    B1 = ACTUAL RESPONSE TIME FOR INPUTTING "BANG"
#                    B3 = CLOCK TIME AT START OF INPUTTING "BANG"
# t.clothes          C  = AMOUNT SPENT ON CLOTHING
# t.need_clothes     C1 = FLAG FOR INSUFFICIENT CLOTHING IN COLD WEATHER
#                    C$ = YES/NO RESPONSE TO QUESTIONS
#                    D1 = COUNTER IN GENERATING EVENTS
# g.turn_number      D3 = TURN NUMBER FOR SETTING DATE
#                    D4 = CURRENT DATE
# t.gun_skill        D9 = CHOICE OF SHOOTING EXPERTISE LEVEL
#                    E  = CHOICE OF EATING
# t.food             F  = AMOUNT SPENT ON FOOD
# t.done_sth_pass    F1 = FLAG FOR CLEARING SOUTH PASS
# t.done_blue_mnts   F2 = FLAG FOR CLEARING BLUE MOUNTAINS
#                    F9 = FRACTION OF 2 WEEKS TRAVELED ON FINAL TURN
# t.injury           K8 = FLAG FOR INJURY (no K5)
#                    L1 = FLAG FOR BLIZZARD
# g.miles            M  = TOTAL MILEAGE WHOLE TRIP
# t.misc             M1 = AMOUNT SPENT ON MISCELLANEOUS SUPPLIES
# g.prev_turn_miles  M2 = TOTAL MILEAGE UP THROUGH PREVIOUS TURN
# g.sth_pass_miles   M9 = FLAG FOR CLEARING SOUTH PASS IN SETTING MILEAGE
#                    P  = AMOUNT SPENT ON ITEMS AT FORT
#                    R1 = RANDOM NUMBER IN CHOOSING EVENTS
# t.sick             S4 = FLAG FOR ILLNESS
#                    S5 = ""HOSTILITY OF RIDERS"" FACTOR
#                    S6 = SHOOTING WORD SELECTOR
#                    S$ = VARIATIONS OF SHOOTING WORD
#                    T  = CASH LEFT OVER AFTER INITIAL PURCHASES
#                    T1 = CHOICE OF TACTICES WHEN ATTACKED
#                    X  = CHOICE OF ACTION FOR EACH TURN
# g.fort_exists      X1 = FLAG FOR FORT OPTION
dates = [
    "MARCH 29",
    "APRIL 12 ",
    "APRIL 26 ",
    "MAY 10 ",
    "MAY 24 ",
    "JUNE 7 ",
    "JUNE 21 ",
    "JULY 5 ",
    "JULY 19 ",
    "AUGUST 2 ",
    "AUGUST 16 ",
    "AUGUST 31 ",
    "SEPTEMBER 13 ",
    "SEPTEMBER 27 ",
    "OCTOBER 11 ",
    "OCTOBER 25 ",
    "NOVEMBER 8 ",
    "NOVEMBER 22 ",
    "DECEMBER 6 ",
    "DECEMBER 20 ",
]

weekdays = [
    "SATURDAY",
    "SUNDAY",
    "MONDAY",
    "TUESDAY",
    "WEDNESDAY",
    "THURSDAY",
    "FRIDAY"
]

# Lines 240 - 680
INTRO_STR: str = """PROGRAM SIMULATES A TRIP OVER THE OREGON TRAIL FROM
INDEPENDENCE, MISSOURI TO OREGON CITY, OREGON IN 1847.
YOUR FAMILY OF FIVE WILL COVER THE 2040-MILE OREGON TRAIL
IN 5-6 MONTHS --- IF YOU MAKE IT ALIVE.

YOU HAD $900 TO SPEND ON SUPPLIES, BUT YOU'VE JUST
    PAID $200 FOR A WAGON, LEAVING YOU WITH $700.
YOU WILL NEED TO SPEND THE REST OF YOUR MONEY ON THE
FOLLOWING ITEMS:

    OXEN - YOU CAN SPEND $200-$300 ON YOUR TEAM
            THE MORE YOU SPEND, THE FASTER YOU'LL GO
            BECAUSE YOU'LL HAVE BETTER ANIMALS

    FOOD - THE MORE YOU HAVE, THE LESS CHANCE THERE
            IS OF GETTING SICK

    AMMUNITION - $1 BUYS A BELT OF 50 BULLETS
                    YOU WILL NEED BULLETS FOR ATTACKS BY ANIMALS
                    AND BANDITS, AND FOR HUNTING FOOD

    CLOTHING - THIS IS ESPECIALLY IMPORTANT FOR THE COLD
                WEATHER YOU WILL ENCOUNTER WHEN CROSSING
                THE MOUNTAINS

    MISCELLANEOUS SUPPLIES - THIS INCLUDES MEDICINE AND
        OTHER THINGS YOU WILL NEED FOR SICKNESS
        AND EMERGENCY REPAIRS

YOU CAN SPEND ALL YOUR MONEY BEFORE YOU START YOUR TRIP -
OR YOU CAN SAVE SOME OF YOUR CASH TO SPEND AT FORTS ALONG
THE WAY WHEN YOU RUN LOW. HOWEVER, ITEMS COST MORE AT
THE FORTS. YOU CAN ALSO GO HUNTING ALONG THE WAY TO GET
MORE FOOD.
WHENEVER YOU HAVE TO USE YOUR TRUSTY RIFLE ALONG THE WAY,
YOU WILL BE TOLD TO TYPE IN THAT WORD (ONE THAT SOUNDS LIKE A
GUN SHOT). THE FASTER YOU TYPE IN THAT WORD AND HIT THE
RETURN KEY, THE BETTER LUCK YOU'LL HAVE WITH YOUR GUN.\n

AT EACH TURN, ALL ITEMS ARE SHOWN IN DOLLAR AMOUNTS
EXCEPT BULLETS
WHEN ASKED TO ENTER MONEY AMOUNTS, DON'T USE A \"$\".
GOOD LUCK!\n\n"""


@dataclass
class Game:
    """ Class for keeping track of Game progress """
    MAX_MILES: int = 2040
    MIN_OXEN_AMOUNT: int = 200
    MAX_OXEN_AMOUNT: int = 300
    done_sth_pass: bool = False
    done_blue_mnts: bool = False
    sth_pass_miles: bool = False
    current_turn: int = 0
    miles: int = 0
    prev_turn_miles: int = 0
    fort_exists: bool = False
    ui: UI = None

    def introduction(self) -> None:
        # 240 - 680
        self.ui.display(INTRO_STR)
        prompt = "HOW GOOD A SHOT ARE YOU WITH YOUR RIFLE?"
        prompt += "\n  (1) ACE MARKSMAN, (2) GOOD SHOT, (3) FAIR TO MIDDLIN'"
        prompt += "\n  (4) NEED MORE PRACTICE, (5) SHAKY KNEES>\n"
        gun_skill = self.ui.get_user_input(prompt, 1, 5)
        cash = 700

        prompt = "HOW MUCH DO YOU WANT TO SPEND ON YOUR OXEN TEAM?  >"
        oxen = self.ui.get_user_input(prompt, self.MIN_OXEN_AMOUNT,
                                      self.MAX_OXEN_AMOUNT)
        cash = cash - oxen

        prompt = "HOW MUCH DO YOU WANT TO SPEND ON FOOD?  >"
        food = self.ui.get_user_input(prompt, 0, cash)
        cash = cash - food

        prompt = "HOW MUCH DO YOU WANT TO SPEND ON AMMUNITION?  >"
        ammo = self.ui.get_user_input(prompt, 0, cash)
        cash = cash - ammo

        prompt = "HOW MUCH DO YOU WANT TO SPEND ON CLOTHING?  >"
        clothes = self.ui.get_user_input(prompt, 0, cash)
        cash = cash - clothes

        prompt = "HOW MUCH DO YOU WANT TO SPEND ON MISCELLANEOUS SUPPLIES?  >"
        misc = self.ui.get_user_input(prompt, 0, cash)
        ammo *= 50  # 1170 $1 per bullet
        self.traveller = Traveller(gun_skill=gun_skill, oxen=oxen, food=food,
                                   ammo=ammo, clothes=clothes, misc=misc,
                                   cash=cash, ui=self.ui)
        print(f"AFTER ALL YOUR PURCHASES, YOU NOW HAVE ${cash} LEFT.")
        print("\nMONDAY MARCH 29 1847")

    def conclusion(self) -> None:
        self.ui.display("CONGRATULATIONS! YOU'VE MADE IT TO OREGON CITY!")

    def do_final_turn(self) -> None:
        self.ui.display("YOU HAVE BEEN ON THE TRAIL TOO LONG ------")
        self.ui.display("YOUR FAMILY DIES IN THE FIRST BLIZZARD OF WINTER")

    def is_final_turn(self, miles, max_miles) -> None:
        if miles >= max_miles:
            self.do_final_turn()

    def get_date(self, current_turn) -> None:
        if self.miles >= self.MAX_MILES:
            self.do_final_turn()
            return
        if current_turn < len(self.dates):
            self.ui.display(f"\n{weekdays[0]} {dates[current_turn]} 1847")


    def request_action(self) -> None:
        if self.fort_exists:
            while True:
                prompt = "DO YOU WANT TO (1) STOP AT THE NEXT FORT, (2) HUNT,"
                prompt += "\n (3) CONTINUE"
                action = self.ui.get_user_input(prompt, 1, 3)
                if action == 1:
                    self.traveller.visit_fort()
                elif  action == 2:
                    result = self.traveller.hunt()
                    if result:
                        break
                else:
                    self.traveller.travel()
        else:
            while True:
                prompt = "DO YOU WANT TO (1) HUNT OR (2) CONTINUE"
                action = self.ui.get_user_input(prompt, 1, 2)
                if action == 1:
                    result = self.traveller.hunt()
                    if result:
                        break
                else:
                    self.traveller.travel()

    def handle_turn(self) -> bool:
        if not self.traveller.check():
            return False
        if not self.sth_pass_miles:
            self.ui.display(f"TOTAL MILEAGE IS {self.miles}")
        else:
            self.ui.display("TOTAL MILEAGE IS 950")
            self.south_pass_flag_updated_mileage = False
        self.traveller.show_stats()
        if not self.request_action():
            return False
        return True


    def handle_death(self) -> None:
        self.ui.handle_death()


