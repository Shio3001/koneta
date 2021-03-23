import tkinter as tk
from PIL import Image, ImageTk
import datetime

class canvas_data:
    def __init__(self):
        self.window = tk.Tk()
        self.canvas = tk.Canvas(self.window, highlightthickness=0, width=100, height=100)
        self.image_pil = None
        self.image_tk = None


    def t(self):

        start_time =  datetime.datetime.now()

        self.window.resizable(width=True, height=True)
        self.window.geometry("{0}x{1}".format(100, 200))
        
        self.canvas.place(x=0,y=0,width=1280, height=720)


        #self.canvas.create_image(0, 0, anchor='nw', image=self.image_tk)

        exit_time =  datetime.datetime.now()

        print(exit_time - start_time)


        window_menubar = tk.Menu(self.window)

        menubar_list = [["test","test2",self.testtt]]

        for bar in menubar_list:

            main_bar = ""
            bar_name = []
            bar_prg = []
            # 奇数と偶数逆じゃん!とおもったら配列は0からはじまりました
            for i, content in enumerate(bar):
                if i == 0:
                    main_bar = content
                elif i % 2 == 0:
                    bar_prg.append(content)
                    # #print("bar偶数情報", content, i)
                elif (i + 1) % 2 == 0:
                    bar_name.append(content)
                    # #print("bar奇数情報", content, i)

            pull_down = tk.Menu(window_menubar, tearoff=0)

            window_menubar.add_cascade(label=main_bar, menu=pull_down)  # それぞれ

            for n, p in zip(bar_name, bar_prg):
                pull_down.add_command(label=n, command=p)

        self.window.config(menu=window_menubar)
        self.window.update()

        self.window.mainloop()

    def testtt(self):

        start_time1 =  datetime.datetime.now()

        self.image_pil = Image.open('j.jpg')
        self.image_tk = ImageTk.PhotoImage(self.image_pil)  # ImageTkフォーマットへ変換


        start_time0 =  datetime.datetime.now()
        self.image_tk = ImageTk.PhotoImage(self.image_pil)  # ImageTkフォーマットへ変換

        start_time =  datetime.datetime.now()
        self.canvas.create_image(0,0,anchor='nw', image=self.image_tk)
        exit_time =  datetime.datetime.now()

        c = exit_time - start_time1
        a = exit_time - start_time0
        b = exit_time - start_time

        print(c)
        print(a)
        print(b)



canvas_dataAAA = canvas_data()
canvas_dataAAA.t()


