from tkinter import *
from challenges import *


# Written by Julie Tucker
# rjtuckr@outlook.com
# https://github.com/rjtuckr


class IFS:
    def __init__(self, pc=None, attribute=None, skill=None, difficulty=None, enemy=None, target=None, condition=None):

        self.pc = pc
        self.attribute = attribute
        self.skill = skill
        self.difficulty = difficulty
        self.enemy = enemy
        self.target = target
        self.condition = condition

    # TGG MAINFRAME
    # Tkinter-generated GUI that brings visual clarity to Fate's internal workings
    # CODE MONKEY'S REMINDER: New widget, new frame!

    def tgg_mainframe(self):
        gui = Tk()
        gui.title("Internal Fate System")

        challenge_var = IntVar()    # Variable that stores the user's choice of challenge
        challenge_var.set(None)

        title_frame = Frame(gui)    # Title frame
        title_frame.grid()

        Label(title_frame, text="Internal Fate System").grid(row=0, pady=3, columnspan=3, sticky='n')

        challenge_frame = Frame(title_frame)      # Challenge options frame
        sc_frame = Frame(title_frame)             # Skill challenge frame

        def skill_challenge_page():

            for widget in sc_frame.winfo_children():  # Calls a list of all the existing widgets in the frame
                widget.destroy()                      # in order to clear them out for new widgets to populate

            svariable = StringVar()
            svariable.set("Select a Skill")           # Sets the default value of the option menu

            cvariable = StringVar()
            cvariable.set("Select a PC")

            dvariable = StringVar()
            dvariable.set("Select Difficulty")

            rvariable = StringVar()
            rvariable.set("The gods will decide...")

            # Get methods for parameters to pass into skill_challenge()

            def get_pc():
                selected_pc = cvariable.get()
                if selected_pc == "Ho":
                    selected_pc = Ho

                elif selected_pc == "Kinzin":
                    selected_pc = Kinzin

                elif selected_pc == "Mignon":       # Because cvariable.get() returns the result as a string, this
                    selected_pc = Mignon            # if statement acts to convert it back to a namedtuple

                elif selected_pc == "Raven":
                    selected_pc = Raven

                elif selected_pc == "Sev":
                    selected_pc = Sev

                else:
                    print("PC not found.")

                return selected_pc

            def get_skill():
                selected_skill = svariable.get()
                if selected_skill == "Acrobatics":
                    selected_skill = acrobatics
                elif selected_skill == "Athletics":
                    selected_skill = athletics
                elif selected_skill == "Block":
                    selected_skill = block
                elif selected_skill == "Chemistry":
                    selected_skill = chemistry
                elif selected_skill == "Control":
                    selected_skill = control
                elif selected_skill == "Craft":
                    selected_skill = craft
                elif selected_skill == "Destruction":
                    selected_skill = destruction
                elif selected_skill == "Disguise":
                    selected_skill = disguise
                elif selected_skill == "Engineering":
                    selected_skill = engineer
                elif selected_skill == "Enhancement":
                    selected_skill = enhancement
                elif selected_skill == "Enlightenment":
                    selected_skill = enlightenment
                elif selected_skill == "Escape":
                    selected_skill = escape
                elif selected_skill == "Heavy Armor":
                    selected_skill = heavy_armor
                elif selected_skill == "Interaction":
                    selected_skill = interaction
                elif selected_skill == "Knowledge":
                    selected_skill = knowledge
                elif selected_skill == "Light Armor":
                    selected_skill = light_armor
                elif selected_skill == "Medicine":
                    selected_skill = medicine
                elif selected_skill == "Melee":                 # Each skill variable has its own associated value,
                    selected_skill = melee                      # or integer, which will be plugged in to the indices
                elif selected_skill == "Perception":            # of a namedtuple to retrieve the desired value
                    selected_skill = perception
                elif selected_skill == "Ranged":
                    selected_skill = ranged
                elif selected_skill == "Ride":
                    selected_skill = ride
                elif selected_skill == "Security":
                    selected_skill = security
                elif selected_skill == "Sense Motive":
                    selected_skill = sense_motive
                elif selected_skill == "Sleight of Hand":
                    selected_skill = sleight_of_hand
                elif selected_skill == "Stealth":
                    selected_skill = stealth
                elif selected_skill == "Survival":
                    selected_skill = survival
                elif selected_skill == "Unarmed":
                    selected_skill = unarmed
                else:
                    print("Skill not found.")
                return selected_skill

            def get_diff():
                selected_diff = dvariable.get()

                if selected_diff == "Easy":
                    selected_diff = Easy

                elif selected_diff == "Hard":
                    selected_diff = Hard

                elif selected_diff == "Standard":
                    selected_diff = Standard

                else:
                    print("Difficulty not found.")

                return selected_diff

            # The trigger behind the "Roll the die!" button

            def sc_roll_the_die():
                sc_pc = get_pc()
                sc_skill = get_skill()
                sc_diff = get_diff()

                result = skill_challenge(sc_pc, sc_skill, sc_diff)
                gui_message = result[4]  # Grabs the string to be presented at the bottom of the card

                rvariable.set(gui_message)
                return result

            # Generates the Skill Challenge frame

            sc_frame.grid()

            # The three drop down menus for the Skill Challenge: Skills, PCs, and Difficulty

            skill_dropdown = OptionMenu(sc_frame, svariable, "Acrobatics", "Athletics", "Block", "Chemistry",
                                        "Control", "Craft", "Destruction", "Disguise", "Engineering", "Enhancement",
                                        "Enlightenment", "Escape", "Heavy Armor", "Interaction", "Knowledge",
                                        "Light Armor", "Medicine", "Melee", "Perception", "Ranged", "Ride", "Security",
                                        "Sense Motive", "Sleight of Hand", "Stealth", "Survival", "Unarmed")

            pc_dropdown = OptionMenu(sc_frame, cvariable, "Ho", "Kinzin", "Mignon", "Raven", "Sev")

            diff_dropdown = OptionMenu(sc_frame, dvariable, "Easy", "Standard", "Hard")

            pc_dropdown.grid(row=2, column=0)
            skill_dropdown.grid(row=2, column=1)
            diff_dropdown.grid(row=2, column=2)

            # Frame that supports the tarot card graphics

            sc_card_frame = Frame(sc_frame)
            sc_card_frame.grid(row=4, columnspan=3)

            skill_chall_label = Label(sc_card_frame, text="Skill Challenge")
            skill_chall_label.grid(row=3, columnspan=3, pady=2)

            # The current template for the IFS tarot graphics

            photo = PhotoImage(file="TarotCard.png")

            skill_chall_card = Label(sc_card_frame, image=photo, width=370, height=300)
            skill_chall_card.photo = photo
            skill_chall_card.grid(row=4)

            # The entry box that displays the outcome of the die roll

            roll_result = Entry(sc_card_frame, width=37, state="readonly", textvariable=rvariable)
            roll_result.grid(row=5, pady=7)

            # The "Roll the die!" button

            roll_die = Button(sc_card_frame, text="Roll the die!", command=sc_roll_the_die)
            roll_die.grid(row=6, columnspan=3, sticky='n', pady=4)

        # Generates the Challenge Buttons Frame

        challenge_frame.grid()

        skill_challenge_button = Radiobutton(challenge_frame, text="Skill Challenge", value=1, variable=challenge_var,
                                             command=skill_challenge_page)

        skill_challenge_button.grid(row=1, column=0)

        dps_challenge_button = Radiobutton(challenge_frame, text="Combat Challenge", value=2, variable=challenge_var)
        dps_challenge_button.grid(row=1, column=1)

        heal_challenge_button = Radiobutton(challenge_frame, text="Heal Challenge", value=3, variable=challenge_var)
        heal_challenge_button.grid(row=1, column=2)

        gui.mainloop()


RNG = IFS()
RNG.tgg_mainframe()
