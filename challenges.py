from bloodcraft import *
from flukesys import fluke_system
from random import *


# The Almighty Skill Challenge
# It determines the modifier by passing in the skill parameter which returns a fixed value based on
# the PC's attribute for that particular skill. (e.g. If your Dexterity is 20, then your modifier is 2.0)
# The modifier is then applied to a random 20-sided dice roll along with the PC's luck modifier and
# compared against the difficulty level. Pray the RNG gods are on your side!


def skill_challenge(pc, skill, difficulty):

    # Converts the skill parameter into a searchable indices value for finding and applying modifiers

    if skill == "Acrobatics" or skill == "Escape" or skill == "Ranged" or skill == "Ride"  \
            or skill == "Sleight of Hand" or skill == "Stealth":
        skill_value = 9
    elif skill == "Athletics" or skill == "Melee" or skill == "Unarmed":
        skill_value = 13
    elif skill == "Block" or skill == "Light Armor":
        skill_value = 12
    elif skill == "Chemistry" or skill == "Craft" or skill == "Engineering" or skill == "Knowledge" \
            or skill == "Security" or skill == "Sense Motive":
        skill_value = 10
    elif skill == "Control" or skill == "Destruction" or skill == "Enhancement" or skill == "Medicine" \
            or skill == "Perception" or skill == "Survival" or skill == "Utility":
        skill_value = 14
    elif skill == "Disguise" or skill == "Enlightenment" or skill == "Interaction":
        skill_value = 7
    elif skill == "Heavy Armor":
        skill_value = 8
    elif skill == "Knowledge" or skill == "Security" or skill == "Sense Motive":
        skill_value = 10
    else:
        skill_value = "Skill Not Found"

    # Converts the difficulty parameter into a string to be used later when projecting the roll results

    if difficulty == 8:
        diff = "Easy"
    elif difficulty == 12:
        diff = "Standard"
    elif difficulty == 16:
        diff = "Hard"
    else:
        diff = None

    # Looks for PC-specific skill modifiers and applies them when rolling for a skill check

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

    the_skill_modifier = get_skill_modifier(pc, skill_value, skill)
    luck_modifier = get_luck_modifier(pc)
    outcome_1 = int(randint(1, 15))
    outcome = outcome_1 + luck_modifier + the_skill_modifier

    # Success!

    if outcome >= difficulty:

        # Calculates the chance of a lucky encounter

        check_for_fluke = fluke_system()

        if check_for_fluke != "Lucky":
            check_for_fluke = None
            message = pc[0] + " passed the " + skill + " check!"
        else:
            message = pc[0] + " passed the " + skill + " check!*"

    # Failure...

    elif outcome < difficulty:
        diff = "Failed"

        # Calculates the chance of an unlucky encounter

        check_for_fluke = fluke_system()

        if check_for_fluke != "Unlucky":
            check_for_fluke = None
            message = pc[0] + " failed the " + skill + " check..."
        else:
            message = pc[0] + " failed the " + skill + " check...*"

    else:
        print("Error.")
        return None

    # This finally returns a list of values to be retrieved and stored individually within MySQL (soon TM)

    return outcome, skill, diff, check_for_fluke, message


# Yuri's Trauma Triage
# Regen System - Implement a manual hp regeneration (per round) based off PC's Constitution modifier
# E.g. At the end of every round, Ho gains .5 hp points

# Medicine Skill - Roll a d20, if >= injured[fortitude], then roll for amount of hp healed
# Using the Medicine skill to heal yourself or another PC deals d4 for hp recovery, multiplied by the Medicine mod


def heal_challenge(healer, injured):
    skill_check = randint(1, 25)
    healer_fortitude = int(healer[14] / 10)
    injured_hp = injured[1]
    healers_luck = fluke_system()

    if skill_check >= injured[4]:
        additional_hp = randint(1, 4)
        hp_back = int(additional_hp) * int(healer_fortitude)
        new_injured_hp = hp_back + injured_hp

        if healers_luck == "Lucky":
            message = healer[0], "healed", injured[0], "for", hp_back, "HPs!*"
        else:
            message = healer[0], "healed", injured[0], "for", hp_back, "HPs!"

    else:
        hp_back = None
        new_injured_hp = None
        if healers_luck == "Unlucky":
            message = healer[0] + " failed to heal " + injured[0] + ".*"
        else:
            message = healer[0] + " failed to heal " + injured[0] + "."

    return hp_back, new_injured_hp, healers_luck, message

# Summoning the Improvised Damage System (IDS)
# Enemy or PC mull roll d20 die and compare it against the target's AC
# If the damage is >=, then roll the appropriate IDS die based on the enemy's attack power

# Improvised Damage System (IDS)
# High DMG - d8
# Med DMG - d6
# Low DMG - d4

# When calculating DMG, -2 if enemy/PC is partially covered
# If the enemy/PC is completely concealed, -5 to DMG roll


def dmg_challenge(target, enemy, condition=None):

    high = "High"
    medium = "Medium"
    low = "Low"

    # dmg() takes a parameter based on the attacker's ap, or attack power

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

    # If the roll is greater than or equal to the target's ac, then the enemy's hit is successful
    # The enemy must now roll for the number of dmg points inflicted

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
