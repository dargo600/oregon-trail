from dataclasses import dataclass
from classes.ui import UI
from classes.utils import tab


@dataclass
class TerminalUI(UI):
    """ Class for handling Terminal UI input and output """
    MAX_MILES: int = 2040

    def display(self, output_string: str) -> None:
        """ Display output_string """
        print(output_string)

    # BASIC gen_zoning
    # 2040 PRINT "FOOD","BULLETS","CLOTHING","MISC. SUPP.","CASH"
    # https://archive.org/details/bitsavers_cdccyberlaBASICOct80_41102953/page/n85/mode/2up
    def gen_zoning(print_list) -> None:
        """
        Mimick print_zoning function from BASIC
        """
        for item in print_list:
            padded_item = str(item).ljust(15)
            print(f"{padded_item}", end="")
        print("")

    # https://archive.org/details/bitsavers_cdccyberlaBASICOct80_41102953/page/n85/mode/2up?q=TAB
    def tab(self, count) -> str:
        """
        Mimick TAB function from BASIC
        """
        return " " * count

    def get_user_input(self, prompt, min_value, max_value) -> int:
        """
        Check value and prompt for a new value if not in range
        of min_value and max_value
        """
        while True:
            val = int(input(prompt))
            if min_value <= val and val <= max_value:
                break
            print(f"INVALID INPUT.  PLEASE ENTER A VALUE BETWEEN {min_value} and {max_value}\n")
        return val

    def handle_death(self) -> None:
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


