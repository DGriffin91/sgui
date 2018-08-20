# sgui
A simple GUI library for Python

Currently, sgui is just simple a wrapper around [Tkinter](https://wiki.python.org/moin/TkInter). (Python's de-facto standard GUI) In the future, backends for other languages like [pyside2](http://wiki.qt.io/Qt_for_Python) may be added.

sgui aims to be a simple and consistent tool for creating basic graphical user interfaces in python.

sgui is currently under development. Basic usage of the library should not change much. But as it is still in early development, newer versions may break scripts written for older versions.

[sgui on github](https://github.com/DGriffin91/sgui)

#### rot13 Code Example

```python
import sgui, codecs

#Call back function for when the  normal text changes
def encode(textBox):
	rotatedTextBox.string = codecs.encode(textBox.string, 'rot_13')

#Start Tk window
window = sgui.Tk() 

#Vertical Layout frame
mainBox = sgui.VBox(window)

sgui.Label(mainBox, string = "Normal Text:") 
normalTextBox = sgui.TextBox(mainBox, string = "Some normal text", command = encode)

sgui.Label(mainBox, string = "Rotated Text:") 
rotatedTextBox = sgui.TextBox(mainBox)

window.startGUI()
```
