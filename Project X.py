import tkinter
from tkinter import messagebox
import random

class STARTUPMENU:
    # This class will include the startup menu of the game.

    def __init__ (self):
        self.wnd = tkinter.Tk ()
        self.wnd.geometry ("500x540")
        self.frame = tkinter.Frame (self.wnd, background = "black")
        self.gameTitle = tkinter.Label (self.frame, text = "GAME TITLE")

        self.startGameButton = tkinter.Button (
        self.frame, text = "Start Game", command = self.startGame,
         background = "grey", activebackground = "white"
                                                )

        self.gameSettingsButton = tkinter.Button (
        self.frame, text = "Settings", command = GAMESETTINGS,
        background = "grey", activebackground = "white"
                                                   )

        self.informationButton = tkinter.Button (
        self.frame, text = "More Information", command = INFOMENU,
        background = "grey", activebackground = "white"
                                                  )

        self.exitGameButton = tkinter.Button (
        self.frame, text = "Exit Game", command = self.wnd.destroy,
        background = "grey", activebackground = "white"
                                               )

        self.startGameButton.bind ("<Enter>", self.onEnterStartGame)
        self.startGameButton.bind ("<Leave>", self.onLeaveStartGame)
        self.gameSettingsButton.bind ("<Enter>", self.onEnterSettings)
        self.gameSettingsButton.bind ("<Leave>", self.onLeaveSettings)
        self.informationButton.bind ("<Enter>", self.onEnterInfo)
        self.informationButton.bind ("<Leave>", self.onLeaveInfo)
        self.exitGameButton.bind ("<Enter>", self.onEnterExit)
        self.exitGameButton.bind ("<Leave>", self.onLeaveExit)
        self.frame.pack (fill = tkinter.BOTH, expand = 1)
        # self.backgroundImage.pack (expand = 1, fill = tkinter.BOTH)
        self.gameTitle.pack (pady = 45, ipadx = 15)
        self.startGameButton.pack (pady = 25, ipadx = 15)
        self.gameSettingsButton.pack (pady = 25, ipadx = 15)
        self.informationButton.pack (pady = 25, ipadx = 15)
        self.exitGameButton.pack (pady = 25, ipadx = 15)
        self.wnd.mainloop ()

    def onEnterStartGame (self, event):
        # This function registers if the mouse is on the Start Game button.
        self.startGameButton["background"] = "red"

    def onLeaveStartGame (self, event):
        # This function registers if the mouse is not on the Start Game button.
        self.startGameButton["background"] = "grey"

    def onEnterSettings (self, event):
        # This function registers if the mouse is on the Settings button.
        self.gameSettingsButton["background"] = "red"

    def onLeaveSettings (self, event):
        # This function registers if the mouse is not on the Settings button.
        self.gameSettingsButton["background"] = "grey"

    def onEnterInfo (self, event):
        # This function registers if the mouse is on the More Info button.
        self.informationButton["background"] = "red"

    def onLeaveInfo (self, event):
        # This function registers if the mouse is not on the More Info button.
        self.informationButton["background"] = "grey"

    def onEnterExit (self, event):
        # This function registers if the mouse is on the Exit Game button.
        self.exitGameButton["background"] = "red"

    def onLeaveExit (self, event):
        # This function registers if the mouse is not on the Exit Game button.
        self.exitGameButton["background"] = "grey"

    def startGame (self):
        # This function executes the Start Game button
        self.wnd.destroy ()
        STARTGAME ()


class INFOMENU:
    # This class is for the Information window.

    def __init__ (self):
        self.wnd = tkinter.Tk ()
        self.wnd.geometry ("400x400")
        self.frame = tkinter.Frame (self.wnd)

        self.informationlabel = tkinter.Label (
        self.frame, text = "This is a choice based game"
                                                )

        self.informationlabel2 = tkinter.Label (
        self.frame, text = "The game changes story every time it's started"
                                                 )

        self.informationlabel3 = tkinter.Label (
        self.frame, text = "Click a button to make a choice"
                                                 )
        self.frame.pack ()
        self.informationlabel.pack (pady = 25)
        self.informationlabel2.pack(pady = 25)
        self.informationlabel3.pack (pady = 25)


class GAMESETTINGS:
    # This class is for the startup menu settings screen.
    lightingChoice = 100
    def __init__ (self):
        self.wnd = tkinter.Tk ()
        self.wnd.geometry ("400x400")
        self.autoReaderState = tkinter.IntVar ()
        self.frame = tkinter.Frame (self.wnd)
        self.lightingLabel = tkinter.Label (self.frame, text = "Lighting Preference:")

        self.lightingSlider = tkinter.Scale (self.frame, from_ = 0, to = 200,
        orient = tkinter.HORIZONTAL
                                              )
        self.lightingSlider.bind ("<ButtonRelease-1>", self.lightingSliderChange)

        self.autoReaderCheckBox = tkinter.Checkbutton (self.frame, text = "Auto Reader",
        variable = self.autoReaderState
                                                        )

        self.autoReaderLabel = tkinter.Label (
        self.frame, text = "Auto Reader Speed:"
                                               )

        self.autoReaderSlider = tkinter.Scale (
        self.frame, from_ = 0, to = 200, orient = tkinter.HORIZONTAL
                                                )

        self.autoReaderSlider.bind ("<ButtonRelease-1>", self.autoReaderChange)
        self.applyButton = tkinter.Button (self.frame, text = "Apply",
        command = self.buttonApply
                                            )

        self.autoReaderSlider.set (100)
        self.lightingSlider.set (100)
        self.frame.pack ()
        self.lightingLabel.pack ()
        self.lightingSlider.pack ()
        self.autoReaderCheckBox.pack ()
        self.autoReaderLabel.pack ()
        self.autoReaderSlider.pack ()
        self.applyButton.pack ()
        self.wnd.mainloop ()

    def lightingSliderChange (self, event):
        # This fucntion is to register the change in the Lighting slider
        self.lightingChoice = self.lightingSlider.get ()

    def autoReaderChange (self, event):
        # This fucntion is to register the  change in the Auto Reader slider.
        self.autoReaderChoice = self.autoReaderSlider.get ()

    def autoReaderCheckBoxChange (self, event):
        # This functino might be removed.
        self.checkBoxResult = self.autoReaderState.get ()

    def buttonApply (self):
        # This fucntion excutes the Apply button.
        # The Apply button applies all of the changes done in settings.
        if type (self.lightingChoice) == int:
            self.lightingSlider.set (self.lightingChoice)
        self.autoReaderChoice = self.autoReaderSlider.get ()


class STARTGAME:
    # This class is for the GUI inside the game.

    score = 0
    firstChoiceList = [
    "Solve it!", "Summon Satan", "Keivin", "Apologies", "Go back to sleep"
                        ]
    secondChoiceList = [
    "Don't solve it.", "Summon Satan", "Prof Sak Wip"
                         ]
    thirdChoiceList = [
    "Summon a demon", "Don't summon Satan", "Talabat Guy"
                        ]
    orderOfChoices = []

    characterNameList = [
    "James Pardew", "Xiao Ling", "Alpha", "Issac III", "Sir Buckethead",
    "Sam O'nella", "Amloaf Ingit", "Ann Iam Theoskroos", "Tom Scott", "Smoky The Cat"
                          ]

    def __init__ (self):
        self.wnd = tkinter.Tk ()
        # self.mainFrame = tkinter.Frame (self.wnd, background = "black")
        self.wnd.geometry ("500x600")
        self.firstFrame = tkinter.Frame (self.wnd, background = "brown")
        self.secondFrame = tkinter.Frame (self.wnd, background = "black")
        self.canvas = tkinter.Canvas (self.wnd, background = "yellow")

        self.firstChoiceButton = tkinter.Button (
        self.firstFrame, text = "First Choice",
        background = "grey", command = self.firstChoice
                                                  )

        self.secondChoiceButton = tkinter.Button (
        self.firstFrame, text = "Second Choice",
        background = "grey", command = self.secondChoice
                                                   )

        self.thirdChoiceButton = tkinter.Button (
        self.firstFrame, text = "Third Choice",
        background = "grey", command = self.thirdChoice
                                                  )
        self.dialogLabel = tkinter.Label (
        self.secondFrame, text = "You are about to start the game!",
        background = "brown"
                                           )

        self.characterNameFrame = tkinter.Frame (
        self.dialogLabel, background = "brown"
                                                  )

        self.characterNameLabel = tkinter.Label (
        self.characterNameFrame, text = "Swapnendu Sanyal",background = "brown"
                                                  )

        self.dialogLabel.bind ("<Button-1>", self.func)

        self.canvas.pack (fill = tkinter.BOTH, expand = 1)
        self.firstFrame.pack (fill = tkinter.BOTH)
        self.secondFrame.pack ()

        self.firstChoiceButton.pack (
        side = tkinter.LEFT, ipadx = 45, ipady = 10
                                      )

        self.secondChoiceButton.pack (
        side = tkinter.LEFT, ipadx = 45, ipady = 10
                                       )

        self.thirdChoiceButton.pack (
        side = tkinter.LEFT, ipadx = 45, ipady = 10
                                      )

        self.dialogLabel.pack (ipady = 30, ipadx = 200, side = tkinter.LEFT)
        self.characterNameFrame.pack (fill = tkinter.BOTH)
        self.characterNameLabel.pack (side = tkinter.LEFT, ipady = 10)
        self.dialogMaker ()

    def firstChoice (self):
        # This function is for registering the left most button clicks.
        self.score += 1
        self.orderOfChoices.append (1)

        self.dialogMaker ()

    def secondChoice (self):
        # This function is for registering the middle button click.
        self.score += 2
        self.orderOfChoices.append (2)

        self.dialogMaker ()

    def thirdChoice (self):
        # This function is for registering the right most button clicks.
        self.score += 3
        self.orderOfChoices.append (3)

        self.dialogMaker ()
        return

    def dialogMaker (self):
        temp = random.randint (0, 9)
        self.secondFrame.pack_forget ()
        self.firstFrame.pack_forget ()
        self.secondFrame.pack ()

        if self.score == 0:
            self.characterNameLabel.configure (text = self.characterNameList [temp])
            self.dialogLabel.configure (text = "Hey Swapnendu Sanyal, Good morning!")
            self.func ()
            self.characterNameLabel.configure (text = "Swapnendu Sanyal")
            self.dialogLabel.configure (text = "How long have i been sleeping?")
            self.func ()
            self.characterNameLabel.configure (text = self.characterNameList [temp])
            self.dialogLabel.configure (text = "About 7 kilometers")
            self.func ()
            self.characterNameLabel.configure (text = "Swapnendu Sanyal")
            self.dialogLabel.configure (text = "Wha... 7 kilometers?")
            self.func ()
            temp = random.randint (0, 9)
            self.characterNameLabel.configure (text = self.characterNameList [temp])
            self.dialogLabel.configure (text = "Yes! You see...")
            self.func ()
            self.characterNameLabel.configure (text = self.characterNameList [temp])
            self.dialogLabel.configure (text = "When you took 16-113 class...")
            self.func ()
            self.characterNameLabel.configure (text = self.characterNameList [temp])
            self.dialogLabel.configure (text = "An old curse fell on you")
            self.func ()
            self.characterNameLabel.configure (text = "Swapnendu Sanyal")
            self.dialogLabel.configure (text = "Why is your name changing?")
            self.func ()
            temp = random.randint (0, 9)
            self.characterNameLabel.configure (text = self.characterNameList [temp])
            self.dialogLabel.configure (text = "...")
            self.func ()
            self.characterNameLabel.configure (text = "Swapnendu Sanyal")
            self.dialogLabel.configure (text = "...")
            self.func ()
            self.characterNameLabel.configure (text = "Game Dev")
            self.dialogLabel.configure (text = "...")
            self.func ()
            temp = random.randint (0, 9)
            self.characterNameLabel.configure (text = self.characterNameList [temp])
            self.dialogLabel.configure (text = "Well, i should tell you..")
            self.func ()
            temp = random.randint (0, 9)
            self.characterNameLabel.configure (text = self.characterNameList [temp])
            self.dialogLabel.configure (text = "This curse make you forced to solve puzzles")
            self.func ()
            temp = random.randint (0, 9)
            self.characterNameLabel.configure (text = self.characterNameList [temp])
            self.dialogLabel.configure (text = "Here, see this puzzle:")
            self.func ()
            self.secondFrame.pack_forget ()
            self.firstFrame.pack ()
            self.secondFrame.pack ()

            self.firstChoiceButton.configure (
            text = self.firstChoiceList [0]
                                               )

            self.secondChoiceButton.configure (
            text = self.secondChoiceList [0]
                                                )

            self.thirdChoiceButton.configure (
            text = self.thirdChoiceList [0]
                                               )
        elif self.score == 1:
            messagebox.showinfo ("Game Info", "Put 8 Queens in a way where the can't attack")
            tempRes = QUEENSGAME ()
            if tempRes:
                self.characterNameLabel.configure (text = "Fake Q")
                self.dialogLabel.configure (text = "Hey bro!")
                self.func ()
                self.characterNameLabel.configure (text = "Q")
                self.dialogLabel.configure (text = "Yes bro!")
                self.func ()
                self.characterNameLabel.configure (text = "Q")
                self.dialogLabel.configure (text = "Yes bro!")
                self.func ()
                self.characterNameLabel.configure (text = "Fake Q")
                self.dialogLabel.configure (text = "See I'm you, Q")
                self.func ()
                self.characterNameLabel.configure (text = "Q")
                self.dialogLabel.configure (text = "Huh?")
                self.func ()
                self.characterNameLabel.configure (text = "Fake Q")
                self.dialogLabel.configure (text = "C I'm you Q")
                self.func ()
                self.characterNameLabel.configure (text = "Q")
                self.dialogLabel.configure (text = "...")
                self.func ()
                self.characterNameLabel.configure (text = "Fake Q")
                self.dialogLabel.configure (text = "C M U Q")
                self.func ()
                self.characterNameLabel.configure (text = "Q")
                self.dialogLabel.configure (text = "*Sigh*")
                self.func ()
                self.wnd.destroy ()
            else:
                self.characterNameLabel.configure (text = "Swapnendu Sanyal")
                self.dialogLabel.configure (text = "Why is this so hard?")
                self.func ()

                self.secondFrame.pack_forget ()
                self.firstFrame.pack ()
                self.secondFrame.pack ()

                self.firstChoiceButton.configure (
                text = self.firstChoiceList [1]
                                                   )

                self.secondChoiceButton.configure (
                text = self.secondChoiceList [1]
                                                    )

                self.thirdChoiceButton.configure (
                text = self.thirdChoiceList [1]
                                                   )

        elif self.orderOfChoices == [1, 1] or self.orderOfChoices == [1, 2] or self. orderOfChoices == [2, 1] or self. orderOfChoices == [2, 2]:
            self.characterNameLabel.configure (text = "Luicfer Morningstar")
            self.dialogLabel.configure (text = "Bloody hell! Who is this?")
            self.func ()
            self.characterNameLabel.configure (text = "Swapnendu Sanyal")
            self.dialogLabel.configure (text = "I'm...")
            self.func ()

            self.secondFrame.pack_forget ()
            self.firstFrame.pack ()
            self.secondFrame.pack ()

            self.firstChoiceButton.configure (
            text = self.firstChoiceList [2]
                                               )

            self.secondChoiceButton.configure (
            text = self.secondChoiceList [2]
                                                )

            self.thirdChoiceButton.configure (
            text = self.thirdChoiceList [2]
                                               )

        elif self.orderOfChoices == [1, 1, 1] or self. orderOfChoices == [2, 1, 1]:
            self.characterNameLabel.configure (text = "")
            self.dialogLabel.configure (text = "*Luicfer Stabs you to death*")
            self.func ()
            self.characterNameLabel.configure (text = "")
            self.dialogLabel.configure (text = "Game Over")
            self.func ()

        elif self.orderOfChoices == [1, 1, 2]:
            self.characterNameLabel.configure (text = "Lucifer Morningstar")
            self.dialogLabel.configure (text = "*Runs away*")
            self.func ()
            self.characterNameLabel.configure (text = "")
            self.dialogLabel.configure (text = "What has Prof Sak Wip done to him?")
            self.func ()

        elif self.orderOfChoices == [1, 1, 3]:
            self.characterNameLabel.configure (text = "Lucifer Morningstar")
            self.dialogLabel.configure (text = "*Runs away*")
            self.func ()
            self.characterNameLabel.configure (text = "")
            self.dialogLabel.configure (text = "What has Taabat done to him?")
            self.func ()

        elif self.orderOfChoices == [2]:
            self.characterNameLabel.configure (text = "")
            self.dialogLabel.configure (text = "Before you realize you start solving it")
            self.func ()

        elif self.orderOfChoices == [3]:
            self.characterNameLabel.configure (text = "A weird figure")
            self.dialogLabel.configure (text = "Who dare startle me today?")
            self.func ()
            self.characterNameLabel.configure (text = "Swapnendu Sanyal")
            self.dialogLabel.configure (text = "It's-a me..")
            self.func ()
            self.characterNameLabel.configure (text = "Prof Sak Wip")
            self.dialogLabel.configure (text = "Don't say it...")
            self.func ()
            self.characterNameLabel.configure (text = "Swapnendu Sanyal")
            self.dialogLabel.configure (text = "...Mario")
            self.func ()
            self.characterNameLabel.configure (text = "Prof Sak Wip")
            self.dialogLabel.configure (text = "That's it you're getting an F")
            self.func ()

    def func (self):
        return


class QUEENSGAME:

    buttonsDict = {}
    chosen = 0
    success = False
    def __init__ (self):
        self.wnd = tkinter.Tk ()
        self.wnd.geometry ("600x608")
        self.firstFrame = tkinter.Frame (self.wnd, background = "blue")
        self.secondFrame = tkinter.Frame (self.wnd)
        self.thirdFrame = tkinter.Frame (self.wnd)
        self.fourthFrame = tkinter.Frame (self.wnd)
        self.fifthFrame = tkinter.Frame (self.wnd)
        self.sixthFrame = tkinter.Frame (self.wnd)
        self.seventhFrame = tkinter.Frame (self.wnd)
        self.eighthFrame = tkinter.Frame (self.wnd, background = "blue")
        self.buttonsCreator ()

        self.A1 = tkinter.Button (self.firstFrame, background = "black", command = self.A1ButtonsClicked)
        self.A2 = tkinter.Button (self.firstFrame, background = "White", command = self.A2ButtonsClicked)
        self.A3 = tkinter.Button (self.firstFrame, background = "black", command = self.A3ButtonsClicked)
        self.A4 = tkinter.Button (self.firstFrame, background = "White", command = self.A4ButtonsClicked)
        self.A5 = tkinter.Button (self.firstFrame, background = "black", command = self.A5ButtonsClicked)
        self.A6 = tkinter.Button (self.firstFrame, background = "White", command = self.A6ButtonsClicked)
        self.A7 = tkinter.Button (self.firstFrame, background = "black", command = self.A7ButtonsClicked)
        self.A8 = tkinter.Button (self.firstFrame, background = "White", command = self.A8ButtonsClicked)
        self.B1 = tkinter.Button (self.secondFrame, background = "White", command = self.B1ButtonsClicked)
        self.B2 = tkinter.Button (self.secondFrame, background = "black", command = self.B2ButtonsClicked)
        self.B3 = tkinter.Button (self.secondFrame, background = "White", command = self.B3ButtonsClicked)
        self.B4 = tkinter.Button (self.secondFrame, background = "black", command = self.B4ButtonsClicked)
        self.B5 = tkinter.Button (self.secondFrame, background = "White", command = self.B5ButtonsClicked)
        self.B6 = tkinter.Button (self.secondFrame, background = "black", command = self.B6ButtonsClicked)
        self.B7 = tkinter.Button (self.secondFrame, background = "White", command = self.B7ButtonsClicked)
        self.B8 = tkinter.Button (self.secondFrame, background = "black", command = self.B8ButtonsClicked)
        self.C1 = tkinter.Button (self.thirdFrame, background = "black", command = self.C1ButtonsClicked)
        self.C2 = tkinter.Button (self.thirdFrame, background = "White", command = self.C2ButtonsClicked)
        self.C3 = tkinter.Button (self.thirdFrame, background = "black", command = self.C3ButtonsClicked)
        self.C4 = tkinter.Button (self.thirdFrame, background = "White", command = self.C4ButtonsClicked)
        self.C5 = tkinter.Button (self.thirdFrame, background = "black", command = self.C5ButtonsClicked)
        self.C6 = tkinter.Button (self.thirdFrame, background = "White", command = self.C6ButtonsClicked)
        self.C7 = tkinter.Button (self.thirdFrame, background = "black", command = self.C7ButtonsClicked)
        self.C8 = tkinter.Button (self.thirdFrame, background = "White", command = self.C8ButtonsClicked)
        self.D1 = tkinter.Button (self.fourthFrame, background = "White", command = self.D1ButtonsClicked)
        self.D2 = tkinter.Button (self.fourthFrame, background = "black", command = self.D2ButtonsClicked)
        self.D3 = tkinter.Button (self.fourthFrame, background = "White", command = self.D3ButtonsClicked)
        self.D4 = tkinter.Button (self.fourthFrame, background = "black", command = self.D4ButtonsClicked)
        self.D5 = tkinter.Button (self.fourthFrame, background = "White", command = self.D5ButtonsClicked)
        self.D6 = tkinter.Button (self.fourthFrame, background = "black", command = self.D6ButtonsClicked)
        self.D7 = tkinter.Button (self.fourthFrame, background = "White", command = self.D7ButtonsClicked)
        self.D8 = tkinter.Button (self.fourthFrame, background = "black", command = self.D8ButtonsClicked)
        self.E1 = tkinter.Button (self.fifthFrame, background = "black", command = self.E1ButtonsClicked)
        self.E2 = tkinter.Button (self.fifthFrame, background = "White", command = self.E2ButtonsClicked)
        self.E3 = tkinter.Button (self.fifthFrame, background = "black", command = self.E3ButtonsClicked)
        self.E4 = tkinter.Button (self.fifthFrame, background = "White", command = self.E4ButtonsClicked)
        self.E5 = tkinter.Button (self.fifthFrame, background = "black", command = self.E5ButtonsClicked)
        self.E6 = tkinter.Button (self.fifthFrame, background = "White", command = self.E6ButtonsClicked)
        self.E7 = tkinter.Button (self.fifthFrame, background = "black", command = self.E7ButtonsClicked)
        self.E8 = tkinter.Button (self.fifthFrame, background = "White", command = self.E8ButtonsClicked)
        self.F1 = tkinter.Button (self.sixthFrame, background = "White", command = self.F1ButtonsClicked)
        self.F2 = tkinter.Button (self.sixthFrame, background = "black", command = self.F2ButtonsClicked)
        self.F3 = tkinter.Button (self.sixthFrame, background = "White", command = self.F3ButtonsClicked)
        self.F4 = tkinter.Button (self.sixthFrame, background = "black", command = self.F4ButtonsClicked)
        self.F5 = tkinter.Button (self.sixthFrame, background = "White", command = self.F5ButtonsClicked)
        self.F6 = tkinter.Button (self.sixthFrame, background = "black", command = self.F6ButtonsClicked)
        self.F7 = tkinter.Button (self.sixthFrame, background = "White", command = self.F7ButtonsClicked)
        self.F8 = tkinter.Button (self.sixthFrame, background = "black", command = self.F8ButtonsClicked)
        self.G1 = tkinter.Button (self.seventhFrame, background = "black", command = self.G1ButtonsClicked)
        self.G2 = tkinter.Button (self.seventhFrame, background = "White", command = self.G2ButtonsClicked)
        self.G3 = tkinter.Button (self.seventhFrame, background = "black", command = self.G3ButtonsClicked)
        self.G4 = tkinter.Button (self.seventhFrame, background = "White", command = self.G4ButtonsClicked)
        self.G5 = tkinter.Button (self.seventhFrame, background = "black", command = self.G5ButtonsClicked)
        self.G6 = tkinter.Button (self.seventhFrame, background = "White", command = self.G6ButtonsClicked)
        self.G7 = tkinter.Button (self.seventhFrame, background = "black", command = self.G7ButtonsClicked)
        self.G8 = tkinter.Button (self.seventhFrame, background = "White", command = self.G8ButtonsClicked)
        self.H1 = tkinter.Button (self.eighthFrame, background = "White", command = self.H1ButtonsClicked)
        self.H2 = tkinter.Button (self.eighthFrame, background = "black", command = self.H2ButtonsClicked)
        self.H3 = tkinter.Button (self.eighthFrame, background = "White", command = self.H3ButtonsClicked)
        self.H4 = tkinter.Button (self.eighthFrame, background = "black", command = self.H4ButtonsClicked)
        self.H5 = tkinter.Button (self.eighthFrame, background = "White", command = self.H5ButtonsClicked)
        self.H6 = tkinter.Button (self.eighthFrame, background = "black", command = self.H6ButtonsClicked)
        self.H7 = tkinter.Button (self.eighthFrame, background = "White", command = self.H7ButtonsClicked)
        self.H8 = tkinter.Button (self.eighthFrame, background = "black", command = self.H8ButtonsClicked)

        self.firstFrame.pack (fill = tkinter.BOTH)
        self.secondFrame.pack (fill = tkinter.BOTH)
        self.thirdFrame.pack (fill = tkinter.BOTH)
        self.fourthFrame.pack (fill = tkinter.BOTH)
        self.fifthFrame.pack (fill = tkinter.BOTH)
        self.sixthFrame.pack (fill = tkinter.BOTH)
        self.seventhFrame.pack (fill = tkinter.BOTH)
        self.eighthFrame.pack (fill = tkinter.BOTH)

        self.A1.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.A2.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.A3.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.A4.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.A5.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.A6.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.A7.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.A8.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.B1.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.B2.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.B3.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.B4.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.B5.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.B6.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.B7.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.B8.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.C1.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.C2.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.C3.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.C4.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.C5.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.C6.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.C7.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.C8.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.D1.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.D2.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.D3.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.D4.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.D5.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.D6.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.D7.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.D8.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.E1.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.E2.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.E3.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.E4.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.E5.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.E6.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.E7.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.E8.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.F1.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.F2.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.F3.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.F4.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.F5.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.F6.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.F7.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.F8.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.G1.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.G2.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.G3.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.G4.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.G5.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.G6.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.G7.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.G8.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.H1.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.H2.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.H3.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.H4.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.H5.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.H6.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.H7.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)
        self.H8.pack (side = tkinter.LEFT, ipadx = 32, ipady = 25)

    def buttonsCreator (self):
        self.buttonsList = []
        for i in range (1, 65):
            self.buttonsList.append (i)

        for k in self.buttonsList:
            self.buttonsDict [k] = 0

        return

    def A1ButtonsClicked (self):
        if self.buttonsDict [1] == 0:
            self.buttonsDict [1] = 1
            self.A1.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [1] = 0
            self.A1.configure (background = "black")
            self.chosen -= 1
        self.endReached ()
        return

    def A2ButtonsClicked (self):
        if self.buttonsDict [2] == 0:
            self.buttonsDict [2] = 1
            self.A2.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [2] = 0
            self.A2.configure (background = "white")
            self.chosen -= 1
        self.endReached ()
        return

    def A3ButtonsClicked (self):
        if self.buttonsDict [3] == 0:
            self.buttonsDict [3] = 1
            self.A3.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [3] = 0
            self.A3.configure (background = "black")
            self.chosen -= 1
        self.endReached ()
        return

    def A4ButtonsClicked (self):
        if self.buttonsDict [4] == 0:
            self.buttonsDict [4] = 1
            self.A4.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [4] = 0
            self.A4.configure (background = "white")
            self.chosen -= 1
        self.endReached ()
        return

    def A5ButtonsClicked (self):
        if self.buttonsDict [5] == 0:
            self.buttonsDict [5] = 1
            self.A5.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [5] = 0
            self.A5.configure (background = "black")
            self.chosen -= 1
        self.endReached ()
        return

    def A6ButtonsClicked (self):
        if self.buttonsDict [6] == 0:
            self.buttonsDict [6] = 1
            self.A6.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [6] = 0
            self.A6.configure (background = "white")
            self.chosen -= 1
        self.endReached ()
        return

    def A7ButtonsClicked (self):
        if self.buttonsDict [7] == 0:
            self.buttonsDict [7] = 1
            self.A7.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [7] = 0
            self.A7.configure (background = "black")
            self.chosen -= 1
        self.endReached ()
        return

    def A8ButtonsClicked (self):
        if self.buttonsDict [8] == 0:
            self.buttonsDict [8] = 1
            self.A8.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [8] = 0
            self.A8.configure (background = "white")
            self.chosen -= 1
        self.endReached ()
        return

    def B1ButtonsClicked (self):
        if self.buttonsDict [9] == 0:
            self.buttonsDict [9] = 1
            self.B1.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [9] = 0
            self.B1.configure (background = "white")
            self.chosen -= 1
        self.endReached ()
        return

    def B2ButtonsClicked (self):
        if self.buttonsDict [10] == 0:
            self.buttonsDict [10] = 1
            self.B2.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [10] = 0
            self.B2.configure (background = "black")
            self.chosen -= 1
        self.endReached ()
        return

    def B3ButtonsClicked (self):
        if self.buttonsDict [11] == 0:
            self.buttonsDict [11] = 1
            self.B3.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [11] = 0
            self.B3.configure (background = "white")
            self.chosen -= 1
        self.endReached ()
        return

    def B4ButtonsClicked (self):
        if self.buttonsDict [12] == 0:
            self.buttonsDict [12] = 1
            self.B4.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [12] = 0
            self.B4.configure (background = "black")
            self.chosen -= 1
        self.endReached ()
        return

    def B5ButtonsClicked (self):
        if self.buttonsDict [13] == 0:
            self.buttonsDict [13] = 1
            self.B5.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [13] = 0
            self.B5.configure (background = "white")
            self.chosen -= 1
        self.endReached ()
        return

    def B6ButtonsClicked (self):
        if self.buttonsDict [14] == 0:
            self.buttonsDict [14] = 1
            self.B6.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [14] = 0
            self.B6.configure (background = "black")
            self.chosen -= 1
        self.endReached ()
        return

    def B7ButtonsClicked (self):
        if self.buttonsDict [15] == 0:
            self.buttonsDict [15] = 1
            self.B7.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [15] = 0
            self.B7.configure (background = "white")
            self.chosen -= 1
        self.endReached ()
        return

    def B8ButtonsClicked (self):
        if self.buttonsDict [16] == 0:
            self.buttonsDict [16] = 1
            self.B8.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [16] = 0
            self.B8.configure (background = "black")
            self.chosen -= 1
        self.endReached ()
        return

    def C1ButtonsClicked (self):
        if self.buttonsDict [17] == 0:
            self.buttonsDict [17] = 1
            self.C1.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [17] = 0
            self.C1.configure (background = "black")
            self.chosen -= 1
        self.endReached ()
        return

    def C2ButtonsClicked (self):
        if self.buttonsDict [18] == 0:
            self.buttonsDict [18] = 1
            self.C2.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [18] = 0
            self.C2.configure (background = "white")
            self.chosen -= 1
        self.endReached ()
        return

    def C3ButtonsClicked (self):
        if self.buttonsDict [19] == 0:
            self.buttonsDict [19] = 1
            self.C3.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [19] = 0
            self.C3.configure (background = "black")
            self.chosen -= 1
        self.endReached ()
        return

    def C4ButtonsClicked (self):
        if self.buttonsDict [20] == 0:
            self.buttonsDict [20] = 1
            self.C4.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [20] = 0
            self.C4.configure (background = "white")
            self.chosen -= 1
        self.endReached ()
        return

    def C5ButtonsClicked (self):
        if self.buttonsDict [21] == 0:
            self.buttonsDict [21] = 1
            self.C5.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [21] = 0
            self.C5.configure (background = "black")
            self.chosen -= 1
        self.endReached ()
        return

    def C6ButtonsClicked (self):
        if self.buttonsDict [22] == 0:
            self.buttonsDict [22] = 1
            self.C6.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [22] = 0
            self.C6.configure (background = "white")
            self.chosen -= 1
        self.endReached ()
        return

    def C7ButtonsClicked (self):
        if self.buttonsDict [23] == 0:
            self.buttonsDict [23] = 1
            self.C7.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [23] = 0
            self.C7.configure (background = "black")
            self.chosen -= 1
        self.endReached ()
        return

    def C8ButtonsClicked (self):
        if self.buttonsDict [24] == 0:
            self.buttonsDict [24] = 1
            self.C8.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [24] = 0
            self.C8.configure (background = "white")
            self.chosen -= 1
        self.endReached ()
        return

    def D1ButtonsClicked (self):
        if self.buttonsDict [25] == 0:
            self.buttonsDict [25] = 1
            self.D1.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [25] = 0
            self.D1.configure (background = "white")
            self.chosen -= 1
        self.endReached ()
        return

    def D2ButtonsClicked (self):
        if self.buttonsDict [26] == 0:
            self.buttonsDict [26] = 1
            self.D2.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [26] = 0
            self.D2.configure (background = "black")
            self.chosen -= 1
        self.endReached ()
        return

    def D3ButtonsClicked (self):
        if self.buttonsDict [27] == 0:
            self.buttonsDict [27] = 1
            self.D3.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [27] = 0
            self.D3.configure (background = "white")
            self.chosen -= 1
        self.endReached ()
        return

    def D4ButtonsClicked (self):
        if self.buttonsDict [28] == 0:
            self.buttonsDict [28] = 1
            self.D4.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [28] = 0
            self.D4.configure (background = "black")
            self.chosen -= 1
        self.endReached ()
        return

    def D5ButtonsClicked (self):
        if self.buttonsDict [29] == 0:
            self.buttonsDict [29] = 1
            self.D5.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [29] = 0
            self.D5.configure (background = "white")
            self.chosen -= 1
        self.endReached ()
        return

    def D6ButtonsClicked (self):
        if self.buttonsDict [30] == 0:
            self.buttonsDict [30] = 1
            self.D6.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [30] = 0
            self.D6.configure (background = "black")
            self.chosen -= 1
        self.endReached ()
        return

    def D7ButtonsClicked (self):
        if self.buttonsDict [31] == 0:
            self.buttonsDict [31] = 1
            self.D7.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [31] = 0
            self.D7.configure (background = "white")
            self.chosen -= 1
        self.endReached ()
        return

    def D8ButtonsClicked (self):
        if self.buttonsDict [32] == 0:
            self.buttonsDict [32] = 1
            self.D8.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [32] = 0
            self.D8.configure (background = "black")
            self.chosen -= 1
        self.endReached ()
        return

    def E1ButtonsClicked (self):
        if self.buttonsDict [33] == 0:
            self.buttonsDict [33] = 1
            self.E1.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [33] = 0
            self.E1.configure (background = "black")
            self.chosen -= 1
        self.endReached ()
        return

    def E2ButtonsClicked (self):
        if self.buttonsDict [34] == 0:
            self.buttonsDict [34] = 1
            self.E2.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [34] = 0
            self.E2.configure (background = "white")
            self.chosen -= 1
        self.endReached ()
        return

    def E3ButtonsClicked (self):
        if self.buttonsDict [35] == 0:
            self.buttonsDict [35] = 1
            self.E3.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [35] = 0
            self.E3.configure (background = "black")
            self.chosen -= 1
        self.endReached ()
        return

    def E4ButtonsClicked (self):
        if self.buttonsDict [36] == 0:
            self.buttonsDict [36] = 1
            self.E4.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [36] = 0
            self.E4.configure (background = "white")
            self.chosen -= 1
        self.endReached ()
        return

    def E5ButtonsClicked (self):
        if self.buttonsDict [37] == 0:
            self.buttonsDict [37] = 1
            self.E5.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [37] = 0
            self.E5.configure (background = "black")
            self.chosen -= 1
        self.endReached ()
        return

    def E6ButtonsClicked (self):
        if self.buttonsDict [38] == 0:
            self.buttonsDict [38] = 1
            self.E6.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [38] = 0
            self.E6.configure (background = "white")
            self.chosen -= 1
        self.endReached ()
        return

    def E7ButtonsClicked (self):
        if self.buttonsDict [39] == 0:
            self.buttonsDict [39] = 1
            self.E7.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [39] = 0
            self.E7.configure (background = "black")
            self.chosen -= 1
        self.endReached ()
        return

    def E8ButtonsClicked (self):
        if self.buttonsDict [40] == 0:
            self.buttonsDict [40] = 1
            self.E8.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [40] = 0
            self.E8.configure (background = "white")
            self.chosen -= 1
        self.endReached ()
        return

    def F1ButtonsClicked (self):
        if self.buttonsDict [41] == 0:
            self.buttonsDict [41] = 1
            self.F1.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [41] = 0
            self.F1.configure (background = "white")
            self.chosen -= 1
        self.endReached ()
        return

    def F2ButtonsClicked (self):
        if self.buttonsDict [42] == 0:
            self.buttonsDict [42] = 1
            self.F2.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [42] = 0
            self.F2.configure (background = "black")
            self.chosen -= 1
        self.endReached ()
        return

    def F3ButtonsClicked (self):
        if self.buttonsDict [43] == 0:
            self.buttonsDict [43] = 1
            self.F3.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [43] = 0
            self.F3.configure (background = "white")
            self.chosen -= 1
        self.endReached ()
        return

    def F4ButtonsClicked (self):
        if self.buttonsDict [44] == 0:
            self.buttonsDict [44] = 1
            self.F4.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [44] = 0
            self.F4.configure (background = "black")
            self.chosen -= 1
        self.endReached ()
        return

    def F5ButtonsClicked (self):
        if self.buttonsDict [45] == 0:
            self.buttonsDict [45] = 1
            self.F5.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [45] = 0
            self.F5.configure (background = "white")
            self.chosen -= 1
        self.endReached ()
        return

    def F6ButtonsClicked (self):
        if self.buttonsDict [46] == 0:
            self.buttonsDict [46] = 1
            self.F6.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [46] = 0
            self.F6.configure (background = "black")
            self.chosen -= 1
        self.endReached ()
        return

    def F7ButtonsClicked (self):
        if self.buttonsDict [47] == 0:
            self.buttonsDict [47] = 1
            self.F7.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [47] = 0
            self.F7.configure (background = "white")
            self.chosen -= 1
        self.endReached ()
        return

    def F8ButtonsClicked (self):
        if self.buttonsDict [48] == 0:
            self.buttonsDict [48] = 1
            self.F8.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [48] = 0
            self.F8.configure (background = "black")
            self.chosen -= 1
        self.endReached ()
        return

    def G1ButtonsClicked (self):
        if self.buttonsDict [49] == 0:
            self.buttonsDict [49] = 1
            self.G1.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [49] = 0
            self.G1.configure (background = "black")
            self.chosen -= 1
        self.endReached ()
        return

    def G2ButtonsClicked (self):
        if self.buttonsDict [50] == 0:
            self.buttonsDict [50] = 1
            self.G2.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [50] = 0
            self.G2.configure (background = "white")
            self.chosen -= 1
        self.endReached ()
        return

    def G3ButtonsClicked (self):
        if self.buttonsDict [51] == 0:
            self.buttonsDict [51] = 1
            self.G3.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [51] = 0
            self.G3.configure (background = "black")
            self.chosen -= 1
        self.endReached ()
        return

    def G4ButtonsClicked (self):
        if self.buttonsDict [52] == 0:
            self.buttonsDict [52] = 1
            self.G4.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [52] = 0
            self.G4.configure (background = "white")
            self.chosen -= 1
        self.endReached ()
        return

    def G5ButtonsClicked (self):
        if self.buttonsDict [53] == 0:
            self.buttonsDict [53] = 1
            self.G5.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [53] = 0
            self.G5.configure (background = "black")
            self.chosen -= 1
        self.endReached ()
        return

    def G6ButtonsClicked (self):
        if self.buttonsDict [54] == 0:
            self.buttonsDict [54] = 1
            self.G6.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [54] = 0
            self.G6.configure (background = "white")
            self.chosen -= 1
        self.endReached ()
        return

    def G7ButtonsClicked (self):
        if self.buttonsDict [55] == 0:
            self.buttonsDict [55] = 1
            self.G7.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [55] = 0
            self.G7.configure (background = "black")
            self.chosen -= 1
        self.endReached ()
        return

    def G8ButtonsClicked (self):
        if self.buttonsDict [56] == 0:
            self.buttonsDict [56] = 1
            self.G8.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [56] = 0
            self.G8.configure (background = "white")
            self.chosen -= 1
        self.endReached ()
        return

    def H1ButtonsClicked (self):
        if self.buttonsDict [57] == 0:
            self.buttonsDict [57] = 1
            self.H1.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [57] = 0
            self.H1.configure (background = "white")
            self.chosen -= 1
        self.endReached ()
        return

    def H2ButtonsClicked (self):
        if self.buttonsDict [58] == 0:
            self.buttonsDict [58] = 1
            self.H2.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [58] = 0
            self.H2.configure (background = "black")
            self.chosen -= 1
        self.endReached ()
        return

    def H3ButtonsClicked (self):
        if self.buttonsDict [59] == 0:
            self.buttonsDict [59] = 1
            self.H3.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [59] = 0
            self.H3.configure (background = "white")
            self.chosen -= 1
        self.endReached ()
        return

    def H4ButtonsClicked (self):
        if self.buttonsDict [60] == 0:
            self.buttonsDict [60] = 1
            self.H4.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [60] = 0
            self.H4.configure (background = "black")
            self.chosen -= 1
        self.endReached ()
        return

    def H5ButtonsClicked (self):
        if self.buttonsDict [61] == 0:
            self.buttonsDict [61] = 1
            self.H5.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [61] = 0
            self.H5.configure (background = "white")
            self.chosen -= 1
        self.endReached ()
        return

    def H6ButtonsClicked (self):
        if self.buttonsDict [62] == 0:
            self.buttonsDict [62] = 1
            self.H6.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [62] = 0
            self.H6.configure (background = "black")
            self.chosen -= 1
        self.endReached ()
        return

    def H7ButtonsClicked (self):
        if self.buttonsDict [63] == 0:
            self.buttonsDict [63] = 1
            self.H7.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [63] = 0
            self.H7.configure (background = "white")
            self.chosen -= 1
        self.endReached ()
        return

    def H8ButtonsClicked (self):
        if self.buttonsDict [64] == 0:
            self.buttonsDict [64] = 1
            self.H8.configure (background = "red")
            self.chosen += 1
        else:
            self.buttonsDict [64] = 0
            self.H8.configure (background = "black")
            self.chosen -= 1
        self.endReached ()
        return

    def endReached (self):
        if self.chosen == 8:
            self.giveResult ()
        else:
            return

    def giveResult (self):
        chosenOnes = []
        k = 0
        smallerValue = 0
        biggerValue = 0
        for i in self.buttonsDict.keys ():
            if self.buttonsDict [i] == 1:
                chosenOnes.append (i)

        while k < len (chosenOnes):
            for i in chosenOnes:
                if chosenOnes [k] != i:
                    if i == (chosenOnes [k] % 8):
                        if chosenOnes [k] % 8 == 0:
                            if (i // 8) == ((chosenOnes [k] // 8) - 1):
                                print ("1", i, chosenOnes [k])
                                self.resultMessageBox ()
                                return

                        elif (i % 9) == 0:
                            if ((i // 8) - 1) == (chosenOnes [k] // 8):
                                print ("2", i, chosenOnes [k])
                                self.resultMessageBox ()
                                return

                        elif ((i // 8)) == (chosenOnes [k] // 8):
                            print ("3", i, chosenOnes [k])
                            self.resultMessageBox ()
                            return

                    elif ((chosenOnes [k] - i) % 9) == 0:
                        print ("4", i, chosenOnes [k])
                        self.resultMessageBox ()
                        return

                    elif ((chosenOnes [k] - i) % 7) == 0:
                        if i < chosenOnes [k]:
                            if ((chosenOnes [k] - i) / 7) < (i):
                                print ("5", i, chosenOnes [k])
                                self.resultMessageBox ()
                                return
                        elif chosenOnes [k] < i:
                            print (i, chosenOnes [k])
                            if ((i - chosenOnes [k]) / 7) < (chosenOnes [k]):
                                print ("6", i, chosenOnes [k])
                                print ((i - chosenOnes [k]) / 7)
                                print (chosenOnes [k])
                                self.resultMessageBox ()
                                return

            k += 1
        self.success = True
        self.resultMessageBox ()
        return

    def resultMessageBox (self):
        if self.success == False:
            messagebox.showinfo ("Failed!", "You have failed the mini game")
        elif self.success == True:
            messagebox.showinfo ("Success!", "You did it! Here take this")
        self.wnd.destroy ()
        return



app = STARTUPMENU ()
