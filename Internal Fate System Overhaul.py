from collections import namedtuple
from random import *
from tkinter import *


class IFS:
    def __init__(self, spin=None, pc=None, attribute=None, skill=None, difficulty=None, enemy=None, target=None,
                 condition=None):

        global Ho, Kinzin, Mignon, Raven, Sev, Vampyrate, name, hp, ac, ap, fortitude, will, reflex, charisma, \
            constitution, dexterity, intelligence, luck, speed, strength, wisdom, disguise, enlightenment, \
            interaction, heavy_armor, acrobatics, escape, ranged, ride, sleight_of_hand, stealth, chemistry, \
            craft, engineer, knowledge, security, sense_motive, block, light_armor, athletics, melee, unarmed, \
            control, destruction, enhancement, medicine, perception, survival, utility, Easy, Standard, Hard

        self.Easy = 8
        self.Standard = 12
        self.Hard = 16

        self.Character = namedtuple("Character", "name hp ac ap fortitude will reflex charisma constitution dexterity "
                                                 "intelligence luck speed strength wisdom")

        self.Enemy = namedtuple("Enemy", "name hp ac ap fortitude will reflex charisma constitution dexterity "
                                         "intelligence luck speed strength wisdom")

        self.Ho = self.Character("Ho", 30, 9, 4, 12, 13, 11, 20, 20, 10, 30, 20, 10, 20, 30)
        self.Kinzin = self.Character("Kinzin", 45, 18, 4, 13, 12, 8, 10, 30, 20, 20, 10, 20, 30, 20)
        self.Mignon = self.Character("Mignon", 30, 12, 4, 12, 13, 13, 10, 20, 30, 20, 10, 20, 20, 30)
        self.Raven = self.Character("Raven", 15, 12, 4, 11, 12, 13, 20, 10, 30, 10, 20, 20, 30, 20)
        self.Sev = self.Character("Sev", 30, 11, 4, 12, 13, 12, 30, 20, 10, 20, 10, 20, 20, 30)
        self.Vampyrate = self.Enemy("Vampyrate", 15, 13, 4, 11, 11, 14, 15, 10, 40, 20, 30, 20, 10, 10)

        # Global references

        Easy = self.Easy
        Standard = self.Standard
        Hard = self.Hard

        Ho = self.Ho
        Kinzin = self.Kinzin
        Mignon = self.Mignon
        Raven = self.Raven
        Sev = self.Sev
        Vampyrate = self.Vampyrate

        name = 0
        hp = 1
        ac = 2
        ap = 3
        fortitude = 4
        will = 5
        reflex = 6
        charisma = 7        # Disguise, Enlightenment, Interaction
        constitution = 8    # Heavy Armor
        dexterity = 9       # Acrobatics, Escape, Ranged, Ride, Sleight of Hand, Stealth
        intelligence = 10   # Chemistry, Craft, Engineer, Knowledge, Security, Sense Motive
        luck = 11
        speed = 12          # Block, Light Armor
        strength = 13       # Athletics, Melee, Unarmed
        wisdom = 14         # Control, Destruction, Enhancement, Medicine, Perception, Survival, Utility

        disguise = "Disguise"
        enlightenment = "Enlightenment"
        interaction = "Interaction"
        heavy_armor = "Heavy Armor"
        acrobatics = "Acrobatics"
        escape = "Escape"
        ranged = "Ranged"
        ride = "Ride"
        sleight_of_hand = "Sleight of Hand"
        stealth = "Stealth"
        chemistry = "Chemistry"
        craft = "Craft"
        engineer = "Engineer"
        knowledge = "Knowledge"
        security = "Security"
        sense_motive = "Sense Motive"
        block = "Block"
        light_armor = "Light Armor"
        athletics = "Athletics"
        melee = "Melee"
        unarmed = "Unarmed"
        control = "Control"
        destruction = "Destruction"
        enhancement = "Enhancement"
        medicine = "Medicine"
        perception = "Perception"
        survival = "Survival"
        utility = "Utility"

        # Function variable setting (Find a more efficient way of doing this!)

        self.spin = spin
        self.pc = pc
        self.attribute = attribute
        self.skill = skill
        self.difficulty = difficulty
        self.enemy = enemy
        self.target = target
        self.condition = condition

    def wheel_of_fate(self):
        self.spin = randint(1, 5)
        print(self.spin)
        return self.spin

    # get_attribute() returns the specified value from the called namedtuple (in this case a Character or Enemy)

    def get_attribute(self, pc, attribute):
        self.pc = pc
        self.attribute = attribute
        chosen_attribute = pc[attribute]
        return chosen_attribute

    # skill_challenge() is the main function for skill checks

    # Summoning the Improvised Damage System (IDS)

    def dmg_challenge(self, target, enemy, condition=None):

        high = "High"
        medium = "Medium"
        low = "Low"

        self.target = target
        self.enemy = enemy
        self.condition = condition

        def dmg(level):
            if level == "High":
                dmg_outcome = randint(1, 8)
                return dmg_outcome
            elif level == "Medium":
                dmg_outcome = randint(1, 6)
                return dmg_outcome
            elif level == "Low":
                dmg_outcome = randint(1, 4)
                return dmg_outcome
            else:
                return None

        decider = randint(1, 20)

        if decider >= target[2]:

            if enemy[3] == 4:
                dmg_points = dmg(low)

                if condition == "Partial":
                    dmg_points = dmg_points - 2
                    if dmg_points <= 0:
                        print("Attack is unsuccessful!")
                        return None
                    else:
                        print("The attack by", enemy[0], "is successful!", target[0], "lost", dmg_points, "HP(s)!")
                        return dmg_points

                elif condition == "Concealed":
                    dmg_points = dmg_points - 5
                    if dmg_points <= 0:
                        print("Attack is unsuccessful!")
                        return None
                    else:
                        print("The attack by", enemy[0], "is successful!", target[0], "lost", dmg_points, "HP(s)!")
                        return dmg_points

                else:
                    print("The attack by", enemy[0], "is successful!", target[0], "lost", dmg_points, "HP(s)!")
                    return dmg_points

            elif enemy[3] == 6:
                dmg_points = dmg(medium)

                if condition == "Partial":
                    dmg_points = dmg_points - 2
                    if dmg_points <= 0:
                        print("Attack is unsuccessful!")
                        return None
                    else:
                        print("The attack by", enemy[0], "is successful!", target[0], "lost", dmg_points, "HP(s)!")
                        return dmg_points

                elif condition == "Concealed":
                    dmg_points = dmg_points - 5
                    if dmg_points <= 0:
                        print("Attack is unsuccessful!")
                        return None
                    else:
                        print("The attack by", enemy[0], "is successful!", target[0], "lost", dmg_points, "HP(s)!")
                        return dmg_points

                else:
                    print("The attack by", enemy[0], "is successful!", target[0], "lost", dmg_points, "HP(s)!")
                    return dmg_points

            elif enemy[3] == 8:
                dmg_points = dmg(high)

                if condition == "Partial":
                    dmg_points = dmg_points - 2
                    if dmg_points <= 0:
                        print("Attack is unsuccessful!")
                        return None
                    else:
                        print("The attack by", enemy[0], "is successful!", target[0], "lost", dmg_points, "HP(s)!")
                        return dmg_points

                elif condition == "Concealed":
                    dmg_points = dmg_points - 5
                    if dmg_points <= 0:
                        print("Attack is unsuccessful!")
                        return None
                    else:
                        print("The attack by", enemy[0], "is successful!", target[0], "lost", dmg_points, "HP(s)!")
                        return dmg_points

                else:
                    print("The attack by", enemy[0], "is successful!", target[0], "lost", dmg_points, "HP(s)!")
                    return dmg_points

        else:
            print("Attack is unsuccessful!")
            return None

    # Yuri's Trauma Triage

    def heal(self, healer, injured):

        skill_check = randint(1, 25)
        healer_fortitude = int(healer[14] / 10)
        injured_hp = injured[1]

        def fluke_system():
            roll_one = randint(-1000, 1000)
            if roll_one <= -850:
                fluke = "Unlucky"

            elif roll_one >= 1850:
                fluke = "Lucky"

            else:
                fluke = None

            return fluke

        if skill_check >= injured[4]:
            additional_hp = randint(1, 4)
            hp_back = int(additional_hp) * int(healer_fortitude)
            new_injured_hp = hp_back + injured_hp

            print(healer[0], "healed", injured[0], "for", hp_back, "HPs!")

            return skill_check, new_injured_hp

        else:
            healers_luck = fluke_system()
            if healers_luck == "Unlucky":
                print("Skill check failed! An unlucky encounter.")
                return healers_luck
            else:
                print(healer[0], "failed the skill check!")
                return None

    # TGG MAINFRAME
    # CODE MONKEY'S REMINDER: New widget, new frame!

    def tgg_mainframe(self):

        gui = Tk()
        gui.title("Internal Fate System")

        challenge_var = IntVar()
        challenge_var.set(None)

        skill_frame = Frame(gui)
        skill_frame.grid()

        Label(skill_frame, text="Internal Fate System").grid(row=0, pady=3, columnspan=3, sticky='n')

        second_frame = Frame(skill_frame)
        sc_frame = Frame(skill_frame)

        def skill_challenge_page():

            for widget in sc_frame.winfo_children():  # calls a list of all the existing widgets in the frame
                widget.destroy()  # in order to clear them out for new widgets to populate

            svariable = StringVar()
            svariable.set("Select a Skill")  # sets the default value of the option menu

            cvariable = StringVar()
            cvariable.set("Select a PC")

            dvariable = StringVar()
            dvariable.set("Select Difficulty")

            rvariable = StringVar()
            rvariable.set("The gods will decide...")

            def skill_challenge(pc, skill, difficulty):
                if skill == "Acrobatics":
                    skill_value = 9
                elif skill == "Athletics":
                    skill_value = 13
                elif skill == "Block":
                    skill_value = 12
                elif skill == "Chemistry":
                    skill_value = 10
                elif skill == "Control":
                    skill_value = 14
                elif skill == "Craft":
                    skill_value = 10
                elif skill == "Destruction":
                    skill_value = 14
                elif skill == "Disguise":
                    skill_value = 7
                elif skill == "Engineering":
                    skill_value = 10
                elif skill == "Enhancement":
                    skill_value = 14
                elif skill == "Enlightenment":
                    skill_value = 7
                elif skill == "Escape":
                    skill_value = 9
                elif skill == "Heavy Armor":
                    skill_value = 8
                elif skill == "Interaction":
                    skill_value = 7
                elif skill == "Knowledge":
                    skill_value = 10
                elif skill == "Light Armor":
                    skill_value = 12
                elif skill == "Medicine":
                    skill_value = 14
                elif skill == "Melee":
                    skill_value = 13
                elif skill == "Perception":
                    skill_value = 14
                elif skill == "Ranged":
                    skill_value = 9
                elif skill == "Ride":
                    skill_value = 9
                elif skill == "Security":
                    skill_value = 10
                elif skill == "Sense Motive":
                    skill_value = 10
                elif skill == "Sleight of Hand":
                    skill_value = 9
                elif skill == "Stealth":
                    skill_value = 9
                elif skill == "Survival":
                    skill_value = 14
                elif skill == "Unarmed":
                    skill_value = 13
                elif skill == "Utility":
                    skill_value = 14
                else:
                    skill_value = "Skill Not Found"

                if difficulty == 8:
                    diff = "Easy"
                elif difficulty == 12:
                    diff = "Standard"
                elif difficulty == 16:
                    diff = "Hard"
                else:
                    diff = None

                def get_skill_modifier(chosen_pc, sv, chosen_skill):
                    return_skill = int(chosen_pc[sv])
                    skill_modifier = int(return_skill / 10)

                    if chosen_pc == Kinzin and chosen_skill == "Acrobatics" \
                            or chosen_pc == Kinzin and chosen_skill == "Control" \
                            or chosen_pc == Kinzin and chosen_skill == "Destruction" \
                            or chosen_pc == Kinzin and chosen_skill == "Enhancement" \
                            or chosen_pc == Kinzin and chosen_skill == "Escape" \
                            or chosen_pc == Kinzin and chosen_skill == "Sleight of Hand" \
                            or chosen_pc == Kinzin and chosen_skill == "Stealth" \
                            or chosen_pc == Kinzin and chosen_skill == "Utility":

                        skill_modifier = int(skill_modifier) - 7
                        return skill_modifier

                    elif chosen_pc == Sev and chosen_skill == "Acrobatics":
                        skill_modifier = int(skill_modifier) - 1
                        return skill_modifier

                    elif chosen_pc == Ho and chosen_skill == "Stealth":
                        skill_modifier = int(skill_modifier) - 5
                        return skill_modifier

                    elif chosen_pc == Vampyrate and chosen_skill == "Stealth":
                        skill_modifier = int(skill_modifier) + 5
                        return skill_modifier

                    else:
                        return skill_modifier

                def get_luck_modifier(chosen_pc):
                    mod = int(chosen_pc[11])
                    luck_mod = int(mod / 10)
                    return luck_mod

                def fluke_system():
                    roll_one = randint(-1000, 1000)
                    if roll_one <= -850:
                        fluke = "Unlucky"

                    elif roll_one >= 1850:
                        fluke = "Lucky"

                    else:
                        fluke = None

                    return fluke

                the_skill_modifier = get_skill_modifier(pc, skill_value, skill)
                luck_modifier = get_luck_modifier(pc)
                outcome_1 = int(randint(1, 15))
                outcome = outcome_1 + luck_modifier + the_skill_modifier

                if outcome >= difficulty:
                    p1 = str(pc[0])
                    p2 = " passed the "
                    p3 = skill
                    p4 = " check!"
                    message = p1 + p2 + p3 + p4  # stores outcome value to be retrieved later for SQL storage
                    check_for_fluke = fluke_system()
                    if check_for_fluke != "Lucky":
                        check_for_fluke = None
                    else:
                        print("Lucky encounter!")

                elif outcome < difficulty:
                    p1 = str(pc[0])
                    p2 = " failed the "
                    p3 = skill
                    p4 = " check..."
                    message = p1 + p2 + p3 + p4
                    diff = "Failed"
                    check_for_fluke = fluke_system()
                    if check_for_fluke != "Unlucky":
                        check_for_fluke = None
                    else:
                        print("Unlucky encounter!")

                else:
                    return None

                return outcome, skill, diff, check_for_fluke, message

            def get_pc():
                selected_pc = cvariable.get()
                if selected_pc == "Ho":
                    selected_pc = Ho

                elif selected_pc == "Kinzin":
                    selected_pc = Kinzin

                elif selected_pc == "Mignon":
                    selected_pc = Mignon

                elif selected_pc == "Raven":
                    selected_pc = Raven

                elif selected_pc == "Sev":
                    selected_pc = Sev

                else:
                    print("PC not found.")

                return selected_pc

            def get_skill():
                selected_skill = svariable.get()
                if selected_skill == "Acrobatics":
                    selected_skill = acrobatics
                elif selected_skill == "Athletics":
                    selected_skill = athletics
                elif selected_skill == "Block":
                    selected_skill = block
                elif selected_skill == "Chemistry":
                    selected_skill = chemistry
                elif selected_skill == "Control":
                    selected_skill = control
                elif selected_skill == "Craft":
                    selected_skill = craft
                elif selected_skill == "Destruction":
                    selected_skill = destruction
                elif selected_skill == "Disguise":
                    selected_skill = disguise
                elif selected_skill == "Engineering":
                    selected_skill = engineer
                elif selected_skill == "Enhancement":
                    selected_skill = enhancement
                elif selected_skill == "Enlightenment":
                    selected_skill = enlightenment
                elif selected_skill == "Escape":
                    selected_skill = escape
                elif selected_skill == "Heavy Armor":
                    selected_skill = heavy_armor
                elif selected_skill == "Interaction":
                    selected_skill = interaction
                elif selected_skill == "Knowledge":
                    selected_skill = knowledge
                elif selected_skill == "Light Armor":
                    selected_skill = light_armor
                elif selected_skill == "Medicine":
                    selected_skill = medicine
                elif selected_skill == "Melee":
                    selected_skill = melee
                elif selected_skill == "Perception":
                    selected_skill = perception
                elif selected_skill == "Ranged":
                    selected_skill = ranged
                elif selected_skill == "Ride":
                    selected_skill = ride
                elif selected_skill == "Security":
                    selected_skill = security
                elif selected_skill == "Sense Motive":
                    selected_skill = sense_motive
                elif selected_skill == "Sleight of Hand":
                    selected_skill = sleight_of_hand
                elif selected_skill == "Stealth":
                    selected_skill = stealth
                elif selected_skill == "Survival":
                    selected_skill = survival
                elif selected_skill == "Unarmed":
                    selected_skill = unarmed
                else:
                    print("Skill not found.")
                return selected_skill

            def get_diff():
                selected_diff = dvariable.get()
                if selected_diff == "Easy":
                    selected_diff = Easy

                elif selected_diff == "Hard":
                    selected_diff = Hard

                elif selected_diff == "Standard":
                    selected_diff = Standard

                else:
                    print("Difficulty not found.")

                return selected_diff

            def roll_the_die():
                rtd_pc = get_pc()
                rtd_skill = get_skill()
                rtd_diff = get_diff()

                result = skill_challenge(rtd_pc, rtd_skill, rtd_diff)
                gui_message = result[4]  # grabs the string to be presented at the bottom of the card

                rvariable.set(gui_message)
                return result

            sc_frame.grid()

            skill_dropdown = OptionMenu(sc_frame, svariable, "Acrobatics", "Athletics", "Block", "Chemistry",
                                        "Control", "Craft", "Destruction", "Disguise", "Engineering", "Enhancement",
                                        "Enlightenment", "Escape", "Heavy Armor", "Interaction", "Knowledge",
                                        "Light Armor", "Medicine", "Melee", "Perception", "Ranged", "Ride", "Security",
                                        "Sense Motive", "Sleight of Hand", "Stealth", "Survival", "Unarmed")

            skill_dropdown.grid(row=2, column=1)

            pc_dropdown = OptionMenu(sc_frame, cvariable, "Ho", "Kinzin", "Mignon", "Raven", "Sev")
            pc_dropdown.grid(row=2, column=0)

            diff_dropdown = OptionMenu(sc_frame, dvariable, "Easy", "Standard", "Hard")
            diff_dropdown.grid(row=2, column=2)

            sc_card_frame = Frame(sc_frame)
            sc_card_frame.grid(row=4, columnspan=3)

            skill_chall_label = Label(sc_card_frame, text="Skill Challenge")
            skill_chall_label.grid(row=3, columnspan=3, pady=2)

            photo = PhotoImage(file="TarotCard.png")

            skill_chall_card = Label(sc_card_frame, image=photo, width=370, height=300)
            skill_chall_card.photo = photo
            skill_chall_card.grid(row=4)

            roll_result = Entry(sc_card_frame, width=37, state="readonly", textvariable=rvariable)
            roll_result.grid(row=5, pady=7)

            roll_die = Button(sc_card_frame, text="Roll the die!", command=roll_the_die)
            roll_die.grid(row=6, columnspan=3, sticky='n', pady=4)

        second_frame.grid()

        skill_challenge_button = Radiobutton(second_frame, text="Skill Challenge", value=1, variable=challenge_var,
                                             command=skill_challenge_page)

        skill_challenge_button.grid(row=1, column=0)

        dps_challenge_button = Radiobutton(second_frame, text="Combat Challenge", value=2, variable=challenge_var)
        dps_challenge_button.grid(row=1, column=1)

        heal_challenge_button = Radiobutton(second_frame, text="Heal Challenge", value=3, variable=challenge_var)
        heal_challenge_button.grid(row=1, column=2)

        gui.mainloop()


RNG = IFS()
RNG.tgg_mainframe()
