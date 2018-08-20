import sgui, codecs

#Update the rotatedTextBox when the normal text changes
def encode(textBox):
	rotatedTextBox.string = codecs.encode(textBox.string, 'rot_13')

#Start window
window = sgui.Tk() 

#Vertical Layout frame
mainBox = sgui.VBox(window)

sgui.Label(mainBox, string = "Normal Text:") 
normalTextBox = sgui.TextBox(mainBox, string = "Some normal text", command = encode)

sgui.Label(mainBox, string = "Rotated Text:") 
rotatedTextBox = sgui.TextBox(mainBox)

window.startGUI()