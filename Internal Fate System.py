from collections import namedtuple
from random import *
from tkinter import *

# Written by Julie Tucker
# rjtuckr@outlook.com

# Attributes
# Charisma (CH)
# Constitution (CON)
# Dexterity (DEX)
# Intelligence (INT)
# Luck (LCK)
# Speed (SPD)
# Strength (STR)
# Wisdom (WIS)


# Skills
# Acrobatics (DEX)
# Athletics (STR)
# Block (SPD)
# Chemistry (INT)
# Control (WIS)
# Craft (INT)
# Destruction (WIS)
# Disguise (CHA)
# Engineering (INT)
# Enhancement (WIS)
# Enlightenment (CHA)
# Escape (DEX)
# Heavy Armor (CON)
# Interaction (CHA)
# Knowledge (INT)
# Light Armor (SPD)
# Medicine (WIS)
# Melee (STR)
# Perception (WIS)
# Ranged (DEX)
# Ride/Drive (DEX)
# Security (INT)
# Sense Motive (WIS)
# Sleight of Hand (DEX)
# Stealth (DEX)
# Survival (WIS)


Character = namedtuple("Character", "name hp ac ap fortitude will reflex charisma constitution dexterity intelligence \
                                    luck speed strength wisdom")

Enemy = namedtuple("Enemy", "name hp ac ap fortitude will reflex charisma constitution dexterity intelligence \
                                    luck speed strength wisdom")


# hp = 1.5 x pc.constitution (score)

# light armor AC = 7 + pc.speed (or pc.dexterity) + getLightArmor(pc) (mod)
# heavy armor AC = 12 + getHeavyArmor(pc) + pc.constitution (mod)

# fortitude = 10 + pc.constitution (mod)
# will = 10 + pc.wisdom (mod)

# light armor reflex = 10 + pc.speed (or pc.dexterity) (mod)
# heavy armor reflex = 5 + pc.speed (or pc.dexterity) + (getHeavyArmor(pc) * .5) (mod)

# ap, or attack power, is d4 by default


# PCs
Ho = Character("Ho", 30, 9, 4, 12, 13, 11, 20, 20, 10, 30, 20, 10, 20, 30)
Kinzin = Character("Kinzin", 45, 18, 4, 13, 12, 8, 10, 30, 20, 20, 10, 20, 30, 20)
Mignon = Character("Mignon", 30, 12, 4, 12, 13, 13, 10, 20, 30, 20, 10, 20, 20, 30)
Raven = Character("Raven", 15, 12, 4, 11, 12, 13, 20, 10, 30, 10, 20, 20, 30, 20)
Sev = Character("Sev", 30, 11, 4, 12, 13, 12, 30, 20, 10, 20, 10, 20, 20, 30)


# "name hp ac ap fortitude will reflex charisma constitution dexterity intelligence luck speed strength wisdom"
# Enemy NPCs
Vampyrate = Enemy("Vampyrate", 15, 13, 4, 11, 11, 14, 15, 10, 40, 20, 30, 20, 10, 10)


# Inventory of PCs
Ho_Inventory = (95, "A Gourd of Sake", "Paintbrush", "Black Ink", "Abacus", "First Aid Kit", "Hearthstone")
Kinzin_Inventory = (148, "Holy-imbued Shield", "Sword", "Map of Azeroth", "Gnomish Army Knife", "Hearthstone")
Mignon_Inventory = (79, "Totem-drum", "Rope", "Skinning Knife", "Hatchet", "Hearthstone")
Raven_Inventory = (145, "Tunestone", "Bundle of Bloodthistle", "Spyglass", "Dagger", "Hearthstone")
Sev_Inventory = (160, "Handcrafted Whip", "Gonk's Staff", "Bottle of Junglevine Wine", "Voodoo Doll", "Hearthstone")

# Ho's Inventory
# [0] Gold pieces
# [1] A Gourd of Sake
# [2] Paintbrush
# [3] Black Ink
# [4] Abacus
# [5] First Aid Kit
# [6] Hearthstone

# Kinzin's Inventory
# [0] Gold pieces
# [1] Holy-imbued Shield
# [2] Sword
# [3] Map of Azeroth
# [4] Gnomish Army Knife
# [5] Hearthstone

# Mignon's Inventory
# [0] Gold pieces
# [1] Totem-drum
# [2] Rope
# [3] Skinning Knife
# [4] Hatchet
# [5] Hearthstone

# Raven's Inventory
# [0] Gold pieces
# [1] Tunestone
# [2] Bundle of Bloodthistle
# [3] Spyglass
# [4] Dagger
# [5] Hearthstone

# Sev's Inventory
# [0] Gold pieces
# [1] Hand-crafted Whip
# [2] Gonk's Staff
# [3] Bottle of Junglevine Wine
# [4] Voodoo Doll
# [5] Hearthstone


# Skill Challenges
Easy = 8
Standard = 12
Hard = 16

# Fate's Wheel of Fate

# Ho - 1
# Kinzin - 2
# Mignon - 3
# Raven - 4
# Sev - 5


def wheel_of_fate():
    spin = randint(1, 5)
    print(spin)
    return spin


#  Gonk's Fluke System
#  Gives each skill challenge a 15% chance for a lucky or unlucky chance encounter


def fluke_system():
    roll_one = randint(-1000, 1000)

    if roll_one <= -850:

        fluke = "Unlucky"

    elif roll_one >= 1850:

        fluke = "Lucky"

    else:

        fluke = None

    return fluke


def get_hp(pc):
    return pc.hp


def get_name(pc):
    return pc.name


def get_charisma(pc):
    return pc.charisma


def get_const(pc):
    return pc.constitution


def get_dexterity(pc):
    return pc.dexterity


def get_intelli(pc):
    return pc.intelligence


def get_luck(pc):
    return pc.luck


def get_luckmod(pc):
    mod_1 = int(pc.luck)
    luck_mod = int(mod_1 / 10)
    return luck_mod


def get_speed(pc):
    return pc.speed


def get_strength(pc):
    return pc.strength


def get_wisdom(pc):
    return pc.wisdom


def get_acrobatics(pc):
    acro = int(pc.dexterity)
    acrobatics = int(acro / 10)
    return acrobatics


def get_athletics(pc):
    ath = int(pc.strength)
    athletics = int(ath / 10)
    return athletics


def get_block(pc):
    bl = int(pc.speed)
    blocks = int(bl / 10)
    return blocks


def get_chemistry(pc):
    chem = int(pc.intelligence)
    chemistries = int(chem / 10)
    return chemistries


def get_control(pc):
    con = int(pc.wisdom)
    controls = int(con / 10)
    return controls


def get_craft(pc):
    cra = int(pc.intelligence)
    crafts = int(cra / 10)
    return crafts


def get_destruct(pc):
    destruct = int(pc.wisdom)
    destructions = int(destruct / 10)
    return destructions


def get_disguise(pc):
    dis = int(pc.charisma)
    disguises = int(dis / 10)
    return disguises


def get_engineer(pc):
    eng = int(pc.intelligence)
    engineerings = int(eng / 10)
    return engineerings


def get_enhance(pc):
    enhance = int(pc.wisdom)
    enhancements = int(enhance / 10)
    return enhancements


def get_enlight(pc):
    enlight = int(pc.charisma)
    enlightenments = int(enlight / 10)
    return enlightenments


def get_escape(pc):
    esc = int(pc.dexterity)
    escapes = int(esc / 10)
    return escapes


def get_heavyarmor(pc):
    heavy = int(pc.constitution)
    heavy_armors = int(heavy / 10)
    return heavy_armors


def get_interaction(pc):
    inter = int(pc.charisma)
    interactions = int(inter / 10)
    return interactions


def get_knowledge(pc):
    know = int(pc.intelligence)
    knowledges = int(know / 10)
    return knowledges


def get_lightarmor(pc):
    light = int(pc.speed)
    light_armors = int(light / 10)
    return light_armors


def get_medicine(pc):
    med = int(pc.wisdom)
    medicines = int(med / 10)
    return medicines


def get_melee(pc):
    me = int(pc.strength)
    melees = int(me / 10)
    return melees


def get_perception(pc):
    percep = int(pc.wisdom)
    perceptions = int(percep / 10)
    return perceptions


def get_ranged(pc):
    rang = int(pc.dexterity)
    ranger = int(rang / 10)
    return ranger


def get_ride(pc):
    rid = int(pc.dexterity)
    rider = int(rid / 10)
    return rider


def get_security(pc):
    secur = int(pc.intelligence)
    secure = int(secur / 10)
    return secure


def get_sensemotive(pc):
    sense = int(pc.intelligence)
    sense_mo = int(sense / 10)
    return sense_mo


def get_sleight(pc):
    slei = int(pc.dexterity)
    sleight = int(slei / 10)
    return sleight


def get_stealth(pc):
    stea = int(pc.dexterity)
    stealthy = int(stea / 10)
    return stealthy


def get_survival(pc):
    sur = int(pc.wisdom)
    survive = int(sur / 10)
    return survive


def get_unarmed(pc):
    unarm = int(pc.strength)
    unarmed_combat = int(unarm / 10)
    return unarmed_combat


def get_utility(pc):
    util = int(pc.wisdom)
    utilities = int(util / 10)
    return utilities


# List of functions to call PC skill values
acrobatic = get_acrobatics
athletic = get_athletics
block = get_block
charisma = get_charisma
chemistry = get_chemistry
control = get_control
craft = get_craft
destruction = get_destruct
dexterity = get_dexterity
disguise = get_disguise
engineer = get_engineer
enhancement = get_enhance
enlightenment = get_enlight
escape = get_escape
heavy_armor = get_heavyarmor
interaction = get_interaction
knowledge = get_knowledge
light_armor = get_lightarmor
medicine = get_medicine
melee = get_melee
perception = get_perception
ranged = get_ranged
ride = get_ride
security = get_security
sense_motive = get_sensemotive
sleight_of_hand = get_sleight
stealth = get_stealth
survival = get_survival
unarmed = get_unarmed
utility = get_utility


def skill_challenge(pc, skill, diff):
    if diff == 8:
        difficulty = "Easy"
        print("Difficulty: Easy")

    elif diff == 12:
        difficulty = "Standard"
        print("Difficulty: Standard")

    elif diff == 16:
        difficulty = "Hard"
        print("Difficulty: Hard")

    else:
        difficulty = "Standard"
        print("Difficulty defaulted to Standard.")

    luck_mod = get_luckmod(pc)
    print("Luck modifier:", luck_mod)

    if skill == athletic:  # recognizes the skill as Athletic and applies proper skill modifier
        skill_modifier = get_athletics(pc)
        skill_name = "Athletic"
        print("Athletics modifier:", skill_modifier)

    elif skill == acrobatic:
        skill_modifier = get_acrobatics(pc)
        skill_name = "Acrobatic"

        if pc == Kinzin:
            skill_modifier = int(skill_modifier) - 7
            print("Acrobatic modifier:", skill_modifier)

        elif pc == Sev:
            skill_modifier = int(skill_modifier) - 1
            print("Acrobatic modifier:", skill_modifier)

        else:
            print("Acrobatic modifier:", skill_modifier)

    elif skill == block:
        skill_modifier = get_block(pc)
        skill_name = "Block"
        print("Block modifier:", skill_modifier)

    elif skill == charisma:
        skill_modifier = get_charisma(pc)
        skill_name = "Charisma"
        print("Charisma modifier:", skill_modifier)

    elif skill == chemistry:
        skill_modifier = get_chemistry(pc)
        skill_name = "Chemistry"
        print("Chemistry modifier:", skill_modifier)

    elif skill == control:
        skill_modifier = get_control(pc)
        skill_name = "Control"

        if pc == Kinzin:
            skill_modifier = int(skill_modifier) - 7
            print("Control modifier:", skill_modifier)
        else:
            print("Control modifier:", skill_modifier)

    elif skill == craft:
        skill_modifier = get_craft(pc)
        skill_name = "Craft"
        print("Craft modifier:", skill_modifier)

    elif skill == destruction:
        skill_modifier = get_destruct(pc)
        skill_name = "Destruction"

        if pc == Kinzin:
            skill_modifier = int(skill_modifier) - 7
            print("Destruction modifier:", skill_modifier)

        else:
            print("Destruction modifier:", skill_modifier)

    elif skill == dexterity:
        skill_modifier = get_dexterity(pc)
        skill_name = "Dexterity"
        print("Dexterity modifier:", skill_modifier)

    elif skill == disguise:
        skill_modifier = get_disguise(pc)
        skill_name = "Disguise"
        print("Disguise modifier:", skill_modifier)

    elif skill == engineer:
        skill_modifier = get_engineer(pc)
        skill_name = "Engineering"
        print("Engineering modifier:", skill_modifier)

    elif skill == enhancement:
        skill_modifier = get_enhance(pc)
        skill_name = "Enhancement"

        if pc == Kinzin:
            skill_modifier = int(skill_modifier) - 7
            print("Enhancement modifier:", skill_modifier)

        else:
            print("Enhancement modifier:", skill_modifier)

    elif skill == enlightenment:
        skill_modifier = get_enlight(pc)
        skill_name = "Enlightenment"
        print("Enlightenment modifier:", skill_modifier)

    elif skill == escape:
        skill_modifier = get_escape(pc)
        skill_name = "Escape"

        if pc == Kinzin:
            skill_modifier = int(skill_modifier) - 7
            print("Escape modifier:", skill_modifier)

        else:
            print("Escape modifier:", skill_modifier)

    elif skill == heavy_armor:
        skill_modifier = get_heavyarmor(pc)
        skill_name = "Heavy Armor"
        print("Heavy Armor modifier:", skill_modifier)

    elif skill == light_armor:
        skill_modifier = get_lightarmor(pc)
        skill_name = "Light Armor"
        print("Light Armor modifier:", skill_modifier)

    elif skill == interaction:
        skill_modifier = get_interaction(pc)
        skill_name = "Interaction"
        print("Interaction modifier:", skill_modifier)

    elif skill == knowledge:
        skill_modifier = get_knowledge(pc)
        skill_name = "Knowledge"
        print("Knowledge modifier:", skill_modifier)

    elif skill == medicine:
        skill_modifier = get_medicine(pc)
        skill_name = "Medicine"
        print("Medicine modifier:", skill_modifier)

    elif skill == melee:
        skill_modifier = get_melee(pc)
        skill_name = "Melee"
        print("Melee modifier:", skill_modifier)

    elif skill == perception:
        skill_modifier = get_perception(pc)
        skill_name = "Perception"
        print("Perception modifier:", skill_modifier)

    elif skill == ranged:
        skill_modifier = get_ranged(pc)
        skill_name = "Ranged"
        print("Ranged modifier:", skill_modifier)

    elif skill == ride:
        skill_modifier = get_ride(pc)
        skill_name = "Ride"
        print("Ride modifier:", skill_modifier)

    elif skill == security:
        skill_modifier = get_security(pc)
        skill_name = "Security"
        print("Security modifier:", skill_modifier)

    elif skill == sense_motive:
        skill_modifier = get_sensemotive(pc)
        skill_name = "Sense Motive"
        print("Sense Motive modifier:", skill_modifier)

    elif skill == sleight_of_hand:
        skill_modifier = get_sleight(pc)
        skill_name = "Sleight of Hand"

        if pc == Kinzin:
            skill_modifier = int(skill_modifier) - 7
            print("Sleight of Hand modifier:", skill_modifier)

        else:
            print("Sleight of Hand modifier:", skill_modifier)

    elif skill == stealth:
        skill_modifier = get_stealth(pc)
        skill_name = "Stealth"

        if pc == Ho:
            skill_modifier = int(skill_modifier) - 5
            print("Stealth modifier:", skill_modifier)

        elif pc == Kinzin:
            skill_modifier = int(skill_modifier) - 7
            print("Stealth modifier:", skill_modifier)

        elif pc == Vampyrate:
            skill_modifier = int(skill_modifier) + 5
            print("Stealth modifier:", skill_modifier)

        else:
            print("Stealth modifier:", skill_modifier)

    elif skill == survival:
        skill_modifier = get_survival(pc)
        skill_name = "Survival"
        print("Survival modifier:", skill_modifier)

    elif skill == unarmed:
        skill_modifier = get_unarmed(pc)
        skill_name = "Unarmed"
        print("Unarmed modifier:", skill_modifier)

    elif skill == utility:
        skill_modifier = get_utility(pc)
        skill_name = "Utility"

        if pc == Kinzin:
            skill_modifier = int(skill_modifier) - 7
            print("Utility modifier:", skill_modifier)

        else:
            print("Utility modifier:", skill_modifier)

    else:
        print("Skill not found.")
        return None

    outcome_1 = int(randint(1, 15))
    print("D20 roll:", outcome_1)

    outcome = outcome_1 + luck_mod + skill_modifier

    print("The total outcome of the roll is:", outcome)

    if outcome >= diff:
        p1 = str(pc.name)
        p2 = " passed the "
        p3 = skill_name
        p4 = " check!"
        message = p1 + p2 + p3 + p4  # stores outcome value to be retrieved later for SQL storage
        fluke = fluke_system()
        if fluke != "Lucky":
            fluke = None

    elif outcome < diff:
        p1 = str(pc.name)
        p2 = " failed the "
        p3 = skill_name
        p4 = " check..."
        message = p1 + p2 + p3 + p4
        difficulty = "Failed"
        fluke = fluke_system()
        if fluke != "Unlucky":
            fluke = None

    else:
        return None

    return outcome, skill_name, difficulty, fluke, message


# Summoning the IDS
# Enemy or PC mull roll d20 die and compare it against the target's AC
# If the damage is >=, then roll the appropriate IDS die based on the enemy's attack power

# Improvised Damage System (IDS)
# High DMG - d8
# Med DMG - d6
# Low DMG - d4

# When calculating DMG, -2 if enemy/PC is partially covered
# If the enemy/PC is completely concealed, -5 to DMG roll


def high_dmg():
    dmg = randint(1, 8)
    return dmg


def med_dmg():
    dmg = randint(1, 6)
    return dmg


def low_dmg():
    dmg = randint(1, 4)
    return dmg


def dmg_challenge(target, enemy, condition=None):

    decider = randint(1, 20)

    if decider >= target.ac:

        if enemy.ap == 4:
            dmg = low_dmg()

            if condition == "Partial":
                dmg = dmg - 2
                if dmg < 0:
                    print("Attack is unsuccessful!")
                    return None
                else:
                    print("The attack by", enemy.name, "is successful!", target.name, "lost", dmg, "HP(s)!")
                    return dmg

            elif condition == "Concealed":
                dmg = dmg - 5
                if dmg < 0:
                    print("Attack is unsuccessful!")
                    return None
                else:
                    print("The attack by", enemy.name, "is successful!", target.name, "lost", dmg, "HP(s)!")
                    return dmg

            else:
                print("The attack by", enemy.name, "is successful!", target.name, "lost", dmg, "HP(s)!")
                return dmg

        elif enemy.ap == 6:
            dmg = med_dmg()

            if condition == "Partial":
                dmg = dmg - 2
                if dmg < 0:
                    print("Attack is unsuccessful!")
                    return None
                else:
                    print("The attack by", enemy.name, "is successful!", target.name, "lost", dmg, "HP(s)!")
                    return dmg

            elif condition == "Concealed":
                dmg = dmg - 5
                if dmg < 0:
                    print("Attack is unsuccessful!")
                    return None
                else:
                    print("The attack by", enemy.name, "is successful!", target.name, "lost", dmg, "HP(s)!")
                    return dmg

            else:
                print("The attack by", enemy.name, "is successful!", target.name, "lost", dmg, "HP(s)!")
                return dmg

        elif enemy.ap == 8:
            dmg = high_dmg()

            if condition == "Partial":
                dmg = dmg - 2
                if dmg < 0:
                    print("Attack is unsuccessful!")
                    return None
                else:
                    print("The attack by", enemy.name, "is successful!", target.name, "lost", dmg, "HP(s)!")
                    return dmg

            elif condition == "Concealed":
                dmg = dmg - 5
                if dmg < 0:
                    print("Attack is unsuccessful!")
                    return None
                else:
                    print("The attack by", enemy.name, "is successful!", target.name, "lost", dmg, "HP(s)!")
                    return dmg

            else:
                print("The attack by", enemy.name, "is successful!", target.name, "lost", dmg, "HP(s)!")
                return dmg

    else:
        print("Attack is unsuccessful!")
        return None


# Yuri's Trauma Triage

# Regen System - Implement a manual hp regeneration (per round) based off PC's Constitution modifier
# E.g. At the end of every round, Ho gains .5 hp points

# Medicine Skill - Roll a d20, if >= pc_being_healed.fortitude, then roll for amount of hp healed
# Using the Medicine skill to heal yourself or another PC deals d4 for hp recovery, multiplied by the Medicine mod

def heal(healer, injured):

    skill_check = randint(1, 25)
    healer_fortitude = get_medicine(healer)
    injured_hp = get_hp(injured)

    if skill_check >= injured.fortitude:
        hp = randint(1, 4)
        hp_back = int(hp) * int(healer_fortitude)
        new_injured_hp = hp_back + injured_hp

        print(healer.name, "healed", injured.name, "for", hp_back, "HPs!")

        return skill_check, new_injured_hp

    else:
        luck = fluke_system()
        if luck == "Unlucky":
            print("Skill check failed! An unlucky encounter.")
            return luck
        else:
            print("Skill check failed!")
            return None


# TGG MAINFRAME
# Tkinter-generated GUI that brings visual clarity to Fate's internal workings
# CODE MONKEY'S REMINDER: New widget, new frame!
# Kill switch = mainloop()


IFS_GUI = Tk()

IFS_GUI.title("Internal Fate System")

challenge_var = IntVar()
challenge_var.set(None)

skill_frame = Frame(IFS_GUI)
skill_frame.grid()

Label(skill_frame, text="Internal Fate System").grid(row=0, pady=3, columnspan=3, sticky='n')

expand_frame = Frame(skill_frame)


def expand_page():

    for widget in expand_frame.winfo_children():    # calls a list of all the existing widgets in the frame
        widget.destroy()                            # in order to clear them out for new widgets to populate

    svariable = StringVar()
    svariable.set("Select a Skill")     # sets the default value of the option menu

    cvariable = StringVar()
    cvariable.set("Select a PC")

    dvariable = StringVar()
    dvariable.set("Select Difficulty")

    rvariable = StringVar()
    rvariable.set("The gods will decide...")

    def get_pc():
        pc = cvariable.get()
        if pc == "Ho":
            pc = Ho

        elif pc == "Kinzin":
            pc = Kinzin

        elif pc == "Mignon":
            pc = Mignon

        elif pc == "Raven":
            pc = Raven

        elif pc == "Sev":
            pc = Sev

        else:
            print("PC not found.")

        return pc

    def get_skill():
        skill = svariable.get()
        if skill == "Acrobatics":
            skill = acrobatic
        elif skill == "Athletics":
            skill = athletic
        elif skill == "Block":
            skill = block
        elif skill == "Chemistry":
            skill = chemistry
        elif skill == "Control":
            skill = control
        elif skill == "Craft":
            skill = craft
        elif skill == "Destruction":
            skill = destruction
        elif skill == "Disguise":
            skill = disguise
        elif skill == "Engineering":
            skill = engineer
        elif skill == "Enhancement":
            skill = enhancement
        elif skill == "Enlightenment":
            skill = enlightenment
        elif skill == "Escape":
            skill = escape
        elif skill == "Heavy Armor":
            skill = heavy_armor
        elif skill == "Interaction":
            skill = interaction
        elif skill == "Knowledge":
            skill = knowledge
        elif skill == "Light Armor":
            skill = light_armor
        elif skill == "Medicine":
            skill = medicine
        elif skill == "Melee":
            skill = melee
        elif skill == "Perception":
            skill = perception
        elif skill == "Ranged":
            skill = ranged
        elif skill == "Ride":
            skill = ride
        elif skill == "Security":
            skill = security
        elif skill == "Sense Motive":
            skill = sense_motive
        elif skill == "Sleight of Hand":
            skill = sleight_of_hand
        elif skill == "Stealth":
            skill = stealth
        elif skill == "Survival":
            skill = survival
        elif skill == "Unarmed":
            skill = unarmed
        else:
            print("Skill not found.")
        return skill

    def get_diff():
        diff = dvariable.get()
        if diff == "Easy":
            diff = Easy

        elif diff == "Hard":
            diff = Hard

        elif diff == "Standard":
            diff = Standard

        else:
            print("Difficulty not found.")

        return diff

    def roll_the_die():
        pc = get_pc()
        skill = get_skill()
        diff = get_diff()

        result = skill_challenge(pc, skill, diff)
        message = result[4]     # grabs the string to be presented at the bottom of the card

        rvariable.set(message)
        return result

    expand_frame.grid()

    skill_dropdown = OptionMenu(expand_frame, svariable, "Acrobatics", "Athletics", "Block", "Chemistry", "Control",
                                "Craft", "Destruction", "Disguise", "Engineering", "Enhancement", "Enlightenment",
                                "Escape", "Heavy Armor", "Interaction", "Knowledge", "Light Armor", "Medicine", "Melee",
                                "Perception", "Ranged", "Ride", "Security", "Sense Motive", "Sleight of Hand",
                                "Stealth", "Survival", "Unarmed")

    skill_dropdown.grid(row=2, column=1)

    pc_dropdown = OptionMenu(expand_frame, cvariable, "Ho", "Kinzin", "Mignon", "Raven", "Sev")
    pc_dropdown.grid(row=2, column=0)

    diff_dropdown = OptionMenu(expand_frame, dvariable, "Easy", "Standard", "Hard")
    diff_dropdown.grid(row=2, column=2)

    card_frame = Frame(expand_frame)
    card_frame.grid(row=4, columnspan=3)

    skill_chall_label = Label(card_frame, text="Skill Challenge")
    skill_chall_label.grid(row=3, columnspan=3, pady=2)

    photo = PhotoImage(file="RavenStealthSuccess2.gif")

    skill_chall_card = Label(card_frame, image=photo, width=240, height=300)
    skill_chall_card.photo = photo
    skill_chall_card.grid(row=4)

    roll_result = Entry(card_frame, width=37, state="readonly", textvariable=rvariable)
    roll_result.grid(row=5, pady=5)

    roll_die = Button(card_frame, text="Roll the die!", command=roll_the_die)
    roll_die.grid(row=6, columnspan=3, sticky='n', pady=4)


second_frame = Frame(skill_frame)
second_frame.grid()

skill_challenge_button = Radiobutton(second_frame, text="Skill Challenge", value=1, variable=challenge_var,
                                     command=expand_page)

skill_challenge_button.grid(row=1, column=0)

dps_challenge_button = Radiobutton(second_frame, text="Combat Challenge", value=2, variable=challenge_var)
dps_challenge_button.grid(row=1, column=1)

heal_challenge_button = Radiobutton(second_frame, text="Heal Challenge", value=3, variable=challenge_var)
heal_challenge_button.grid(row=1, column=2)


IFS_GUI.mainloop()
