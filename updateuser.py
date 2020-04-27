#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Jan 01, 2020 01:45:18 PM CST  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import updateuser_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    updateuser_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    updateuser_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font9 = "-family {Microsoft YaHei UI} -size 11 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"

        top.geometry("600x450+676+276")
        top.minsize(152, 1)
        top.maxsize(1924, 1055)
        top.resizable(1, 1)
        top.title("修改用户信息界面")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.233, rely=0.711, height=53, width=113)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(command=updateuser_support.update)
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font9)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''更新''')
        self.Button1.configure(cursor = "hand2")

        self.Button1_1 = tk.Button(top)
        self.Button1_1.place(relx=0.55, rely=0.711, height=53, width=103)
        self.Button1_1.configure(activebackground="#ececec")
        self.Button1_1.configure(activeforeground="#000000")
        self.Button1_1.configure(background="#d9d9d9")
        self.Button1_1.configure(command=updateuser_support.comeback)
        self.Button1_1.configure(disabledforeground="#a3a3a3")
        self.Button1_1.configure(font=font9)
        self.Button1_1.configure(foreground="#000000")
        self.Button1_1.configure(highlightbackground="#d9d9d9")
        self.Button1_1.configure(highlightcolor="black")
        self.Button1_1.configure(pady="0")
        self.Button1_1.configure(text='''返回''')
        self.Button1_1.configure(cursor="hand2")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.183, rely=0.111, height=46, width=125)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="#000000")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''用户名''')

        self.Entryusername = tk.Entry(top)
        self.Entryusername.place(relx=0.45, rely=0.111, height=51
                , relwidth=0.307)
        self.Entryusername.configure(background="white")
        self.Entryusername.configure(disabledforeground="#a3a3a3")
        self.Entryusername.configure(font="TkFixedFont")
        self.Entryusername.configure(foreground="#000000")
        self.Entryusername.configure(highlightbackground="#d9d9d9")
        self.Entryusername.configure(highlightcolor="black")
        self.Entryusername.configure(insertbackground="black")
        self.Entryusername.configure(selectbackground="#c4c4c4")
        self.Entryusername.configure(selectforeground="black")

        self.Label1_2 = tk.Label(top)
        self.Label1_2.place(relx=0.183, rely=0.244, height=46, width=125)
        self.Label1_2.configure(activebackground="#f9f9f9")
        self.Label1_2.configure(activeforeground="black")
        self.Label1_2.configure(background="#d9d9d9")
        self.Label1_2.configure(disabledforeground="#a3a3a3")
        self.Label1_2.configure(font=font9)
        self.Label1_2.configure(foreground="#000000")
        self.Label1_2.configure(highlightbackground="#d9d9d9")
        self.Label1_2.configure(highlightcolor="black")
        self.Label1_2.configure(text='''旧密码''')

        self.Entrypwd = tk.Entry(top)
        self.Entrypwd.place(relx=0.45, rely=0.244,height=51, relwidth=0.307)
        self.Entrypwd.configure(background="white")
        self.Entrypwd.configure(disabledforeground="#a3a3a3")
        self.Entrypwd.configure(font="TkFixedFont")
        self.Entrypwd.configure(foreground="#000000")
        self.Entrypwd.configure(highlightbackground="#d9d9d9")
        self.Entrypwd.configure(highlightcolor="black")
        self.Entrypwd.configure(insertbackground="black")
        self.Entrypwd.configure(selectbackground="#c4c4c4")
        self.Entrypwd.configure(selectforeground="black")

        self.Label1_3 = tk.Label(top)
        self.Label1_3.place(relx=0.183, rely=0.378, height=46, width=125)
        self.Label1_3.configure(activebackground="#f9f9f9")
        self.Label1_3.configure(activeforeground="black")
        self.Label1_3.configure(background="#d9d9d9")
        self.Label1_3.configure(disabledforeground="#a3a3a3")
        self.Label1_3.configure(font=font9)
        self.Label1_3.configure(foreground="#000000")
        self.Label1_3.configure(highlightbackground="#d9d9d9")
        self.Label1_3.configure(highlightcolor="black")
        self.Label1_3.configure(text='''新密码''')

        self.Entrypwd1 = tk.Entry(top)
        self.Entrypwd1.place(relx=0.45, rely=0.378,height=51, relwidth=0.307)
        self.Entrypwd1.configure(background="white")
        self.Entrypwd1.configure(disabledforeground="#a3a3a3")
        self.Entrypwd1.configure(font="TkFixedFont")
        self.Entrypwd1.configure(foreground="#000000")
        self.Entrypwd1.configure(highlightbackground="#d9d9d9")
        self.Entrypwd1.configure(highlightcolor="black")
        self.Entrypwd1.configure(insertbackground="black")
        self.Entrypwd1.configure(selectbackground="#c4c4c4")
        self.Entrypwd1.configure(selectforeground="black")

        self.Entryqx = tk.Entry(top)
        self.Entryqx.place(relx=0.45, rely=0.511,height=51, relwidth=0.307)
        self.Entryqx.configure(background="white")
        self.Entryqx.configure(disabledforeground="#a3a3a3")
        self.Entryqx.configure(font="TkFixedFont")
        self.Entryqx.configure(foreground="#000000")
        self.Entryqx.configure(highlightbackground="#d9d9d9")
        self.Entryqx.configure(highlightcolor="black")
        self.Entryqx.configure(insertbackground="black")
        self.Entryqx.configure(selectbackground="#c4c4c4")
        self.Entryqx.configure(selectforeground="black")

        self.Label1_4 = tk.Label(top)
        self.Label1_4.place(relx=0.183, rely=0.511, height=46, width=125)
        self.Label1_4.configure(activebackground="#f9f9f9")
        self.Label1_4.configure(activeforeground="black")
        self.Label1_4.configure(background="#d9d9d9")
        self.Label1_4.configure(disabledforeground="#a3a3a3")
        self.Label1_4.configure(font="-family {Microsoft YaHei UI} -size 11 -weight bold")
        self.Label1_4.configure(foreground="#000000")
        self.Label1_4.configure(highlightbackground="#d9d9d9")
        self.Label1_4.configure(highlightcolor="black")
        self.Label1_4.configure(text='''权限''')

if __name__ == '__main__':
    vp_start_gui()




