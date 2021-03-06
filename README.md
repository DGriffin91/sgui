# sgui
A simple GUI library for Python

Currently, sgui is just simple a wrapper around [Tkinter](https://wiki.python.org/moin/TkInter). (Python's de-facto standard GUI) In the future, backends for other languages like [pyside2](http://wiki.qt.io/Qt_for_Python) may be added.

sgui aims to be a simple and consistent tool for creating basic graphical user interfaces in Python.

sgui is currently under development. Basic usage of the library should not change much. But as it is still in early development, newer versions may break scripts written for older versions.

[sgui on github](https://github.com/DGriffin91/sgui)

To install sgui simply use pip:  
`$ pip install sgui`

### rot13 Code Example

```python
import sgui, codecs

#Update the rotatedTextBox when the normal text changes
def encode(textBox):
	rotatedTextBox.string = codecs.encode(textBox.string, 'rot_13')

#Start window
window = sgui.Tk() 

#Vertical Layout frame
mainBox = sgui.VBox(window)

sgui.Label(mainBox, string = "Normal Text:") 
normalTextBox = sgui.Textbox(mainBox, string = "Some normal text", command = encode)

sgui.Label(mainBox, string = "Rotated Text:") 
rotatedTextBox = sgui.Textbox(mainBox)

window.startGUI()
```

### Currently Supported Widgets
* Textbox
* Textentry
* Button
* Label
* Checkbox
* Listbox
* Radiobuttons
* Canvas
* VBox
* HBox

##### Most widgets support:
* `.string` for text manipulation (String)
* `.command` for call back function (Function)
* `.enabled` can be True or False for enabling/disabling control (Boolean)
* `.tooltip` for hover over tool tips (String)

##### For example:
```python
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
```

##### `.string` and `.command` can be declared when the widget is created:
```python
testButton = sgui.Button(window, string = "I'm a button!", command = foo) 
```
