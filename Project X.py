import tkinter
from PIL import ImageTk, Image

class STARTUPMENU:
    # This class will include the startup menu of the game.

    def __init__ (self):
        self.wnd = tkinter.Tk ()
        self.wnd.geometry ("500x540")
        self.frame = tkinter.Frame (self.wnd, background = "black")
        # self.bgImage = ImageTk.PhotoImage (Image.open ("BG.jpg"))
        # self.backgroundImage = tkinter.Label (image = self.bgImage)
        self.gameTitle = tkinter.Label (self.frame, text = "GAME TITLE")
        self.startGameButton = tkinter.Button (self.frame, text = "Start Game", command = self.startGame, background = "grey", activebackground = "white")
        self.gameSettingsButton = tkinter.Button (self.frame, text = "Settings", command = GAMESETTINGS, background = "grey", activebackground = "white")
        self.informationButton = tkinter.Button (self.frame, text = "More Information", command = INFOMENU, background = "grey", activebackground = "white")
        self.exitGameButton = tkinter.Button (self.frame, text = "Exit Game", command = self.wnd.destroy, background = "grey", activebackground = "white")
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
        # This function registers if the mouse is on the More Information button.
        self.informationButton["background"] = "red"

    def onLeaveInfo (self, event):
        # This function registers if the mouse is not on the More Information button.
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
        self.informationlabel = tkinter.Label (self.frame, text = "Some text to inform the player of the mechanics of the game")
        self.informationlabel2 = tkinter.Label (self.frame, text = "And explain some of the story")
        self.informationlabel3 = tkinter.Label (self.frame, text = "Here the control will be explained too")
        self.frame.pack ()
        self.informationlabel.pack (pady = 25)
        self.informationlabel2.pack(pady = 25)
        self.informationlabel3.pack (pady = 25)


class GAMESETTINGS:
    # This class is for the startup menu settings screen.

    def __init__ (self):
        self.wnd = tkinter.Tk ()
        self.wnd.geometry ("400x400")
        self.frame = tkinter.Frame (self.wnd)
        self.autoReaderState = tkinter.IntVar ()
        self.lightingLabel = tkinter.Label (self.frame, text = "Lighting Preference:")
        self.lightingSlider = tkinter.Scale (self.frame, from_ = 0, to = 200, orient = tkinter.HORIZONTAL)
        self.lightingSlider.bind ("<ButtonRelease-1>", self.lightingSliderChange)
        self.autoReaderCheckBox = tkinter.Checkbutton (self.frame, text = "Auto Reader", variable = self.autoReaderState)
        self.autoReaderLabel = tkinter.Label (self.frame, text = "Auto Reader Speed:")
        self.autoReaderSlider = tkinter.Scale (self.frame, from_ = 0, to = 200, orient = tkinter.HORIZONTAL)
        self.autoReaderSlider.bind ("<ButtonRelease-1>", self.autoReaderChange)
        self.applyButton = tkinter.Button (self.frame, text = "Apply", command = self.buttonApply)
        self.lightingChoice = self.lightingSliderChange
        self.autoReaderChoice = self.autoReaderChange
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
    firstChoiceList = []
    secondChoiceList = []
    thirdChoiceList = []
    dialoglist = []
    orderOfChoices = []
    characterNameList = ["Swapnendu Sanyal", "Omar Sinan         ", "Saquib Razak       "]

    def __init__ (self):
        self.wnd = tkinter.Tk ()
        # self.mainFrame = tkinter.Frame (self.wnd, background = "black")
        self.wnd.geometry ("500x600")
        self.buttonTextMaker ()
        self.firstFrame = tkinter.Frame (self.wnd, background = "brown")
        self.secondFrame = tkinter.Frame (self.wnd, background = "black")
        self.canvas = tkinter.Canvas (self.wnd, background = "yellow")
        self.firstChoiceButton = tkinter.Button (self.firstFrame, text = "First Choice", background = "grey", command = self.firstChoice)
        self.secondChoiceButton = tkinter.Button (self.firstFrame, text = "Second Choice", background = "grey", command = self.secondChoice)
        self.thirdChoiceButton = tkinter.Button (self.firstFrame, text = "Third Choice", background = "grey", command = self.thirdChoice)
        self.dialogLabel = tkinter.Label (self.secondFrame, text = "This is test dialog 1 out of 3", background = "brown")
        self.characterNameFrame = tkinter.Frame (self.dialogLabel, background = "brown")
        self.characterNameLabel = tkinter.Label (self.characterNameFrame, text = "Swapnendu Sanyal", background = "brown")
        # self.mainFrame.pack (fill = tkinter.BOTH, expand = 1)
        self.canvas.pack (fill = tkinter.BOTH, expand = 1)
        self.firstFrame.pack (fill = tkinter.BOTH)
        self.secondFrame.pack ()
        self.firstChoiceButton.pack (side = tkinter.LEFT, ipadx = 45, ipady = 10)
        self.secondChoiceButton.pack (side = tkinter.LEFT, ipadx = 45, ipady = 10)
        self.thirdChoiceButton.pack (side = tkinter.LEFT, ipadx = 45, ipady = 10)
        self.dialogLabel.pack (ipady = 30, ipadx = 200, side = tkinter.LEFT)
        self.characterNameFrame.pack (fill = tkinter.BOTH)
        self.characterNameLabel.pack (side = tkinter.LEFT, ipady = 10)

    def firstChoice (self):
        # This function is for registering the left most button clicks.
        self.score += 1
        self.orderOfChoices.append (1)
        self.firstFrame.pack_forget ()
        self.lenOfOrder = len (self.orderOfChoices)
        if self.lenOfOrder == 3:
            self.choicesResult ()
        self.firstChoiceButton.configure (text = self.firstChoiceList[self.lenOfOrder])
        self.secondChoiceButton.configure(text = self.secondChoiceList[self.lenOfOrder])
        self.thirdChoiceButton.configure (text = self.thirdChoiceList[self.lenOfOrder])
        self.dialogMaker ()

    def secondChoice (self):
        # This function is for registering the middle button click.
        self.score += 2
        self.orderOfChoices.append (2)
        self.firstFrame.pack_forget ()
        self.lenOfOrder = len (self.orderOfChoices)
        if self.lenOfOrder == 3:
            self.choicesResult ()
        self.firstChoiceButton.configure (text = self.firstChoiceList[self.lenOfOrder])
        self.secondChoiceButton.configure(text = self.secondChoiceList[self.lenOfOrder])
        self.thirdChoiceButton.configure (text = self.thirdChoiceList[self.lenOfOrder])
        self.dialogMaker ()

    def thirdChoice (self):
        # This function is for registering the right most button clicks.
        self.score += 3
        self.orderOfChoices.append (3)
        self.firstFrame.pack_forget ()
        self.lenOfOrder = len (self.orderOfChoices)
        if self.lenOfOrder == 3:
            self.choicesResult ()
        self.firstChoiceButton.configure (text = self.firstChoiceList[self.lenOfOrder])
        self.secondChoiceButton.configure(text = self.secondChoiceList[self.lenOfOrder])
        self.thirdChoiceButton.configure (text = self.thirdChoiceList[self.lenOfOrder])
        self.dialogMaker ()

    def buttonTextMaker (self):
        for y in range (1, 4):
            temp = "Say Number " + str (y) + "?"
            self.firstChoiceList.append (temp)
            temp = "Say Number " + str (y * 7) + "?"
            self.secondChoiceList.append (temp)
            temp = "Say Number " + str (y * 11) + "?"
            self.thirdChoiceList.append (temp)
            temp = "This is test dialog " + str (y) + " out of 3"
            self.dialoglist.append (temp)

    # def buttonTextChanger (self):
    #     self.firstChoiceButton.lift (self.firstFrame)
    #     self.secondChoiceButton.lift (self.firstFrame)
    #     self.thirdChoiceButton.lift (self.firstFrame)
    #     self.lenOfOrder = len (orderOfChoices)
    #     self.firstChoiceButton.configure (text = firstChoiceList[lenOfOrder])
    #     self.secondChoiceButton.configure(text = secondChoiceList[lenOfOrder])
    #     self.thirdChoiceButton.configure (text = thirdChoiceList[lenOfOrder])
    #     return

        #
        # if self.isPressed (self.firstChoiceButton):
        #     for i in self.firstChoiceList:
        #         self.firstChoiceButton.configure (text = i)
        #
        # if self.isPressed (self.secondChoiceButton):
        #     for k in self.secondChoiceList:
        #         self.secondChoiceButton.configure (text = k)
        #
        # if self.isPressed (self.thirdChoiceButton):
        #     for j in self.thirdChoiceList:
        #         self.thirdChoiceButton.configure (text = j)

    def dialoghChoiceOrganizer (self):
        return

    def dialogMaker (self):
        self.secondFrame.pack_forget ()
        self.firstFrame.pack ()
        self.secondFrame.pack ()
        self.lenOfOrder = len (self.orderOfChoices)
        self.dialogLabel.configure (text = self.dialoglist[self.lenOfOrder])
        self.characterNameLabel.configure (text = self.characterNameList[self.lenOfOrder])
        return

    def choicesResult (self):
        endingList = []
        for g in range (1, 8):
            temp = "You have reached ending number " + str (g) + "!"
            endingList.append (temp)

        if len (self.orderOfChoices) == 3:
            if self.score == 3:
                self.dialogLabel.configure (text = endingList[0])
            elif self.score == 4:
                self.dialogLabel.configure (text = endingList[2])
            elif self.score == 5:
                self.dialogLabel.configure (text = endingList[3])
            elif self.score == 6:
                self.dialogLabel.configure (text = endingList[4])
            elif self.score == 7:
                self.dialogLabel.configure (text = endingList[5])
            elif self.score == 8:
                self.dialogLabel.configure (text = endingList[6])
            elif self.score == 9:
                self.dialogLabel.configure (text = endingList[7])
            # elif score == 14:
            #     self.dialogLabel.configure (text = endingList[8])
            # elif score == 15:
            #     self.dialogLabel.configure (text = endingList[9])
            # elif score == 16:
            #     self.dialogLabel.configure (text = endingList[10])
            # elif score == 17:
            #     self.dialogLabel.configure (text = endingList[11])
            # elif score == 18:
            #     self.dialogLabel.configure (text = endingList[12])
            # elif score == 19:
            #     self.dialogLabel.configure (text = endingList[13])
            # elif score == 20:
            #     self.dialogLabel.configure (text = endingList[14])
            # elif score == 21:
            #     self.dialogLabel.configure (text = endingList[15])
        else:
            return False
app = STARTUPMENU ()
