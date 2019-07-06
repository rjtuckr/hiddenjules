from collections import namedtuple
from random import *
from tkinter import *


class IFS:
    def __init__(self, spin=None, fluke=None, pc=None, attribute=None, skill=None, difficulty=None):

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
        self.fluke = fluke
        self.pc = pc
        self.attribute = attribute
        self.skill = skill
        self.difficulty = difficulty

    def wheel_of_fate(self):
        self.spin = randint(1, 5)
        print(self.spin)
        return self.spin

    def get_attribute(self, pc, attribute):
        self.pc = pc
        self.attribute = attribute
        chosen_attribute = pc[attribute]
        return chosen_attribute

    def skill_challenge(self, pc, skill, difficulty):
        self.pc = pc
        self.skill = skill
        self.difficulty = difficulty

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

        def get_skill(chosen_pc, sv, chosen_skill):
            return_skill = int(chosen_pc[sv])
            skill_modifier = int(return_skill / 10)

            if chosen_pc == Kinzin and chosen_skill == "Acrobatics" \
                    or chosen_pc == Kinzin and chosen_skill == "Control"\
                    or chosen_pc == Kinzin and chosen_skill == "Destruction"\
                    or chosen_pc == Kinzin and chosen_skill == "Enhancement"\
                    or chosen_pc == Kinzin and chosen_skill == "Escape"\
                    or chosen_pc == Kinzin and chosen_skill == "Sleight of Hand"\
                    or chosen_pc == Kinzin and chosen_skill == "Stealth"\
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

        the_skill_modifier = get_skill(pc, skill_value, skill)
        luck_modifier = get_luck_modifier(pc)
        outcome_1 = int(randint(1, 15))
        outcome = outcome_1 + luck_modifier + the_skill_modifier

        print("The total outcome of the roll is", outcome)

        if outcome >= difficulty:
            p1 = str(pc[0])
            p2 = " passed the "
            p3 = skill
            p4 = " check!"
            message = p1 + p2 + p3 + p4  # stores outcome value to be retrieved later for SQL storage
            check_for_fluke = fluke_system()
            if check_for_fluke != "Lucky":
                check_for_fluke = None

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
            return None

        print(message)
        return outcome, skill, diff, check_for_fluke, message


rng = IFS()
rng.skill_challenge(Ho, acrobatics, Easy)
