#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Jan 03, 2020 11:53:46 AM CST  platform: Windows NT

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

import updategrade_support

def vp_start_gui(sno,cno,grade):
    '''Starting point when module is the main routine.'''
    global sno1,cno1,grade1
    sno1 = sno
    cno1 = cno
    grade1 = grade
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    updategrade_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    updategrade_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        global sno1, cno1, grade1
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("947x348+533+289")
        top.minsize(152, 1)
        top.maxsize(1924, 1055)
        top.resizable(1, 1)
        top.title("修改课程信息界面")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.348, rely=0.69, height=53, width=113)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(command=updategrade_support.updates)
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Microsoft YaHei UI} -size 11 -weight bold")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''修改信息''')

        self.Button1_1 = tk.Button(top)
        self.Button1_1.place(relx=0.57, rely=0.69, height=53, width=103)
        self.Button1_1.configure(activebackground="#ececec")
        self.Button1_1.configure(activeforeground="#000000")
        self.Button1_1.configure(background="#d9d9d9")
        self.Button1_1.configure(command=updategrade_support.comeback)
        self.Button1_1.configure(disabledforeground="#a3a3a3")
        self.Button1_1.configure(font="-family {Microsoft YaHei UI} -size 11 -weight bold")
        self.Button1_1.configure(foreground="#000000")
        self.Button1_1.configure(highlightbackground="#d9d9d9")
        self.Button1_1.configure(highlightcolor="black")
        self.Button1_1.configure(pady="0")
        self.Button1_1.configure(text='''返回''')

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.327, rely=0.086, height=46, width=125)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="#000000")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Microsoft YaHei UI} -size 11 -weight bold")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''学号''')

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.486, rely=0.086,height=51, relwidth=0.194)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")
        self.Entry1.insert(0,sno1)
        self.Entry1.configure(state="readonly")

        self.Label1_2 = tk.Label(top)
        self.Label1_2.place(relx=0.327, rely=0.287, height=46, width=125)
        self.Label1_2.configure(activebackground="#f9f9f9")
        self.Label1_2.configure(activeforeground="black")
        self.Label1_2.configure(background="#d9d9d9")
        self.Label1_2.configure(disabledforeground="#a3a3a3")
        self.Label1_2.configure(font="-family {Microsoft YaHei UI} -size 11 -weight bold")
        self.Label1_2.configure(foreground="#000000")
        self.Label1_2.configure(highlightbackground="#d9d9d9")
        self.Label1_2.configure(highlightcolor="black")
        self.Label1_2.configure(text='''课程号''')

        self.Entry2 = tk.Entry(top)
        self.Entry2.place(relx=0.486, rely=0.287,height=51, relwidth=0.194)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(selectbackground="#c4c4c4")
        self.Entry2.configure(selectforeground="black")
        self.Entry2.insert(0,cno1)
        self.Entry2.configure(state="readonly")

        self.Entry4 = tk.Entry(top)
        self.Entry4.place(relx=0.486, rely=0.489,height=51, relwidth=0.194)
        self.Entry4.configure(background="white")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font="TkFixedFont")
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(highlightbackground="#d9d9d9")
        self.Entry4.configure(highlightcolor="black")
        self.Entry4.configure(insertbackground="black")
        self.Entry4.configure(selectbackground="#c4c4c4")
        self.Entry4.configure(selectforeground="black")
        self.Entry4.insert(0,grade1)

        self.Label1_4 = tk.Label(top)
        self.Label1_4.place(relx=0.845, rely=-0.374, height=46, width=125)
        self.Label1_4.configure(activebackground="#f9f9f9")
        self.Label1_4.configure(activeforeground="black")
        self.Label1_4.configure(background="#d9d9d9")
        self.Label1_4.configure(disabledforeground="#a3a3a3")
        self.Label1_4.configure(font="-family {Microsoft YaHei UI} -size 11 -weight bold")
        self.Label1_4.configure(foreground="#000000")
        self.Label1_4.configure(highlightbackground="#d9d9d9")
        self.Label1_4.configure(highlightcolor="black")
        self.Label1_4.configure(text='''专业''')

        self.Label1_1 = tk.Label(top)
        self.Label1_1.place(relx=-0.106, rely=1.667, height=46, width=125)
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(activeforeground="black")
        self.Label1_1.configure(background="#d9d9d9")
        self.Label1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1.configure(font="-family {Microsoft YaHei UI} -size 11 -weight bold")
        self.Label1_1.configure(foreground="#000000")
        self.Label1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1.configure(highlightcolor="black")
        self.Label1_1.configure(text='''大学物理''')

        self.Label1_3 = tk.Label(top)
        self.Label1_3.place(relx=0.327, rely=0.489, height=46, width=125)
        self.Label1_3.configure(activebackground="#f9f9f9")
        self.Label1_3.configure(activeforeground="black")
        self.Label1_3.configure(background="#d9d9d9")
        self.Label1_3.configure(disabledforeground="#a3a3a3")
        self.Label1_3.configure(font="-family {Microsoft YaHei UI} -size 11 -weight bold")
        self.Label1_3.configure(foreground="#000000")
        self.Label1_3.configure(highlightbackground="#d9d9d9")
        self.Label1_3.configure(highlightcolor="black")
        self.Label1_3.configure(text='''成绩''')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

    @staticmethod
    def popup1(event, *args, **kwargs):
        Popupmenu1 = tk.Menu(root, tearoff=0)
        Popupmenu1.configure(activebackground="#f9f9f9")
        Popupmenu1.configure(activeborderwidth="1")
        Popupmenu1.configure(activeforeground="black")
        Popupmenu1.configure(background="#d9d9d9")
        Popupmenu1.configure(borderwidth="1")
        Popupmenu1.configure(disabledforeground="#a3a3a3")
        Popupmenu1.configure(font="-family {Microsoft YaHei UI} -size 9")
        Popupmenu1.configure(foreground="black")
        Popupmenu1.post(event.x_root, event.y_root)

if __name__ == '__main__':
    vp_start_gui()





