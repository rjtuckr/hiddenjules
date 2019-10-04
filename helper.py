from bloodcraft import Kinzin, Sev, Ho, Vampyrate
from flukesys import fluke_system
from random import randint


# IFS Guts
# These helper functions correspond to the skill, heal and damage challenges.
# They can search for the summoned skill and its modifier for that PC in 
# order to be applied to some RNG logic for determining the outcome.


def get_skill_value(skill):

    # Converts the skill parameter into a searchable indices value for finding and applying modifiers

        if skill == "Acrobatics" or skill == "Escape" or skill == "Ranged" or skill == "Ride"  \
                or skill == "Sleight of Hand" or skill == "Stealth":
            skill_value = 9
            return skill_value
        elif skill == "Athletics" or skill == "Melee" or skill == "Unarmed":
            skill_value = 13
            return skill_value
        elif skill == "Block" or skill == "Light Armor":
            skill_value = 12
            return skill_value
        elif skill == "Chemistry" or skill == "Craft" or skill == "Engineering" or skill == "Knowledge" \
                or skill == "Security" or skill == "Sense Motive":
            skill_value = 10
            return skill_value
        elif skill == "Control" or skill == "Destruction" or skill == "Enhancement" or skill == "Medicine" \
                or skill == "Perception" or skill == "Survival" or skill == "Utility":
            skill_value = 14
            return skill_value
        elif skill == "Disguise" or skill == "Enlightenment" or skill == "Interaction":
            skill_value = 7
            return skill_value
        elif skill == "Conviction" or "Heavy Armor":
            skill_value = 8
            return skill_value
        elif skill == "Knowledge" or skill == "Security" or skill == "Sense Motive":
            skill_value = 10
            return skill_value
        else:
            skill_value = "Skill Not Found"
            print(skill_value)
            return None

def get_skill_modifier(chosen_pc, sv, chosen_skill):

        # Looks for PC-specific skill modifiers and applies them when rolling for a skill check

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

