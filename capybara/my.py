from tkinter import *

window = Tk()
window.title("daa")
window.geometry("1000x400")
canvas_left = Canvas()
canvas_right = Canvas()
canvas_up = Canvas()
canvas_down = Canvas()


lbl_up = Label(canvas_up, font=("Lato", 40, "bold"), text="Капібара")
lbl_center = Label(canvas_up, font=("Lato", 10),  text="Капiба́ра, или водосви́нка, — полуводное травоядное \n"
                                                       "млекопитающее из подсемейства водосвинковых,\n"
                                                       " один из двух ныне существующих видов рода водосвинки. \n"
                                                       "Капибара — самый крупный среди современных грызунов.\n")
lbl_left = Label(canvas_left, font=("Lato", 10), text="Высшая классификация:\n Водосвинки\n"
                                                      "Масса:\n 35 – 66 кг (взрослая особь)\n"
                                                      "Длина:\n 1,1 – 1,3 м (взрослая особь)\n", justify=LEFT)
lbl_right = Label(canvas_right, font=("Lato", 10), text="Рост: 50 – 62 см\n (взрослая особь, В холке)\n"
                                                        "Научное название:\n Hydrochoerus hydrochaeris\n"
                                                        "Период беременности:\n 130 – 150 дней", justify=RIGHT)
lbl_down = Label(canvas_down, font=("Lato", 15, "bold"), text="Південна Америка")

capibara_down = PhotoImage(file="capybara-square-1.jpg.optimal.png")
Label(canvas_down, image=capibara_down).pack(side="left")

lbl_down.pack(pady=10, side="left")

capibara_down1 = PhotoImage(file="Carpincho_en_el_Parque_Nacional_El_Palmar.png")
Label(canvas_down, image=capibara_down1).pack(side="left")

lbl_up.pack(pady=15)
lbl_center.pack()
canvas_up.pack(pady=10)

lbl_left.pack()
canvas_left.pack(side="left")

lbl_right.pack()
canvas_right.pack(side="right")

canvas_down.pack(pady=40)

mainloop()
#test