#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as Tk
from tkinter import ttk
import logging
import os
import gettext
import sys
import getopt


current_lang = os.getenv('LANG')
lang = gettext.translation('pyshutdown', localedir='locale', languages=[current_lang], fallback=True)
lang.install()

BSIZE = 150
APP_PATH = os.path.dirname(os.path.abspath(__file__)) + "/"
RESOURCE_PATH = APP_PATH
BNAME_SHUTDOWN = RESOURCE_PATH + "shutdown_128.png"
BNAME_RESTART = RESOURCE_PATH + "restart_128.png"
BNAME_CONTINUE = RESOURCE_PATH + "continue_128.png"

BTEXT_SHUTDOWN = _('Shutdown')
BTEXT_RESTART = _("Restart")
BTEXT_CONTINUE = _("Continue")

PB_TIMER = 60


class pyshutdown():
    def __init__(self, setlogging, current_lang):
        try:
            self.setlogging = setlogging
            if self.setlogging:
                self.logger = logging.getLogger('pyshutdown')
                hdlr = logging.FileHandler('/var/tmp/pyshutdown_{}.log'.format(os.getlogin()))
                formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
                hdlr.setFormatter(formatter)
                self.logger.addHandler(hdlr)
                self.logger.setLevel(logging.INFO)
                self.logger.info('Starting...')

            self.writelog('Current language {}'.format(current_lang))

            self.initcontrols()
            self.top.mainloop()
        except Exception as e:
            print (str(e))


    def initcontrols(self):
        self.buttons =[]
        self.photos = []
        t_width = BSIZE * 3 + 50
        t_height_bframe = BSIZE
        t_height = t_height_bframe + 50

        self.top = Tk.Tk()
        self.top.overrideredirect(True)
        posx = (self.top.winfo_screenwidth() - t_width) // 2
        posy = (self.top.winfo_screenheight() - t_height) // 2
        self.top.geometry('{}x{}+{}+{}'.format(t_width, t_height, posx, posy))

        self.bframe = Tk.Frame(self.top,
                               width=t_width,
                               height=t_height_bframe)
        self.bframe.pack()

        self.createbutton(BTEXT_SHUTDOWN, BNAME_SHUTDOWN, self.shutdownCallBack)
        self.createbutton(BTEXT_RESTART, BNAME_RESTART, self.restartCallBack)
        self.createbutton(BTEXT_CONTINUE, BNAME_CONTINUE, self.cancelCallBack)

        self.progress = ttk.Progressbar(self.top, orient="horizontal",
                                    length=t_width, mode="determinate")
        self.progress.pack(side=Tk.BOTTOM)
        self.progress["value"] =  PB_TIMER
        self.progress["maximum"] = PB_TIMER
        if PB_TIMER:
            self.top.after(1000, self.timer)

        self.progress_text = Tk.StringVar()
        self.progress_label = Tk.Label(self.top,
                                   textvariable = self.progress_text)
        self.progress_label.pack(side=Tk.BOTTOM)

        self.top.resizable(width=False, height=False)
        self.top.update_idletasks()

        self.writelog('All stuff prepared...')

    def cancelCallBack(self):
        self.writelog('Cancel')
        exit()

    def shutdownCallBack(self):
        self.writelog('Shutdown pressed')
        os.system("sudo /sbin/shutdown -h now")

    def restartCallBack(self):
        self.writelog('Restart pressed')
        os.system("sudo /sbin/shutdown -r now")

    def timer(self):
        if self.progress["value"]:
            self.progress["value"] -=1
            self.progress_text.set(_("Shutdown in {}").format(self.progress["value"]))
            self.top.after(1000, self.timer)
        else:
            self.progress_text.set(_("Shutting down..."))
            self.writelog('Shutdown by timer')
            self.shutdownCallBack()

    def createbutton(self, text_button, path_image, command_callback):
        """ Create a button with a description (text_button),
            an image (path_image) and a command (command_callback)

            Button and photoimage are stored in global list.
        """
        button = Tk.Button(self.bframe, text=text_button,
                       command=command_callback, cursor="hand2",
                       height=BSIZE, width=BSIZE, compound="top")
        self.buttons.append(button)
        photo = Tk.PhotoImage(file=path_image)
        self.photos.append(photo)
        button.config(image=photo)
        button.pack(side=Tk.LEFT)

    def writelog(self, msg):
        if self.setlogging:
            self.logger.info(msg)

def main(argv):
    try:
        opts, args = getopt.getopt(argv,"hl",['logging'])
    except getopt.GetoptError:
      print ('pyshutdown.py [-h] [-l]')
      sys.exit(2)

    logging = False
    for opt, arg in opts:
        if opt == '-h':
            print ('pyshutdown.py [-h] [-l]')
            sys.exit()
        elif opt in ("-l", "--logging"):
            logging = True

    app = pyshutdown(logging, current_lang)


if __name__ == "__main__":
   main(sys.argv[1:])
