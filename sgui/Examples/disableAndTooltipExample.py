import sgui

#Start TK window
window = sgui.Tk() 

#Layout frame
mainBox = sgui.HBox(window)

# --- Callback functions ---

def buttonPress(btn):
    print(btn.string + " pressed!")
    print(testCheckbox.checked)
    testCheckbox.checked = not testCheckbox.checked

def checkBoxed(chb):
    print(chb.string + " " + str(chb.checked))

def printList(listb):
    print(listb.items)
    print(listb.selection)
    print(listb.items[listb.selection])

def printText(textb):
    print(textb.string)

# --- Labels ---

testLabel = sgui.Label(mainBox, string = "Stuff!") 

testLabel2 = sgui.Label(mainBox) 
testLabel2.string = "Stuff2!"

# --- Buttons ---

#myStyle = ttk.Style()


buttonBox = sgui.VBox(mainBox)
buttonBox.tooltip = "!!!"

testLabel = sgui.Label(buttonBox, string = "Some buttons:") 

testButton = sgui.Button(buttonBox, string = "Generic Fungus", command = buttonPress) 


testButton2 = sgui.Button(buttonBox) 
testButton2.string = "Jungle Rot"
testButton2.command = buttonPress
testButton2.tooltip = "A Jungle Rot tool tip"

testButton2['state'] = 'disabled'

testButton3 = sgui.Button(buttonBox) 
testButton3.string = "Episodic Appendage Spawning"
testButton3.command = buttonPress
testButton3.tooltip = "A tool tip"

# --- Checkboxes ---


checkBoxBox = sgui.VBox(mainBox)

testCheckbox = sgui.Checkbox(checkBoxBox, string = "Check me!", command = checkBoxed) 

testCheckbox2 = sgui.Checkbox(checkBoxBox) 
testCheckbox2.string = "No, check me!!"
testCheckbox2.command = checkBoxed

testCheckbox2.enabled = False
testCheckbox2.tooltip = "A No, check me!! tool tip"

# --- Listboxes ---

listbox1 = sgui.Listbox(mainBox, items = ["AAA","BBB","CCC","DDD"], command = printList)

listbox2 = sgui.Listbox(mainBox) 
listbox2.items = ["FFF","GGG","HHH","III"]
listbox2.command = printList

listbox2.enabled = False
listbox2.tooltip = "A List tool tip"

# --- Textboxes ---

textBox1 = sgui.Textbox(mainBox, command = printText)

textBox2 = sgui.Textbox(mainBox)
textBox2.command = printText
textBox2.enabled = False
textBox2.tooltip = "textBox2 tool tip"

# --- Radiobuttons ---


radio1 = sgui.VBox(mainBox)

radiobuttons = sgui.Radiobuttons(radio1, items = ["JJJ","LLL","MMM","NNN"], command = printList) 

radio2 = sgui.VBox(mainBox)
radiobuttons = sgui.Radiobuttons(radio2) 
radiobuttons.items = ["OOO","PPP","QQQ","RRR"]
radiobuttons.command = printList
radiobuttons.buttons[1].enabled = False
radiobuttons.tooltip = "radiobuttons tool tip"
radiobuttons.buttons[1].tooltip = "radiobutton 1 tool tip"

# --- TextEntry ---

textEntryBox = sgui.VBox(mainBox)

textEntry = sgui.Textentry(textEntryBox)
textEntry.command = printText
textEntry.tooltip = "textEntry tool tip"

textEntry = sgui.Textentry(textEntryBox, string = "TEST!!", command = printText)
textEntry.enabled = False

#Start GUI
window.startGUI()