# -*- coding: utf-8 -*-
import tkinter

root= tkinter.Tk()    #生成主窗口
label = tkinter.Label(root,text = "hello\npython",
                      width = 20,
                      height = 20,
                      justify = tkinter.LEFT)  #生成标签,显示文本灬图片
label.pack()                                #将标签添加到root主窗口
button1 = tkinter.Button(root,                         
                         anchor = tkinter.E,
                         text = 'button1',
                         width = 40,
                         height = 5,
                         bg = 'red',
                         bd = 2,
                         font = 45,
                         state = tkinter.DISABLED)  #生成button1
button1.pack()
button2 = tkinter.Button(root, text = 'button2')  #生成button1
button2.pack(side = tkinter.LEFT)
                         
entry1 = tkinter.Entry(root,
                       bg = 'yellow',
                       selectforeground = 'red')
entry1.pack()

edit1 = tkinter.Text(root)
edit1.pack()

menu = tkinter.Menu(root)
submenu = tkinter.Menu(menu, tearoff = 0)
submenu.add_command(label = 'open')
submenu.add_separator()
submenu.add_command(label = 'save')
menu.add_cascade(label = 'file', menu = submenu)

root.config(menu = menu)

root.mainloop()     
