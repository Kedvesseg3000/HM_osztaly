input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    for (let index = 0; index < 1; index++) {
        szam = randint(1, 6)
        basic.showNumber(szam)
    }
    basic.showIcon(IconNames.Heart)
})
let szam = 0
basic.showIcon(IconNames.Heart)
basic.forever(function on_forever() {
    
})
