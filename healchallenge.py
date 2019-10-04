from flukesys import fluke_system
from random import randint


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

    return hp_back, new_injured_hp, healers_luck, message, healer, injured

