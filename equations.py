def result(x):
	return float('%0.6f' % x)

def atseret(num):
	if num==0.0:
		return 1.0
	if num<0.0:
		return 0.0
	t=1.0
	v=1.0
	while t<=num:
		v=v*t
		t=t+1
	return v


def absolut(y):
	if y<0.0:
		y=-y
	return y
	

def maarih(num,n):
	w=1.0
	exp=1.0
	while w<=num:
		exp=exp*n
		w=w+1
	return result(exp)


def exponent(x):
	num=1.0
	exp=1.0
	new=1.0
	n=absolut(x)
	while new>0.0:
		new=maarih(num,n)/atseret(num)
		exp=exp+new
		num=num+1.0
	if x<0.0:
		return result(1/exp)
	else:
		return result(exp)



def Ln(x):
	if x<=0.0:
		return 0.0
	Y=x-1.0
	Ybefore=1.0
	while True:
		Ybefore=Y
		Y=Ybefore+2*((x-exponent(Ybefore))/(x+exponent(Ybefore)))
		Eps=absolut(Y-Ybefore)
		if Eps<=0.001:
			return result(Y)

def XtimesY(x,y):
	if x<=0.0:
		return 0.0
	Xy=exponent(y*Ln(x))
	return result(Xy)

def sqrt(x,y):
	if x==0:
		return 0.0
	answer=XtimesY(y,1/x)
	return result(answer)

def calculate(x):
	if x<=0.0:
		return 0.0
	y=exponent(x)*XtimesY(7,x)*XtimesY(x,-1.0)*sqrt(x,x)
	return result(y)	
