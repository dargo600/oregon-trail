Based on:

https://github.com/clintmoyer/oregon-trail/tree/master/refactor

The variables that were used have been updated to be more descriptive:

```
6470 REM ***IDENTIFICATION OF VARIABLES IN THE PROGRAM***
t.oxen              6480 REM A = AMOUNT SPENT ON ANIMALS
t.ammo              6490 REM B = AMOUNT SPENT ON AMMUNITION
g.response          6500 REM B1 = ACTUAL RESPONSE TIME FOR INPUTTING "BANG"
g.start             6510 REM B3 = CLOCK TIME AT START OF INPUTTING "BANG"
t.clothes           6520 REM C = AMOUNT SPENT ON CLOTHING
t.need_clothes      6530 REM C1 = FLAG FOR INSUFFICIENT CLOTHING IN COLD WEATHER
                    6540 REM C$ = YES/NO RESPONSE TO QUESTIONS
                    6550 REM D1 = COUNTER IN GENERATING EVENTS
g.turn_number       6560 REM D3 = TURN NUMBER FOR SETTING DATE
                    6570 REM D4 = CURRENT DATE
t.gun_skill         6580 REM D9 = CHOICE OF SHOOTING EXPERTISE LEVEL
                    6590 REM E = CHOICE OF EATING
t.food              6600 REM F = AMOUNT SPENT ON FOOD
t.done_sth_pass     6610 REM F1 = FLAG FOR CLEARING SOUTH PASS
t.done_blue_mnts    6620 REM F2 = FLAG FOR CLEARING BLUE MOUNTAINS
                    6630 REM F9 = FRACTION OF 2 WEEKS TRAVELED ON FINAL TURN
t.injury            6640 REM K8 = FLAG FOR INJURY
                    6650 REM L1 = FLAG FOR BLIZZARD
g.miles             6660 REM M = TOTAL MILEAGE WHOLE TRIP
t.misc              6670 REM M1 = AMOUNT SPENT ON MISCELLANEOUS SUPPLIES
g.prev_turn_miles   6680 REM M2 = TOTAL MILEAGE UP THROUGH PREVIOUS TURN
g.sth_pass_miles    6690 REM M9 = FLAG FOR CLEARING SOUTH PASS IN SETTING MILEAGE
                    6700 REM P = AMOUNT SPENT ON ITEMS AT FORT
                    6710 REM R1 = RANDOM NUMBER IN CHOOSING EVENTS
t.sick              6720 REM S4 = FLAG FOR ILLNESS
                    6730 REM S5 = ""HOSTILITY OF RIDERS"" FACTOR
                    6740 REM S6 = SHOOTING WORD SELECTOR
                    6750 REM S$ = VARIATIONS OF SHOOTING WORD
                    6760 REM T = CASH LEFT OVER AFTER INITIAL PURCHASES
                    6770 REM T1 = CHOICE OF TACTICES WHEN ATTACKED
                    6780 REM X = CHOICE OF ACTION FOR EACH TURN
                    6790 REM X1 = FLAG FOR FORT OPTION
```