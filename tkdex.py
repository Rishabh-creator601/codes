import tkinter as tk 
from tkinter import ttk 
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
from matplotlib.figure import Figure 

matplotlib.use("TkAgg")





class StartPage(tk.Frame):

	def __init__(self,parent,controller):

		tk.Frame.__init__(self,parent)



		label =ttk.Label(self,text="This is Start Page ").pack()


		b1 = ttk.Button(self,text="Visit Page 1",command=lambda :controller.show_frame(1))
		b2 = ttk.Button(self,text='Visit Page 2',command=lambda : controller.show_frame(2))
		b3 = ttk.Button(self,text='Graph Page',command=lambda : controller.show_frame(3))



		b1.pack()
		b2.pack()
		b3.pack()








class PageOne(tk.Frame):

	def __init__(self,parent,controller):

		tk.Frame.__init__(self,parent)



		label =ttk.Label(self,text="This is  Page 1").pack()


		b1 = ttk.Button(self,text="< Back To Home",command=lambda :controller.show_frame(0))
		b2 = ttk.Button(self,text='Visit Page 2',command=lambda : controller.show_frame(2))
		b3 = ttk.Button(self,text='Graph Page',command=lambda : controller.show_frame(3))



		b1.pack()
		b2.pack()
		b3.pack()


		




class PageTwo(tk.Frame):

	def __init__(self,parent,controller):

		tk.Frame.__init__(self,parent)



		label =ttk.Label(self,text="This is Page 2 ").pack()


		b1 = ttk.Button(self,text="Back To Home",command=lambda :controller.show_frame(0))
		b2 = ttk.Button(self,text='Visit Page 1',command=lambda : controller.show_frame(1))
		b3 = ttk.Button(self,text='Graph Page',command=lambda : controller.show_frame(3))



		b1.pack()
		b2.pack()
		b3.pack()




class PageThree(tk.Frame):

	def __init__(self,parent,controller):

		tk.Frame.__init__(self,parent)



		label =ttk.Label(self,text="Graph Wala Page").pack(padx=10,pady=10)


		b1 = ttk.Button(self,text="To Home",command=lambda :controller.show_frame(0))
		b2 = ttk.Button(self,text='Visit Page 1',command=lambda : controller.show_frame(1))


		b1.pack()
		b2.pack()




		f = Figure(figsize=(5,5),dpi=100)
		a = f.add_subplot(111)
		a.plot([1,2,3,4,5],[2,4,5,68,9])


		canvas = FigureCanvasTkAgg(f,self)
		canvas.draw()

		canvas.get_tk_widget().pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)



		toolbar = NavigationToolbar2Tk(canvas,self)
		toolbar.update()

		canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)






class SeaofBTCapp(tk.Tk):

	def __init__(self,*args,**kwargs):



		tk.Tk.__init__(self,*args,**kwargs)

		container = tk.Frame(self)
		container.pack(side="top",fill="both",expand=True)


		container.grid_rowconfigure(0,weight=1)
		container.grid_columnconfigure(0,weight=1)


		self.frames  = {}


		frame =StartPage(container,self)

		one = PageOne(container,self)
		two = PageTwo(container,self)



		pages = [StartPage,PageOne,PageTwo,PageThree]





		for idx,F in enumerate(pages):

			frame = F(container,self)

			self.frames[idx] = frame

			frame.grid(row=0,column=0,sticky='nsew')




		


		self.show_frame(0)




	def show_frame(self,cont):

		frame = self.frames[cont]
		frame.tkraise()





app = SeaofBTCapp()
app.geometry("400x100")
app.mainloop()

