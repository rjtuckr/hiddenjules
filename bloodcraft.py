from collections import namedtuple

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
# Conviction (CHA)
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

# Difficulty Levels
Easy = 8
Standard = 12
Hard = 16

# MATHEMATICAL BREAKDOWN
# hp = 1.5 x pc[constitution] (score)

# light armor AC = 7 + pc[speed] (or pc[dexterity]) + pc[light_armor] (mod)
# heavy armor AC = 12 + pc[heavy_armor] + pc.constitution (mod)

# fortitude = 10 + pc[constitution] (mod)
# will = 10 + pc[wisdom] (mod)

# light armor reflex = 10 + pc[speed] (or pc[dexterity]) (mod)
# heavy armor reflex = 5 + pc[speed] (or pc[dexterity]) + (pc[heavy_armor] * .5) (mod)

# ap, or attack power, is d4 by default

Character = namedtuple("Character", "name hp ac ap fortitude will reflex charisma constitution dexterity intelligence"
                                    " luck speed strength wisdom")

Enemy = namedtuple("Enemy", "name hp ac ap fortitude will reflex charisma constitution dexterity intelligence luck "
                            "speed strength wisdom")

# Namedtuple Values
name = 0
hp = 1
ac = 2
ap = 3
fortitude = 4
will = 5
reflex = 6
charisma = 7            # Disguise, Enlightenment, Interaction
constitution = 8        # Conviction, Heavy Armor
dexterity = 9           # Acrobatics, Escape, Ranged, Ride, Sleight of Hand, Stealth
intelligence = 10       # Chemistry, Craft, Engineering, Knowledge, Security, Sense Motive
luck = 11
speed = 12              # Block, Light Armor
strength = 13           # Athletics, Melee, Unarmed
wisdom = 14             # Control, Destruction, Enhancement, Medicine, Perception, Survival, Utility

# PCs and Enemies
Ho = Character("Ho", 30, 9, 4, 12, 13, 11, 20, 20, 10, 30, 20, 10, 20, 30)
Kinzin = Character("Kinzin", 45, 18, 4, 13, 12, 8, 10, 30, 20, 20, 10, 20, 30, 20)
Mignon = Character("Mignon", 30, 12, 4, 12, 13, 13, 10, 20, 30, 20, 10, 20, 20, 30)
Raven = Character("Raven", 15, 12, 4, 11, 12, 13, 20, 10, 30, 10, 20, 20, 30, 20)
Sev = Character("Sev", 30, 11, 4, 12, 13, 12, 30, 20, 10, 20, 10, 20, 20, 30)
Vampyrate = Enemy("Vampyrate", 15, 13, 4, 11, 11, 14, 15, 10, 40, 20, 30, 20, 10, 10)
Plaguebourne_Pillager = Enemy("Pillager", 10, 11, 4, 12, 12, 12, 20, 20, 20, 20, 20, 20, 20, 20)

# Skills
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
conviction = "Conviction"
destruction = "Destruction"
enhancement = "Enhancement"
medicine = "Medicine"
perception = "Perception"
survival = "Survival"
utility = "Utility"
