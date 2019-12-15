# -*- coding: utf-8 -*-

"""Fidget, inspired by fidget spinners.

Exercises

1. Change the spinner pattern.
2. Respond to mouse clicks.
3. Change its acceleration.
4. Make it go forwards and backwards.

"""
import turtle
from audio_input import AudioInput
from pynput.keyboard import Key, Controller
import numpy as np

keyboard = Controller()
def press_space():
    keyboard.press(Key.space)
    keyboard.release(Key.space)

def press_a():
    keyboard.press('a')
    keyboard.release('a')

audio_input = AudioInput(onset_thres=0.03, verbose=True)
audio_input.add_onset_action(press_space, accept_band=[90, 200])
audio_input.add_onset_action(press_a, accept_band=[200, 1000])
audio_input.launch()

state = {'turn': 0}

def spinner():
    "Draw fidget spinner."
    turtle.clear()
    turtle.angle = state['turn'] / 10
    turtle.right(turtle.angle)
    turtle.forward(100)
    turtle.dot(120, 'red')
    turtle.back(100)
    turtle.right(120)
    turtle.forward(100)
    turtle.dot(120, 'green')
    turtle.back(100)
    turtle.right(120)
    turtle.forward(100)
    turtle.dot(120, 'blue')
    turtle.back(100)
    turtle.right(120)
    turtle.update()

def animate():
    "Animate fidget spinner."
    damp = np.abs(round(state['turn']*0.008))+1
    if state['turn'] > damp:
        state['turn'] -= damp
    elif state['turn'] < -damp:
        state['turn'] += damp
    else:
        state['turan'] = 0
    spinner()
    turtle.ontimer(animate, 20)

def flick():
    "Flick fidget spinner."
    state['turn'] += 50

def drag():
    "Drag fidget spinner."
    state['turn'] -= 50

turtle.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle.tracer(False)
turtle.width(20)
turtle.onkey(flick, 'space')
turtle.onkey(drag, 'a')
turtle.listen()
animate()
turtle.done()
audio_input.terminate()

 
