import sgui
window = sgui.Tk() 

def foo(btn):
	print(btn.string, "foo!")

testButton = sgui.Button(window) 
testButton.string = "I'm a button!"
testButton.command = foo
testButton.enabled = False
testButton.tooltip = "This button is disabled, it will never foo!"

window.startGUI()