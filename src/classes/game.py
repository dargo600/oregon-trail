#!/usr/bin/env python

from classes.traveller import Traveller
from classes.utils import tab, get_user_input

# IDENTIFICATION OF VARIABLES IN THE PROGRAM^*
# t.oxen             A  = AMOUNT SPENT ON ANIMALS
# t.ammo             B  = AMOUNT SPENT ON AMMUNITION
# g.response         B1 = ACTUAL RESPONSE TIME FOR INPUTTING "BANG"
# g.start            B3 = CLOCK TIME AT START OF INPUTTING "BANG"
# t.clothing         C  = AMOUNT SPENT ON CLOTHING
# t.need_clothes     C1 = FLAG FOR INSUFFICIENT CLOTHING IN COLD WEATHER
#                    C$ = YES/NO RESPONSE TO QUESTIONS
#                    D1 = COUNTER IN GENERATING EVENTS
# g.turn_number      D3 = TURN NUMBER FOR SETTING DATE
#                    D4 = CURRENT DATE
# t.gun_skill        D9 = CHOICE OF SHOOTING EXPERTISE LEVEL
#                    E  = CHOICE OF EATING
#                    F  = AMOUNT SPENT ON FOOD
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

class Game:
    MAX_MILES = 2040
    MIN_OXEN_AMOUNT = 200
    MAX_OXEN_AMOUNT= 300

    def __init__(self):
        self.done_sth_pass = False
        self.done_blue_mnts = False
        self.sth_pass_miles = False
        self.current_turn = 0
        self.miles = 0
        self.prev_turn_miles = 0
        self.fort_exists = False

    def introduction(self):
        # 240 - 680
        print("PROGRAM SIMULATES A TRIP OVER THE OREGON TRAIL FROM")
        print("INDEPENDENCE, MISSOURI TO OREGON CITY, OREGON IN 1847.")
        print("YOUR FAMILY OF FIVE WILL COVER THE 2040-MILE OREGON TRAIL")
        print("IN 5-6 MONTHS --- IF YOU MAKE IT ALIVE.")
        print("")
        print("YOU HAD $900 TO SPEND ON SUPPLIES, BUT YOU'VE JUST")
        print("  PAID $200 FOR A WAGON, LEAVING YOU WITH $700.")
        print("YOU WILL NEED TO SPEND THE REST OF YOUR MONEY ON THE")
        print("   FOLLOWING ITEMS:")
        print("")
        print("     OXEN - YOU CAN SPEND $200-$300 ON YOUR TEAM")
        print("            THE MORE YOU SPEND, THE FASTER YOU'LL GO")
        print("               BECAUSE YOU'LL HAVE BETTER ANIMALS")
        print("")
        print("     FOOD - THE MORE YOU HAVE, THE LESS CHANCE THERE")
        print("               IS OF GETTING SICK")
        print("")
        print("     AMMUNITION - $1 BUYS A BELT OF 50 BULLETS")
        print("            YOU WILL NEED BULLETS FOR ATTACKS BY ANIMALS")
        print("               AND BANDITS, AND FOR HUNTING FOOD")
        print("")
        print("     CLOTHING - THIS IS ESPECIALLY IMPORTANT FOR THE COLD")
        print("               WEATHER YOU WILL ENCOUNTER WHEN CROSSING")
        print("               THE MOUNTAINS")
        print("")
        print("     MISCELLANEOUS SUPPLIES - THIS INCLUDES MEDICINE AND")
        print("              OTHER THINGS YOU WILL NEED FOR SICKNESS")
        print("              AND EMERGENCY REPAIRS")
        print("")
        print("")
        print("YOU CAN SPEND ALL YOUR MONEY BEFORE YOU START YOUR TRIP -")
        print("OR YOU CAN SAVE SOME OF YOUR CASH TO SPEND AT FORTS ALONG")
        print("THE WAY WHEN YOU RUN LOW. HOWEVER, ITEMS COST MORE AT")
        print("THE FORTS. YOU CAN ALSO GO HUNTING ALONG THE WAY TO GET")
        print("MORE FOOD.")
        print("WHENEVER YOU HAVE TO USE YOUR TRUSTY RIFLE ALONG THE WAY,")
        print("YOU WILL BE TOLD TO TYPE IN THAT WORD (ONE THAT SOUNDS LIKE A")
        print("GUN SHOT). THE FASTER YOU TYPE IN THAT WORD AND HIT THE")
        print("RETURN KEY, THE BETTER LUCK YOU'LL HAVE WITH YOUR GUN.\n")
        print("")
        print("AT EACH TURN, ALL ITEMS ARE SHOWN IN DOLLAR AMOUNTS")
        print("EXCEPT BULLETS")
        print("WHEN ASKED TO ENTER MONEY AMOUNTS, DON'T USE A \"$\".")
        print("GOOD LUCK!\n\n")

    # Lines 700- X1, K5, S4, F1, F2, M, M9, D3
    def initial_setup(self):
        prompt = "HOW GOOD A SHOT ARE YOU WITH YOUR RIFLE?"
        prompt += "\n  (1) ACE MARKSMAN, (2) GOOD SHOT, (3) FAIR TO MIDDLIN'"
        prompt += "\n  (4) NEED MORE PRACTICE, (5) SHAKY KNEES>\n"
        shooting_skill = input(prompt)
        cash = 700
 
        prompt = "HOW MUCH DO YOU WANT TO SPEND ON YOUR OXEN TEAM?  >"
        oxen = get_user_input(prompt, self.MIN_OXEN_AMOUNT, self.MAX_OXEN_AMOUNT)
        cash = cash - oxen
 
        prompt = "HOW MUCH DO YOU WANT TO SPEND ON FOOD?  >"
        food = get_user_input(prompt, 0, cash)
        cash = cash - food

        prompt = "HOW MUCH DO YOU WANT TO SPEND ON AMMUNITION?  >"
        ammo = get_user_input(prompt, 0, cash)
        cash = cash - ammo

        prompt = "HOW MUCH DO YOU WANT TO SPEND ON CLOTHING?  >"
        clothing = get_user_input(prompt, 0, cash)
        cash = cash - clothing

        prompt = "HOW MUCH DO YOU WANT TO SPEND ON MISCELLANEOUS SUPPLIES?  >"
        misc = get_user_input(prompt, 0, cash)
        self.traveller = Traveller(shooting_skill, oxen, food, ammo, clothing, misc, cash)
        print(f"AFTER ALL YOUR PURCHASES, YOU NOW HAVE ${cash} LEFT.")
        print("\nMONDAY MARCH 29 1847")


    def conclusion(self):
        print("CONGRATULATIONS! YOU'VE MADE IT TO OREGON CITY!")

    def do_final_turn(self):
        print("YOU HAVE BEEN ON THE TRAIL TOO LONG ------")
        print("YOUR FAMILY DIES IN THE FIRST BLIZZARD OF WINTER")

    def is_final_turn(self, miles, max_miles):
        if miles >= max_miles:
            self.do_final_turn()

    def get_date(self, current_turn):
        if self.miles >= self.MAX_MILES:
            self.do_final_turn()
            return
        if current_turn < len(self.dates):
            print(f"\n{weekdays[0]} {dates[current_turn]} 1847")


    def request_action(self):
        if self.fort_exists:
            while True:
                prompt = "DO YOU WANT TO (1) STOP AT THE NEXT FORT, (2) HUNT,"
                prompt += "\n (3) CONTINUE"
                action = get_user_input(prompt, 1, 3)
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
                action = get_user_input(prompt, 1, 2)
                if action == 1:
                    result = self.traveller.hunt()
                    if result:
                        break 
                else:
                    self.traveller.travel()

    def handle_turn(self):
        if not self.traveller.check():
            return False
        if not self.sth_pass_miles:
            print(f"TOTAL MILEAGE IS {self.miles}")
        else:
            print("TOTAL MILEAGE IS 950")
            self.south_pass_flag_updated_mileage = False
        self.traveller.show_stats()
        if not self.request_action():
            return False
        return True

    def handle_death(self):
        print("DUE TO YOUR UNFORTUNATE SITUATION, THERE ARE FEW")
        print("FORMALITIES WE MUST GO THROUGH")
        question = "\nWOULD YOU LIKE A MINISTER?"
        answer = input(question)
        question = "\nWOULD YOU LIKE A FANCY FUNERAL?"
        answer = input(question)
        question = "\nWOULD YOU LIKE US TO INFORM YOUR NEXT OF KIN?"
        answer = input(question)
        if answer == "NO":
            print("BUT YOUR AUNT SADIE IN ST. LOUIS IS REALLY WORRIED ABOUT YOU")
        else:
            print("THAT WILL BE $50 FOR THE TELEGRAPH CHARGE.")
        print("WE THANK YOU FOR THIS INFORMATION AND WE ARE SORRY YOU")
        print("DIDN'T MAKE IT TO THE GREAT TERRITORY OF OREGON")
        print("BETTER LUCK NEXT TIME")
        print("")
        print(tab(30) + "SINCERELY")
        print(tab(17) + "THE OREGON CITY CHAMBER OF COMMERCE")

