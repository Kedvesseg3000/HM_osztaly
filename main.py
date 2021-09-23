def on_button_pressed_a():
    global szam
    for index in range(1):
        szam = randint(1, 6)
        basic.show_number(szam)
    basic.show_icon(IconNames.HEART)
input.on_button_pressed(Button.A, on_button_pressed_a)

szam = 0
basic.show_icon(IconNames.HEART)

def on_forever():
    pass
basic.forever(on_forever)
