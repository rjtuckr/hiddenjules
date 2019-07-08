# INTERNAL FATE APP 

An RPG-inspired app that rolls the die of Fate for you. This was built as an app for writers participating in a campaign who didn't have the time to pursue a traditional tabletop RPG -- but it can be used by anyone who finds it useful. You select a PC, a skill, and a difficulty (ranging from Easy to Standard to Hard) and hope that Luck is in your favor!

STEP NUMBER ONE: Figure out the mystery that are pulls and pull requests and branches (why are there so many branches?)

Most of the code within the files comes with notes to explain the reason behind functions. But I'll place the details here as well:

# ATTRIBUTES AND SKILLS

TL;DR -- Find under Bloodcraft.py


# MAIN FUNCTIONS

# The Almighty Skill Challenge
It determines the modifier by grabbing the skill parameter which returns a fixed value based on
the PC's attribute for that particular skill. (e.g. If your Dexterity is 20, then your modifier is 2.0)
The modifier is then applied to a random 20-sided dice roll (aka randint) along with the PC's luck modifier and
compared against the difficulty level. Pray the RNG gods are on your side!


# The Heal Challenge
Regen System - Implement a manual hp regeneration (per round) based off PC's Constitution modifier (soon TM)
E.g. At the end of every round, Ho gains .5 hp points

Medicine Skill - Roll a d20, if >= injured[fortitude], then roll for amount of hp healed

Using the Medicine skill to heal yourself or another PC deals d4 for hp recovery, multiplied by the Medicine mod


# The Combat Challenge
Enemy or PC must roll d20 die and compare it against the target's AC

If the damage is >=, then roll the appropriate IDS die based on the enemy's attack power

Improvised Damage System (IDS)

High DMG - d8

Med DMG - d6

Low DMG - d4

When calculating DMG, -2 if enemy/PC is partially covered

If the enemy/PC is completely concealed, -5 to DMG roll


# TRANSLATING RPG SHEETS INTO NAMEDTUPLES 

pc = namedtuple(list of values here)

hp = 1.5 x pc[constitution] (score)

light armor AC = 7 + pc[speed] (or pc[dexterity]) + pc[light_armor] (mod)

heavy armor AC = 12 + pc[heavy_armor] + pc.constitution (mod)

fortitude = 10 + pc[constitution] (mod)

will = 10 + pc[wisdom] (mod)

light armor reflex = 10 + pc[speed] (or pc[dexterity]) (mod)

heavy armor reflex = 5 + pc[speed] (or pc[dexterity]) + (pc[heavy_armor] * .5) (mod)

ap, or attack power, is d4 by default
