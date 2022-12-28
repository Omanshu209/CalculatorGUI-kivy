from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.core.window import Window

Num=1
Oper=0
Dot=0
OB=0

Window.size=Window.size

Builder.load_file("CalculatorDesign.kv")

class MyLayout(Widget):
	global Num,Oper,Dot
	def F0(self):
		global Num,Oper,Dot
		self.ids.main_screen.text+='0'
		Num+=1
		if Oper>0:
			Dot=0
		Oper=0
	def F1(self):
		global Num,Oper,Dot
		self.ids.main_screen.text+='1'
		Num+=1
		if Oper>0:
			Dot=0
		Oper=0
		Mul=0
	def F2(self):
		global Num,Oper,Dot
		self.ids.main_screen.text+='2'
		Num+=1
		if Oper>0:
			Dot=0
		Oper=0
	def F3(self):
		global Num,Oper,Dot
		self.ids.main_screen.text+='3'
		Num+=1
		if Oper>0:
			Dot=0
		Oper=0
	def F4(self):
		global Num,Oper,Dot
		self.ids.main_screen.text+='4'
		Num+=1
		if Oper>0:
			Dot=0
		Oper=0
	def F5(self):
		global Num,Oper,Dot
		self.ids.main_screen.text+='5'
		Num+=1
		if Oper>0:
			Dot=0
		Oper=0
	def F6(self):
		global Num,Oper,Dot
		self.ids.main_screen.text+='6'
		Num+=1
		if Oper>0:
			Dot=0
		Oper=0
	def F7(self):
		global Num,Oper,Dot
		self.ids.main_screen.text+='7'
		Num+=1
		if Oper>0:
			Dot=0
		Oper=0
	def F8(self):
		global Num,Oper,Dot
		self.ids.main_screen.text+='8'
		Num+=1
		if Oper>0:
			Dot=0
		Oper=0
	def F9(self):
		global Num,Oper,Dot
		self.ids.main_screen.text+='9'
		Num+=1
		if Oper>0:
			Dot=0
		Oper=0
	def FAC(self):
		global Num,Oper
		self.ids.main_screen.text=""
		Num=0
		Oper=0
	def FCE(self):
		global Num,Oper
		if len(self.ids.main_screen.text)>0:
			self.ids.main_screen.text=self.ids.main_screen.text[:-1]
			if Num>1:
				Num-=1
				Oper=0
			else:
				Num=0
				if len(self.ids.main_screen.text)>0:
					Oper+=1
				else:
					Oper=0
	def FA(self):
		global Num,Oper
		if Num>0:
			self.ids.main_screen.text+='+'
			Num=0 
			Oper+=1
	def FS(self):
		global Num,Oper
		if Oper==0:
			self.ids.main_screen.text+='-'
			Num=0
			Oper+=1
	def FM(self):
		global Num,Oper
		if Num>0:
			self.ids.main_screen.text+='*'
			Num=0 
			Oper+=1
	def FD(self):
		global Num,Oper
		if Num>0:
			self.ids.main_screen.text+='/'
			Num=0 
			Oper+=1
	def FOB(self):
		global Num,Oper,OB
		if Num==0:
			self.ids.main_screen.text+="("
			Num=0
			Oper=0
			OB+=1
	def FP(self):
		global Num,Oper,Dot
		if Num>0 and Dot==0:
			self.ids.main_screen.text+="."
			Num=0
			Oper=0
			Dot+=1
	def FCB(self):
		global Num,Oper,OB 
		if Num>0 and OB>0:
			self.ids.main_screen.text+=")"
			Oper=0
			OB-=1
	def FE(self):
		if len(self.ids.main_screen.text)>0 and Num>0:
			try:
				self.ids.main_screen.text=str(eval(self.ids.main_screen.text))
			except:
				self.ids.main_screen.text='ER'

class Calculator(App):
	def build(self):
		return MyLayout()
		
if __name__=="__main__":
	Calculator().run()
