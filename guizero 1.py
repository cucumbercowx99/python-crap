from guizero import App, Text, PushButton, TextBox

def display_height():
    textbox1cont.value = window1cont4.value

window1 = App(title='Height Calculator')
window1cont1 = Text(window1, text='')
window1cont2 = Text(window1, text='Enter your height in the box below (including measurement units):' )
textbox1cont = TextBox(window1)
window1cont3 = PushButton(window1, command=display_height, text='Go')
window1cont4 = Text(window1, text='')
window1.display()