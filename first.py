import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
class work:
    def __init__(self):
        
        root = tk.Tk()
        self.string = tk.StringVar()
        self.data = []
        label1 = tk.Label(root,text = "Enter comma seprated words")
        label1.grid(row  =0,column = 0,sticky="w")

        entry1 = tk.Entry(root,textvariable=self.string)
        entry1.grid(row=1,column = 0,sticky="w")
        
        button1 = tk.Button(root,text = "word",command = lambda : self.extract())
        button1.grid(row  = 2,column = 0,sticky="w")

        # self.start()
        root.mainloop()
    def extract(self):
        self.data = [x for x in self.string.get().split(',')]
        self.start()
    def start(self):
        result = [0 for i in range(0,len(self.data))]
        
        files= [".//database//test1.txt",".//database//test2.txt",".//database//test3.txt",".//database//test4.txt",".//database//test5.txt"]
        
        for file in files:
            fileobj = open(file,'r')
            string = fileobj.read()
            ls = []
            ls = string.split(' ')
            temp = -1
            for word in self.data:
                temp += 1
                counter=0
                for str in ls:
                    if(word == str):
                        counter+=1
                result[temp] +=counter
            fileobj.close()
        print(result)
        self.ploting(result)

    def ploting(self,ls):
        x = np.array(self.data)
        y = np.array(ls)
        plt.style.use('ggplot')
        matplotlib.use( 'tkagg' )
        plt.bar(x,y)
        plt.show()
obj = work()