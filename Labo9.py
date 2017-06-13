class Contador():

	rebase = int(0)

	def __init__(self, c, m):
		self.c = c
		self.m = m

	def getCuenta(self):
		return self.c

	def getMax(self):
		return self.m

	def getRebase(self):
		return rebase

	def setCuenta(self, c):
		self.c = int(c)

	def setMax(self,m):
		self.m - int (m)

	def setRebase(self, r):
		self.rebase= int(r)

	def contar(self):
		if self.c < self.m:
			self.c = self.c+1
		else:
			self.c-0
			self.rebase=1

	def borrarRebase(self):
		self.rebase =0

class Mes(Contador):

	out= int(0)
	nombre = ""
	def __init__(self,c,m,n):
		super().__init__(c,m)
		self.n = n


	def setNombre(self):
		pass

	def getNombre(self, n):
	
	    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
	    a=months.index(n) + 1
	    import calendar
	    import datetime
	    print(calendar.monthrange(2012,a)[1])

class Reloj(Contador):

	def __init__(self,s,min,h): #NO DEBE DE CONFUNDIRSE MINUTOS CON M DE MAXIMUM
		super().__init__(m)
		self.s = s
		self.h=h
		

	def tic(self):
		pass

class Calendario(Mes):
	pass

		
	        





# instancia = Contador(30,50)
# print(instancia.c)
# instancia.setCuenta(600)
# instancia.setRebase(402)

inst = Mes(40,50,'Nov')
inst.getNombre('Nov')





