from flukesys import fluke_system
from random import randint
from helper import get_skill_value, get_skill_modifier


# Summoning the Improvised Damage System (IDS)
# Enemy or PC mull roll d20 die and compare it against the target's AC
# If the damage is >=, then roll the appropriate IDS die based on the enemy's attack power
# The appropriate combat modifier is applied (e.g. ranged, melee, destruction, etc.)

# Improvised Damage System (IDS)
# High DMG - d8
# Med DMG - d6
# Low DMG - d4

# When calculating DMG, -2 if enemy/PC is partially covered
# If the enemy/PC is completely concealed, -5 to DMG roll


def dmg_challenge(target, enemy, skill, condition=None):

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

    sv = get_skill_value(skill)
    the_skill_modifier = get_skill_modifier(enemy, sv, skill)
    rand_roll = randint(1, 20)
    decider = rand_roll + the_skill_modifier

    # If the roll is >= to the target's ac plus the skill modifier, then the enemy's hit is successful
    # The enemy must now roll for the number of dmg points inflicted

    if decider >= target[2]:

        if enemy[3] == 4:
            dmg_points = dmg(low)

            if condition == "Partial":
                dmg_points = dmg_points - 2
                if dmg_points > 0:
                    message = enemy[0], "attacks", target[0], "for", dmg_points, "HP(s)."
                    return dmg_points, enemy, target, message
                else:
                    message = "The attack is unsuccessful."
                    dmg_points = None
                    return dmg_points, enemy, target, message

            elif condition == "Concealed":
                dmg_points = dmg_points - 5
                if dmg_points > 0:
                    message = enemy[0], "attacks", target[0], "for", dmg_points, "HP(s)."
                    return dmg_points, enemy, target, message
                else:
                    message = "The attack is unsuccessful."
                    dmg_points = None
                    return dmg_points, enemy, target, message

            else:
                message = enemy[0], "attacks", target[0], "for", dmg_points, "HP(s)."
                return dmg_points, enemy, target, message

        elif enemy[3] == 6:
            dmg_points = dmg(medium)

            if condition == "Partial":
                dmg_points = dmg_points - 2
                if dmg_points > 0:
                    message = enemy[0], "attacks", target[0], "for", dmg_points, "HP(s)."
                    return dmg_points, enemy, target, message
                else:
                    message = "The attack is unsuccessful."
                    dmg_points = None
                    return dmg_points, enemy, target, message

            elif condition == "Concealed":
                dmg_points = dmg_points - 5
                if dmg_points > 0:
                    message = enemy[0], "attacks", target[0], "for", dmg_points, "HP(s)."
                    return dmg_points, enemy, target, message
                else:
                    message = "The attack is unsuccessful."
                    dmg_points = None
                    return dmg_points, enemy, target, message

            else:
                message = enemy[0], "attacks", target[0], "for", dmg_points, "HP(s)."
                return dmg_points, enemy, target, message

        elif enemy[3] == 8:
            dmg_points = dmg(high)

            if condition == "Partial":
                dmg_points = dmg_points - 2
                if dmg_points > 0:
                    message = enemy[0], "attacks", target[0], "for", dmg_points, "HP(s)."
                    return dmg_points, enemy, target, message
                else:
                    message = "The attack is unsuccessful."
                    dmg_points = None
                    return dmg_points, enemy, target, message

            elif condition == "Concealed":
                dmg_points = dmg_points - 5
                if dmg_points > 0:
                    message = enemy[0], "attacks", target[0], "for", dmg_points, "HP(s)."
                    return dmg_points, enemy, target, message
                else:
                    message = "The attack is unsuccessful."
                    dmg_points = None
                    return dmg_points, enemy, target, message

            else:
                message = enemy[0], "attacks", target[0], "for", dmg_points, "HP(s)."
                return dmg_points, enemy, target, message

    else:
        message = "The attack is unsuccessful."
        dmg_points = None
        return dmg_points, enemy, target, message

