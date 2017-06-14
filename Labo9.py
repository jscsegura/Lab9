# class Contador():

# 	rebase = int(0)

# 	def __init__(self, c, m):
# 		self.c = c
# 		self.m = m

# 	def getCuenta(self):
# 		return self.c

# 	def getMax(self):
# 		return self.m

# 	def getRebase(self):
# 		return rebase

# 	def setCuenta(self, c):
# 		self.c = int(c)

# 	def setMax(self,m):
# 		self.m - int (m)

# 	def setRebase(self, r):
# 		self.rebase= int(r)

# 	def contar(self):
# 		if self.c < self.m:
# 			self.c = self.c+1
# 		else:
# 			self.c-0
# 			self.rebase=1

# 	def borrarRebase(self):
# 		self.rebase =0

class Mes(object):

	out= int(0)
	nombre = ""
	def __init__(self,mes):
		self.mes = mes

	def getNombre(self, n):
	
	    months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
	    a=months.index(n) + 1
	    import calendar
	    import datetime
	    print(calendar.monthrange(2012,a)[1])

class Reloj(object):

	def __init__(self,hours,minutes,seconds): #NO DEBE DE CONFUNDIRSE MINUTOS CON M DE MAXIMUM
		#super().__init__()
		self.set(hours, minutes,seconds)

	def set(self, hours, minutes, seconds):
		if type(hours) == int and 0 <= hours and hours < 24:
		            self.hours = hours
		else:
			raise TypeError("Las horas deben de estar entre 0 y 23!")
		if type(minutes) == int and 0 <= minutes and minutes < 60:
			self.minutes = minutes 
		else:
			raise TypeError("Los minutos deben ser entre 0 y 59!")
		if type(seconds) == int and 0 <= seconds and seconds < 60:
			self.seconds = seconds
		else:
			raise TypeError("Los segundos deben de ser entre 0 y 59")

	def tic(self):
		if self.seconds == 59:
			self.seconds = 0
			if self.minutes == 59:
				self.minutes = 0
				if self.hours == 23:
					self.hours = 0
				else:
					self.hours += 1
			else:
				self.minutes += 1
		else:
			self.seconds += 1

	def __str__(self):
		return "{0:02d}:{1:02d}:{2:02d}".format(self.hours,self.minutes,self.seconds)

	def display(self):
		return "{0:02d}:{1:02d}:{2:02d}".format(self.hours,self.minutes,self.seconds)


class Calendario(object):

	months = (31,28,31,30,31,30,31,31,30,31,30,31)
	def __init__(self, dia,mes,año): 
		self.set(dia,mes,año)

	@staticmethod
	def anoBisiesto(año):
		if not año%4==0:
			return False
		elif not año % 100==0:
			return True
		elif not año % 400 == 0:
			return False
		else:
			return True

	def set(self,dia,mes,año):
		if type(dia)==int and type(mes)==int and type(año)==int:
			self.dia= dia
			self.mes = mes
			self.año = año
		else:
			TypeError ("el día, mes y año deben de ser números enteros!")

	def avanzarDia(self):
		
		maxdias = Calendario.months[self.mes-1]
		if self.mes==2 and Calendario.anoBisiesto(self.año):
			maxdias+=1
		if self.dia==maxdias:
			self.dia=1
			if self.mes==12:
				self.mes=1
				self.año +=1
			else:
				self.mes +=1
		else:
			self.dia +=1

	def __str__(self):
		return "{0:02d}/{1:02d}/{2:4d}".format(self.mes,self.dia,self. año)


class Fecha(Reloj, Calendario):



	def __init__(self, dia, mes, año, hours , minutes,seconds):
		self.dia =dia
		self.mes =mes
		self.año = año
		self.hours=hours
		self.minutes=minutes
		self.seconds = seconds
		Reloj(hours,minutes,seconds)
		Calendario(dia, mes, año)
		Mes(mes)

	def avanzar(self):
		horaAnterior= self.hours
		Reloj.tic(self)
		if (self.hours < horaAnterior):
			self.avanzarDia()

	def __str__(self):
		return "{} de {} del {}".format(self.dia,self.mes,self.año)






# instancia = Contador(30,50)
# print(instancia.c)
# instancia.setCuenta(600)
# instancia.setRebase(402)

# inst = Mes(40,50,'Nov')
# inst.getNombre('Nov')
# x=Reloj(23,59,59)
# print(x)
# x.tic()
# print(x)
# inst2=Calendario(28,2,2012)
# inst2.avanzarDia()
# print(inst2)

# import calendar-
# import datetime
# print(calendar.monthrange(2012,4)[1])

x=Fecha(28,2,2012,23,59,59)


x.avanzar()
print(x)

# x.tic()



