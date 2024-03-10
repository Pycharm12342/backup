# from tkinter import *
#
# def create_window_with_question(font_size, text, fg, bg):
#     window = Tk()
#     window.title("daa")
#     window.geometry("600x700")
#
#     hh = Label(text=text, fg=fg, bg=bg,font=("comic sans ms", font_size))
#     hh.pack()
#     mainloop()
# create_window_with_question(25, 'lable1', 'red', 'green')
# create_window_with_question(15, 'lable2', 'orange', 'blue')

############

# from tkinter import *
#
#
# def calculator(buttons, font_size, bg, but_color, x_y):
#     window = Tk()
#     window.title("daa")
#     window.geometry(f'{x_y[0]}x{x_y[1]}')
#
#     def def_text(elem):
#         if entre.get()=="error":
#             clear_f()
#         main_text.set(entre.get() + elem)
#
#     main_text = StringVar()
#
#     def clear_f():
#         main_text.set("")
#
#     def solve_f():
#         try:
#             main_text.set(eval(entre.get()))
#         except:
#             main_text.set("error")
#
#     entre = Entry(font=("comic sans ms", font_size), textvariable=main_text)#state="disabled"
#     entre.grid(row=0, columnspan=4, ipady=20, pady=4)
#
#     but7 = Button(text=buttons[0], command=lambda: def_text("7"), font=("comic sans ms", font_size))
#     but7.grid(row=1, column=0, padx=4, pady=4)
#
#     but8 = Button(text=buttons[1], command=lambda: def_text("8"), font=("comic sans ms", font_size))
#     but8.grid(row=1, column=1, padx=4, pady=4)
#
#     but9 = Button(text=buttons[2], command=lambda: def_text("9"), font=("comic sans ms", font_size))
#     but9.grid(row=1, column=2, padx=4, pady=4)
#
#     butD = Button(text=buttons[3], command=lambda: def_text("-"), font=("comic sans ms", font_size))
#     butD.grid(row=1, column=3, padx=4, pady=4)
#
#     butG = Button(text=buttons[4], command=lambda: def_text("4"), font=("comic sans ms", font_size))
#     butG.grid(row=2, column=0, padx=4, pady=4)
#
#     but5 = Button(text=buttons[5], command=lambda: def_text("5"), font=("comic sans ms", font_size))
#     but5.grid(row=2, column=1, padx=4, pady=4)
#
#     but6 = Button(text=buttons[6], command=lambda: def_text("6"), font=("comic sans ms", font_size))
#     but6.grid(row=2, column=2, padx=4, pady=4)
#
#     butT = Button(text=buttons[7], command=lambda: def_text("+"), font=("comic sans ms", font_size))
#     butT.grid(row=2, column=3, padx=4, pady=4)
#
#     but0 = Button(text=buttons[8], command=lambda: def_text("1"), font=("comic sans ms", font_size))
#     but0.grid(row=3, column=0, padx=4, pady=4)
#
#     but1 = Button(text=buttons[9], command=lambda: def_text("2"), font=("comic sans ms", font_size))
#     but1.grid(row=3, column=1, padx=4, pady=4)
#
#     but2 = Button(text=buttons[10], command=lambda: def_text("3"), font=("comic sans ms", font_size))
#     but2.grid(row=3, column=2, padx=4, pady=4)
#
#     but3 = Button(text=buttons[11], command=lambda: def_text("0"), font=("comic sans ms", font_size))
#     but3.grid(row=3, column=3, padx=4, pady=4)
#
#     butC = Button(text=buttons[12], command=clear_f, font=("comic sans ms", font_size))
#     butC.grid(row=4, column=0, padx=4, pady=4)
#
#     butH = Button(text=buttons[13], command=lambda: def_text("*"), font=("comic sans ms", font_size))
#     butH.grid(row=4, column=1, padx=4, pady=4)
#
#     butF = Button(text=buttons[14], command=solve_f, font=("comic sans ms", font_size))
#     butF.grid(row=4, column=2, padx=4, pady=6)
#
#     butV = Button(text=buttons[15], command=lambda: def_text("/"), font=("comic sans ms", font_size))
#     butV.grid(row=4, column=3, padx=4, pady=4)
#
#     mainloop()
#
#
# buttons = ("7", "8", "9", "-", "4", "5", "6", "+", "1", "2", "3", "0", "C", "*", "=", "/")  # всі кнопки 15 штук
# calculator(buttons, 14, "red", 'grey', (240, 300))

#############
# from tkinter import *
# import random
# window = Tk()
# window.title("daa")
# window.geometry("300x300")
#
# def randoom():
#     lable["text"] = random.randint(1, 50)
#
# lable = Label(text="Random", )
# lable.grid(row=1, columnspan=1, ipady=20, pady=4)
#
# but = Button(font=("comic sans ms", 22, "bold", "underline"), text="Push", command=randoom)
# but.grid(row=2, columnspan=21, ipady=20, pady=4)
#
# mainloop()

##############
# arguments-в середині дужок функції () тільки є утонченя
# from tkinter import *
# import random
# window = Tk()
# window.title("daa")
# window.geometry("500x500")
#
# def h(event):
#     lable.place(x= random.randint(1, 500), y=random.randint(1, 500))
#
# lable = Label(text="Snake" )
# lable.place(x=150, y=60,)
# lable.bind("<Button-1>", h)
# mainloop()

######

# from tkinter import *
# window = Tk()
# window.title("daa")
# screen_left = 0
# screen_right = 500
# screen_down = 500
# screen_up = 0
# window.geometry(f"{screen_right}x{screen_down}")
# window.resizable(False, False)
# l_y = 180
# l_x = 180
# step = 5
#
# lable_x_s = 45
# lable_y_s = 10
#
# def moving_up(event):
#     global l_y
#     if l_y > screen_up:
#         l_y -= step
#         lable.place(y=l_y)
#
# def moving_down(event):
#     global l_y
#     if l_y + lable_y_s < screen_down:
#         l_y += step
#         lable.place(y=l_y)
#
# def moving_left(event):
#     global l_x
#     if l_x > screen_left:
#         l_x -= step
#         lable.place(x=l_x)
#
# def moving_right(event):
#     global l_x
#     if lable_x_s + l_x < screen_right:
#         l_x += step
#         lable.place(x=l_x)
#
# lable = Label(text="Snake")
# lable.place(x=l_x, y=l_y, width=lable_x_s, height=lable_y_s)
#
# window.bind("<w>", moving_up)
# window.bind("<s>", moving_down)
# window.bind("<a>", moving_left)
# window.bind("<d>", moving_right)
#
# but_up = Button(font=("comic sans ms", 22, "bold", "underline"), command=moving_up, text="up")
# but_up.place(x=215, y=300)
#
# but_down = Button(font=("comic sans ms", 22, "bold", "underline"), command=moving_down, text="down")
# but_down.place(x=200, y=400)
#
# but_left = Button(font=("comic sans ms", 22, "bold", "underline"), command=moving_left, text="left")
# but_left.place(x=100, y=400)
#
# but_right = Button(font=("comic sans ms", 22, "bold", "underline"), command=moving_right, text="right")
# but_right.place(x=320, y=400)
#
# lable.bind("<w>", moving_up)
# lable.bind("<s>", moving_down)
# lable.bind("<a>", moving_left)
# lable.bind("<d>", moving_right)#-колізія
# mainloop()

###

# from tkinter import *
# from resourses.colors import colors_list
# import random
# window = Tk()
# window.title("daa")
# screen_left = 0
# screen_right = 600
# screen_down = 400
# screen_up = 0
# window.geometry(f"{screen_right}x{screen_down}")
# window.resizable(False, False)
# x = 180
# y = 180
# label_size_x = 60
# label_size_y = 30
# step_x = 1
# step_y = 1

# i = 0

# def move():
#     global x,y,step_y,step_x, i
#     while True:
#         if x + label_size_x > screen_right:
#             step_x *= -1
#             label["fg"] = colors_list[random.randint(0, 685)]
# #             i += 1
#         if x < screen_left:
#             step_x *= -1
#             label["fg"] = colors_list[random.randint(0, 685)]
# #             i += 1
#         if y < screen_up:
#             step_y *= -1
#             label["fg"] = colors_list[random.randint(0, 685)]
# #             i +=1
#         if y + label_size_y > screen_down:
#             step_y *= -1
#             label["fg"] = colors_list[random.randint(0, 685)]
# #             i += 1
#         x += step_x
#         y += step_y
#         label.place(x= x, y=y)
#         window.update()
#         window.after(1)
#
#
# label = Label(text="DVD", font=("Century", 22), foreground=colors_list[0])
# label.place(x= x, y=y, width=label_size_x, height=label_size_y)
# move()

###

# from tkinter import *
# from resourses.colors import colors_list
# import random
# window = Tk()
# window.title("daa")
# screen_left = 0
# screen_right = 600
# screen_down = 400
# screen_up = 0
# window.geometry(f"{screen_right}x{screen_down}")
# window.resizable(False, False)
# x = 180
# y = 180
# label_size = 40
# step_x = 1
# step_y = 1
#
# # i = 0
#
#
# def move():
#     global x, y, step_y, step_x, i, label_size
#     while True:
#         if x + label_size > screen_right or x < screen_left:
#             step_x *= -1
#             label["bg"] = colors_list[random.randint(0, 685)]
#             label_size += 10
# #             i += 1
#         if y < screen_up or y + label_size > screen_down:
#             step_y *= -1
#             # label_size += 10
#             label["bg"] = colors_list[random.randint(0, 685)]
# #             i +=1
#         x += step_x
#         y += step_y
#         label.place(x=x, y=y)
#         window.update()
#         window.after(5)
#
#
# label = Label(font=("Century", 10), background=colors_list[0])
# label.place(x=x, y=y, width=label_size, height=label_size)
# move()

####

# from tkinter import *
#
# def dd():
#     text = ""
#     if var.get() == 1:
#         text = "Ви вибрали кошку"
#     if var.get() == 2:
#         text = "Ви вибрали собаку"
#     if var.get() == 3:
#         text = "Ви вибрали пташку"
#     if var.get() == 4:
#         text = "Ви вибрали курку"
#     if var.get() == 5:
#         text = "Ви вибрали черепашка"
#     lbl['text'] = text
#
#
# window = Tk()
# window.title("daa")
# screen_right = 600
# screen_down = 400
# window.geometry(f"{screen_right}x{screen_down}")
#
# var = IntVar()
#
# r1 = Radiobutton(text="Кишку", font=22, variable=var, value=1)
# r1.place(x=20, y=40)
# r2 = Radiobutton(text="Собачку", font=22, variable=var, value=2)
# r2.place(x=20, y=80)
# r3 = Radiobutton(text="Патушку", font=22, variable=var, value=3)
# r3.place(x=20, y=120)
# r4 = Radiobutton(text="Курку", font=22, variable=var, value=4)
# r4.place(x=20, y=160)
# r5 = Radiobutton(text="Черепашка", font=22, variable=var, value=5)
# r5.place(x=20, y=200)
#
# but = Button(text='OK', command=dd)
# but.place(x=20, y=240)
#
# lbl = Label(font=22, text="")
# lbl.place(x=300, y=40)
#
# mainloop()

####

# from tkinter import *
#
# def dd():
#     text = ""
#     if var.get() == 1:
#         text = "Ви вибрали кошку"
#         lbl_image['image'] = cat
#     if var.get() == 2:
#         text = "Ви вибрали собаку"
#         lbl_image['image'] = dog
#     if var.get() == 3:
#         text = "Ви вибрали пташку"
#         lbl_image['image'] = bird
#     if var.get() == 4:
#         text = "Ви вибрали курку"
#         lbl_image['image'] = chican
#     if var.get() == 5:
#         lbl_image['image'] = cherepaha1
#     lbl['text'] = text
#     lbl_image.place(x=300, y=90, width=200, height=200)
#
#
# window = Tk()
# window.title("daa")
# screen_right = 600
# screen_down = 400
# window.geometry(f"{screen_right}x{screen_down}")
# cat = PhotoImage(file="cat.png")
# dog = PhotoImage(file="dog.png")
# bird = PhotoImage(file="bird.png")
# chican = PhotoImage(file="chican.png")
# cherepaha1 = PhotoImage(file="cherepaha1.png")
# var = IntVar()
#
#
# r1 = Radiobutton(text="Кишку", font=22, variable=var, value=1)
# r1.place(x=20, y=40)
# r2 = Radiobutton(text="Собачку", font=22, variable=var, value=2)
# r2.place(x=20, y=80)
# r3 = Radiobutton(text="Патушку", font=22, variable=var, value=3)
# r3.place(x=20, y=120)
# r4 = Radiobutton(text="Курку", font=22, variable=var, value=4)
# r4.place(x=20, y=160)
# r5 = Radiobutton(text="Черепашка", font=22, variable=var, value=5)
# r5.place(x=20, y=200)
#
# but = Button(text='OK', command=dd)
# but.place(x=20, y=240)
#
# lbl = Label(font=22, text="")
# lbl.place(x=300, y=40)
#
# # широта висота проблема з картинкою
# lbl_image = Label(image="")
# lbl_image.place(x=300, y=90)
#
# mainloop()

###

# from tkinter import *
# from random import shuffle
# def add(img, question, *answers):
#     correct = answers[0]
#     answers = list(answers)
#     shuffle(answers)
#     correct = answers.index(correct)
#     def d(img):
#         if var.get() == correct:
#             window.destroy()
#             window1 = Tk()
#             window1.title("daa")
#             window1.geometry("600x700")
#             img = PhotoImage(file=img)
#             Label(image=img).pack()
#             window1.update()
#             window1.after(3000)
#             window1.destroy()
#         else:
#             print("Not correct")
#
#     window = Tk()
#     window.title("daa")
#     window.geometry("600x700")
#     var = IntVar()
#     canvas = Canvas()
#     canvas.pack(pady=150)
#     Label(canvas,text=question, font=15).pack()
#     for i in range(len(answers)):
#         Radiobutton(canvas, text=answers[i], variable=var, value=i).pack()
#     Button(canvas,text="Push", command=lambda: d(img)).pack()
# ##LAMBDA - ВИКОРИСТОВУЄТЬСЯ В РЯДОЧКУ ЛИШЕ 1 РАЗ
#     mainloop()
# add("spider.png", "До якого виду відносяться павуки?", "павуки", "комахи", "тварини", 'птахи')
# add("spider.png",'питання2', '1', '2', '3', '4')

# from tkinter import *
# from random import randint, shuffle
# window = Tk()
# window.title("daa")
# window.geometry("600x800")
#
#
# lst = [1, 2, 3]
# correct = lst[0]
# shuffle(lst)
# correct = lst.index(correct)
# print(correct)
# def d():
#     if var ==correct:
#         print("Correct")
#     else:
#         print("Not correct")
#
# main_canvas = Canvas()
# main_canvas.pack(pady=150)
#
# var = IntVar()
#
# Label(canvas1, text="QUESTION1").pack(pady=10)
# Radiobutton(canvas1, text="dsad", variable=var, value=0).pack(pady=5)
# Radiobutton(canvas1, text="dsad", variable=var, value=1).pack(pady=5)
# Button(cavas1, text="button", command=d).pack(pady=10)
###
# from tkinter import *
# window = Tk()
# window.title("daa")
# window.geometry("600x800")
# main_canvas=Canvas()
# main_canvas.pack(pady=90)
#
# canvas = Canvas(main_canvas, bg="red")
# canvas.pack(pady=10, ipadx=5)
# Label(canvas, text="QUESTION1").pack(pady=10)
# Radiobutton(canvas, text="rdbtn").pack(pady=5)
# Radiobutton(canvas, text="rdbtn1").pack(pady=5)
# Button(canvas, text="button").pack(pady=10)
#
#
#
# canvas2 = Canvas(main_canvas, bg="red")
# canvas2.pack(pady=10, ipadx=50)
# Label(canvas2, text="QUESTION1").pack(pady=10)
# Radiobutton(canvas2, text="rdbtn").pack(pady=5)
# Radiobutton(canvas2, text="rdbtn1").pack(pady=5)
# Button(canvas2, text="button").pack(pady=10)
#
#
# canvas3 = Canvas(main_canvas, bg="red")
# canvas3.pack(pady=10, ipadx=100)
# Label(canvas3, text="QUESTION1").pack(pady=10)
# Radiobutton(canvas3, text="rdbtn").pack(pady=5)
# Radiobutton(canvas3, text="rdbtn1").pack(pady=5)
# Button(canvas3, text="button").pack(pady=10)
#
# mainloop()

###

# from tkinter import *
#
# root = Tk()
#
# lst = [1, 2, 0, 1, 2, 3, 3]
#
# for i in range(len(lst)):
#     Button(text=lst[i]).pack()
#
# mainloop()
#
#
# def func(e):
#     return e+2
#
# print(func(2))
#
# a = lambda e: e+2
# print(a(2))

# from tkinter import *
#
# root = Tk()
#
# var = IntVar()
#
# Checkbutton(text="Я хочу отримувати пропозиції на пошту", variable=var).pack()
# # Checkbutton(text="Я не хочу отримувати пропозиції на пошту", variable=var, onvalue=0).pack()
# # Button(text="Ok", command=lambda: print("Він натиснув так" if var.get() == 1 else "Він натиснув ні")).pack()
#
# def func():
#     if var.get() == 1:
#         print("Він натиснув так")
#     elif var.get() == 0:
#         print("Він натиснув ні")
# Button(text="Ok", command=func).pack()
#
# var1 = IntVar()
# Checkbutton(text="Вам є 18 років?", variable=var1).pack()
#
# def func():
#     if var1.get() == 1:
#         print("Йому є 18")
#     elif var1.get() == 0:
#         print("Йому немає 18")
# Button(text="Ok", command=func).pack()
#
# mainloop()

# коли натискаєш на чекбаттон з'являється лейбл, а коли відтискаєш - зникає
# from tkinter import *
#
# def create_lbl_with_mail(event):
#     global lbl
#     if var.get() == 0:
#         lbl = Label(text="This is mail")
#         lbl.pack()
#     if var.get() == 1:
#         lbl.destroy()
#
# Label(text="This is random text").pack()
# var = IntVar()
# check = Checkbutton(text="Створити лейбл", variable=var)
# check.pack()
#
# check.bind('<Button-1>', create_lbl_with_mail)
#
# mainloop()

# from tkinter import *
# # window = Tk()
# # window.title("daa")
# # window.geometry("600x800")
# root = Tk()
# var = IntVar()
# canvas= Canvas(background="red")
# canvas.pack()
# canvas1 = Canvas(background="red")
# canvas1.pack()
#
# Label(canvas, text="Призвіще:").pack(side="left", ipadx=40)
# Label(canvas, text="Ім'я:").pack(side="left", ipadx=40)
# Label(canvas, text="По батькові:").pack(side="left", ipadx=40)
# entry_name1 = Entry(canvas1).pack(side="left")
# entry_name2 = Entry(canvas1).pack(side="left")
# entry_name3 = Entry(canvas1).pack(side="left")
# # entry_name1 = Entry().pack()
# # entry_name2 = Entry().pack()
# # entry_name3 = Entry().pack()
# Checkbutton(text="Вам є 18 років?", variable=var).pack()

# def ok():
#     if name.get().isalpha() and surname.get().isalpha() and entry2.get().isalpha():
#         file = open("form data.txt", "a")
#         file.write(f"\nName: {name.get()}\n")
#         file.write(f"Surname: {surname.get()}\n")
#         if var.get() == 1:
#             file.write("More than 18: True\n")
#         else:
#             file.write(f"More than 18: False\n")
#         messagebox.showinfo("it is fine", message="We got your data, thanks")
#     else:
#         messagebox.showinfo("problem detected", message="Check your info")
# def func():
#     if var.get() == 1:
#         print("Йому є 18")
#     elif var.get() == 0:
#         print("Йому немає 18")
# Button(text="Ok", command=func).pack()
# mainloop()

# from tkinter import *
#
# def func():
#     # тут запихаємо інфу з ентрі в файл
#     if var.get() == 1:
#         # тут запихаємо інфу з чекбаттона в файл
#         print("Йому є 18")
#     elif var.get() == 0:
#         # тут запихаємо інфу з чекбаттона в файл
#         print("Йому немає 18")
#
# root = Tk()
# var = IntVar()
#
# canvas = Canvas()
#
# # зпакували через side, все вказуємо по черзі вліво
# Label(canvas, text="Прізвище:").pack(side="left", padx=15)
# Label(canvas, text="Ім'я:").pack(side="left", padx=15)
# Label(canvas, text="По батькові:").pack(side="left", padx=15)
#
# # # згрідили через колонки
# # Label(canvas, text="Прізвище:").grid(row=0, column=0, padx=15)
# # Label(canvas, text="Ім'я:").grid(row=0, column=1, padx=15)
# # Label(canvas, text="По батькові:").grid(row=0, column=2, padx=15)
#
#
# canvas.pack()
#
# # ще один канвас для ентрі
#
# # присвоюєш ентрі щоб тоді отримати з них інфу
# entry_name = Entry()
# = Entry()
# = Entry()
#
# # спаковуєш все по черзі вліво і виставляєш відступи (padx)
# entry_name.pack()
#
#
# Checkbutton(text="Вам є 18 років?", variable=var).pack()
#
#
# Button(text="Ok", command=func).pack()
#
#
# mainloop()

# from tkinter import *
#
#
# def func():
#      entry_fathername.get() entry_surname.get()
#     # тут запихаємо інфу з ентрі в файл
#     if var.get() == 1:
#         # тут запихаємо інфу з чекбаттона в файл(консоль)
#         print("Йому є 18")
#     elif var.get() == 0:
#         # тут запихаємо інфу з чекбаттона в файл(консоль)
#         print("Йому немає 18")
#
# root = Tk()
# var = IntVar()
#
# canvas = Canvas()
#
#
# # зпакували через side, все вказуємо по черзі вліво
# Label(canvas, text="Прізвище:").pack(side="left", padx=55)
# Label(canvas, text="Ім'я:").pack(side="left", padx=55)
# Label(canvas, text="По батькові:").pack(side="left", padx=55)
#
# # # згрідили через колонки
# # Label(canvas, text="Прізвище:").grid(row=0, column=0, padx=15)
# # Label(canvas, text="Ім'я:").grid(row=0, column=1, padx=15)
# # Label(canvas, text="По батькові:").grid(row=0, column=2, padx=15)
#
#
# canvas.pack()
#
#
# # ще один канвас для ентрі
# canvas_entry = Canvas()
# # присвоюєш ентрі щоб тоді отримати з них інфу
# entry_name = Entry(canvas_entry)
# entry_surname = Entry(canvas_entry)
# entry_fathername = Entry(canvas_entry)
#
# # спаковуєш все по черзі вліво і виставляєш відступи (padx)
# entry_surname.pack(side="left", padx=15)
# entry_name.pack(side="left", padx=15)
# entry_fathername.pack(side="left", padx=15)
# canvas_entry.pack()
#
# Checkbutton(text="Вам є 18 років?", variable=var).pack()
#
#
# Button(text="Ok", command=func).pack()
#
#
# mainloop()

# from tkinter import *
#
# window = Tk()
# window.title("daa")
# window.geometry("600x300")
# canvas = Canvas()
#
# lbl = Label(canvas, font=("arial", 40), text="Wombat enimal").pack()
# lbl1 = Label(canvas, font=("arial", 20), text="Speed:").pack()
#
# mainloop()

