# hiddenjules
A coder's cove safehousing the early stages of the Internal Fate App.

STEP NUMBER ONE: Figure out the mystery that are pulls and pull requests and branches (why are there so many branches?)

Most of the code within the files comes with notes to explain the reason behind functions. But I'll word vomit the details here as well:

ATTRIBUTES AND SKILLS

# Charisma (CH)
# Constitution (CON)
# Dexterity (DEX)
# Intelligence (INT)
# Luck (LCK)
# Speed (SPD)
# Strength (STR)
# Wisdom (WIS)

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


MAIN FUNCTIONS

# The Almighty Skill Challenge
# It determines the modifier by passing in the skill parameter which returns a fixed value based on
# the PC's attribute for that particular skill. (e.g. If your Dexterity is 20, then your modifier is 2.0)
# The modifier is then applied to a random 20-sided dice roll along with the PC's luck modifier and
# compared against the difficulty level. Pray the RNG gods are on your side!


# Yuri's Trauma Triage
# Regen System - Implement a manual hp regeneration (per round) based off PC's Constitution modifier (soon TM)
# E.g. At the end of every round, Ho gains .5 hp points

# Medicine Skill - Roll a d20, if >= injured[fortitude], then roll for amount of hp healed
# Using the Medicine skill to heal yourself or another PC deals d4 for hp recovery, multiplied by the Medicine mod


# Summoning the Improvised Damage System (IDS)
# Enemy or PC mull roll d20 die and compare it against the target's AC
# If the damage is >=, then roll the appropriate IDS die based on the enemy's attack power

# Improvised Damage System (IDS)
# High DMG - d8
# Med DMG - d6
# Low DMG - d4

# When calculating DMG, -2 if enemy/PC is partially covered
# If the enemy/PC is completely concealed, -5 to DMG roll


TRANSLATING RPG SHEETS INTO NAMEDTUPLES 

# MATHEMATICAL BREAKDOWN
# pc = namedtuple(list of values here)
# hp = 1.5 x pc[constitution] (score)

# light armor AC = 7 + pc[speed] (or pc[dexterity]) + pc[light_armor] (mod)
# heavy armor AC = 12 + pc[heavy_armor] + pc.constitution (mod)

# fortitude = 10 + pc[constitution] (mod)
# will = 10 + pc[wisdom] (mod)

# light armor reflex = 10 + pc[speed] (or pc[dexterity]) (mod)
# heavy armor reflex = 5 + pc[speed] (or pc[dexterity]) + (pc[heavy_armor] * .5) (mod)

# ap, or attack power, is d4 by default
