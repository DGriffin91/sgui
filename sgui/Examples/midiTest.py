import sgui
import mido

port = mido.open_output()

#Start TK window
window = sgui.Tk() 

#Layout frame
mainBox = sgui.HBox(window)


def playMidiNotes(btn):
    notes = noteSequenceEntry.string.split()
    for note in notes:
        print(int(note))
        msg = mido.Message('note_on', note=int(note))
        port.send(msg)

buttonBox = sgui.HBox(mainBox)

noteSequenceEntry = sgui.Textentry(buttonBox, string = "60 64") 

playButton = sgui.Button(buttonBox, string = "Play", command = playMidiNotes) 


#Start GUI
window.startGUI()