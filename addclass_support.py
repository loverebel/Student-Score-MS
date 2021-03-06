#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Jan 02, 2020 11:38:36 PM CST  platform: Windows NT

import sys
import pymysql
try:
    import Tkinter as tk
    import Tkinter.messagebox as v
except ImportError:
    import tkinter as tk
    import tkinter.messagebox as v

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def addgrade():
    cno = w.Entry1_6.get()
    cname = w.Entry1.get()
    credit = w.Entry1_1.get()
    if cno == "" or cname == "":
        v.showerror("错误","课程和课程名不能为空")
    else:
        conn = pymysql.connect(host='localhost', user='root', passwd='809144', db='mydb', port=3306)
        cur = conn.cursor()
        cur.execute("SELECT * FROM class WHERE cno = %s",cno)
        r = cur.fetchone()
        if r == None:
            values = [cno,cname,credit]
            cur.execute('INSERT INTO class VALUES(%s,%s,%s)',values)
            conn.commit()
            v.showinfo(cno, "添加成功")
        else:
            v.showerror("错误", "该课程信息已经存在，请检查后添加")
    cur.close()
    conn.close()
    sys.stdout.flush()

def comeback():
    destroy_window()
    sys.stdout.flush()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import addclass
    addclass.vp_start_gui()




