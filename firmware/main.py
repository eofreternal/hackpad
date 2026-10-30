print("Main.py started")

import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner
from kmk.modules.encoder import EncoderHandler

encoder_handler = EncoderHandler()

pins = [
    board.D2, # First row W
    board.D10, # Second row A
    board.D9, # Second row S
    board.D3, # Second row D
]

keyboard = KMKKeyboard()
keyboard.matrix = KeysScanner(pins)
keyboard.modules = [encoder_handler]

encoder_handler.pins = (
    (board.D8, board.D7, board.D6)
)
encoder_handler.map = [((KC.VOLD, KC.VOLU, KC.MUTE),)]

keyboard.keymap = [[KC.W, KC.A, KC.S, KC.D]]

if __name__ == "__main__":
    keyboard.go()