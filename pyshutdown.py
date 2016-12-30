#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter as Tk
import ttk
import logging
import os


logger = logging.getLogger('pyshutdown')
hdlr = logging.FileHandler('/var/tmp/pyshutdown.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)

logger.info('Starting...')


BSIZE = 150
#PAPP = "/home/m/Documentos/desarrollo/gui/"
APP_PATH = os.path.dirname(os.path.abspath(__file__)) + "/"
RESOURCE_PATH = APP_PATH
BNAME_SHUTDOWN = "shutdown_128.png"
BNAME_RESTART = "restart_128.png"
BNAME_CONTINUE = "continue_128.png"

BTEXT_SHUTDOWN = "Apagar"
BTEXT_RESTART = "Reiniciar"
BTEXT_CONTINUE = "Continuar"

PB_TIMER = 15


class pyshutdown():
    def __init__(self):
        try:
            self.initcontrols()
            self.top.mainloop()
        except Exception, e:
            logger.error('Exception', exc_info=True)

    def initcontrols(self):
        t_width = BSIZE * 3 + 50
        t_height_bframe = BSIZE
        t_height = t_height_bframe + 50

        self.top = Tk.Tk()
        self.top.overrideredirect(True)
        posx = self.top.winfo_screenwidth() / 2 - t_width / 2
        posy = self.top.winfo_screenheight() / 2 - t_height / 2
        self.top.geometry('{}x{}+{}+{}'.format(t_width, t_height, posx, posy))

        self.bframe = Tk.Frame(self.top,
                               width=t_width,
                               height=t_height_bframe)
        self.bframe.pack()

        self.Bs = Tk.Button(self.bframe, text=BTEXT_SHUTDOWN,
                       command=self.shutdownCallBack, cursor="hand2",
                       height=BSIZE, width=BSIZE, compound="top")
        self.ps = Tk.PhotoImage(file=APP_PATH + BNAME_SHUTDOWN)
        self.Bs.config(image=self.ps)
        self.Bs.pack(side=Tk.LEFT)

        self.Br = Tk.Button(self.bframe, text=BTEXT_RESTART,
                       command=self.restartCallBack, cursor="hand2",
                       height=BSIZE, width=BSIZE, compound="top")
        self.pr = Tk.PhotoImage(file=APP_PATH + BNAME_RESTART)
        self.Br.config(image=self.pr)
        self.Br.pack(side=Tk.LEFT)

        self.Bc = Tk.Button(self.bframe, text=BTEXT_CONTINUE,
                       command=self.cancelCallBack, cursor="hand2",
                       height=BSIZE, width=BSIZE, compound="top")
        self.pc = Tk.PhotoImage(file=APP_PATH + BNAME_CONTINUE)
        self.Bc.config(image=self.pc)
        self.Bc.pack(side=Tk.LEFT)

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

        logger.info('All stuff prepared...')
    def cancelCallBack(self):
        exit()

    def shutdownCallBack(self):
        os.system("sudo /sbin/shutdown -h now")

    def restartCallBack(self):
        os.system("sudo /sbin/shutdown -r now")

    def timer(self):
        if self.progress["value"]:
            self.progress["value"] -=1
            self.progress_text.set("Apagado en {}".format(self.progress["value"]))
            self.top.after(1000, self.timer)
        else:
            self.progress_text.set("Apagando...")

app=pyshutdown()


