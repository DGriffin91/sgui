import sgui
import mido

port = mido.open_output()

window = sgui.Tk() 

mainBox = sgui.HBox(window)

bpmMS = int(60000 / 60 / 4)

global btnGrid
btnGrid = []

global currentStep
currentStep = 0

stepBox = sgui.HBox(mainBox)
for col in range(24):
    btnGridCol = []
    vBox = sgui.VBox(stepBox)
    for col in range(24):
        btnGridCol.append(sgui.Checkbox(vBox))
    btnGrid.append(btnGridCol)

def step():
    global currentStep
    global btnGrid
    print(currentStep)

    for i, btn in enumerate(btnGrid[currentStep]):
        if btn.checked:
            port.send(mido.Message('note_on', note=i+60-12))

    if currentStep >= 23:
        currentStep = 0
    else:
        currentStep += 1

    window.after(bpmMS, step)

window.after(bpmMS, step)

window.startGUI()