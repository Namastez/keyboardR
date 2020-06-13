# Written by: Namastez, Johan Lundgren
# Python3.6+
# Dependencies (requirements.txt): keyboard, pywinauto, pydub
#
# To use with MAX Keyboard macropad(or any other pad/keyboard)
# I mainly use this for my stream on twitch
# I use the Max Falcon software for media keys and to customize the LEDs of the pad.
# Identify keys like F20 etc, with the print_pressed_keys function. They show up in console when pressed.


import keyboard
import os
import time
from pywinauto import application
import random
from pydub import AudioSegment
from pydub.playback import play


#GLOBAL
wins = '0'
losses = '0'


#Setting the value 0 to each of the .txt files
def start_scoring():
    with open('today_losses.txt', 'w') as fL:
        fL.write(losses)
        print('Initiated losses scoring, setting 0')
    with open('today_wins.txt', 'w') as fW:
        fW.write(wins)
        print('Initiated scoring for wins, setting 0')


#System started sound
system_online = AudioSegment.from_file_using_temporary_files('Z:\stream\gg\online.mp3')


# Open spotify to work with the right window ID.
app_spotify = application.Application()
time.sleep(2)
app_spotify.start(r'C:\Users\Namastez\AppData\Roaming\Spotify\Spotify.exe')


# Shows the currently pressed key(s) in terminal
def print_pressed_keys(e):
    line = ', '.join(str(code) for code in keyboard._pressed_events)
    print('\r' + line + ' '*40, end='')


# SPOTIFY (need to minimize and restore window, was otherwise bugged on my Windows)
def open_spotify():
    app_dialog = app_spotify.top_window()
    app_dialog.minimize()
    time.sleep(0.2)
    app_dialog.restore()
    app_dialog.set_focus()


#Paste
def paster():
    #CTRL = 29, v = 47, Enter: 28
    keyboard.press(29)
    keyboard.press(47)
    keyboard.release(47)
    keyboard.release(29)
    time.sleep(0.2)
    keyboard.press(28)
    keyboard.release(28)


def play_error():
    # Error sound:
    system_error = AudioSegment.from_file_using_temporary_files('Z:\stream\gg\Windows_error.mp3')
    play(system_error)


#Placeholder funtion, discord-hotkey + this hotkey plays a sound in my discord
#by typing the command in the chat
def discord_hotkey():
    keyboard.write('!sound ljuger')
    keyboard.press(28)
    time.sleep(0.1)
    keyboard.release(28)


# Using pydub, plays a random sound from directory
def play_gg_sound():
    sounddir = 'Z:\stream\gg\mp3'
    soundlist = os.listdir(sounddir)
    gg_play = random.choice(soundlist)
    sound2play = sounddir + '\\' + gg_play
    playsound = AudioSegment.from_file_using_temporary_files(sound2play)
    print('GG! played sound: ' + gg_play)
    play(playsound)



def add_win():
    with open('today_wins.txt', 'r+') as fWin:
        current_wins = fWin.read()
        wint = int(current_wins)
        new_score = wint + 1
        fWin.seek(0)
        fWin.write(str(new_score))
        print('Added win, current wins: ' + str(new_score))
        fWin.close()


def add_loss():
    with open('today_losses.txt', 'r+') as fLoss:
        current_wins = fLoss.read()
        wloss = int(current_wins)
        new_score = wloss + 1
        fLoss.seek(0)
        fLoss.write(str(new_score))
        print('Added loss, current losses: ' + str(new_score))
        fLoss.close()


# F13
keyboard.add_hotkey(100, lambda: os.startfile(r'C:\Users\Namastez\AppData\Local\Discord\app-0.0.305\Discord.exe'))
# F14
keyboard.add_hotkey(101, lambda: open_spotify())
# F15
keyboard.add_hotkey(102, lambda: (add_win()))
# F16
keyboard.add_hotkey(103, lambda: (add_loss()))
# F17
keyboard.add_hotkey(104, lambda: play_error())
# F18

# F19
keyboard.add_hotkey(106, lambda: play_gg_sound())
# F20


# ABBREVIATIONS FOR SIMPLE QUICK TYPING
# GMAIL
keyboard.add_abbreviation('@@', 'namastezjohan@gmail.com')
# PROTONMAIL
keyboard.add_abbreviation('@@@', 'namastez@protonmail.com')
#Twitch
keyboard.add_abbreviation('TTV', 'https://twitch.tv/namastez')
# MISCELLANEOUS
keyboard.add_abbreviation('tm', u'™')
keyboard.add_abbreviation('cr', u'©')
keyboard.add_abbreviation('^^2', u'²')

play(system_online) # Plays a sound when program starts
start_scoring() # Makes sure the .txt files for scoring are reset
keyboard.hook(print_pressed_keys) # Shows the value for currently pressed key in console
keyboard.wait() # "While True"

