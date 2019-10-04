from flukesys import fluke_system
from random import randint
from helper import get_skill_modifier, get_luck_modifier, get_skill_value


# The Almighty Skill Challenge
# It determines the modifier by passing in the skill parameter which returns a fixed value based on
# the PC's attribute for that particular skill. (e.g. If your Dexterity is 20, then your modifier is 2.0)
# The modifier is then applied to a random 20-sided dice roll along with the PC's luck modifier and
# compared against the difficulty level. Pray the RNG gods are on your side!


def skill_challenge(pc, skill, difficulty):

    # Converts the difficulty parameter into a string to be used later when projecting the roll results

    if difficulty == 8:
        diff = "Easy"
    elif difficulty == 12:
        diff = "Standard"
    elif difficulty == 16:
        diff = "Hard"
    else:
        diff = None

    sv = get_skill_value(skill)
    the_skill_modifier = get_skill_modifier(pc, sv, skill)
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
