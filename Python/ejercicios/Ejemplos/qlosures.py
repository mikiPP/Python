def marker(N):
	def action(X):
		print(X ** N)
		return X ** N

	return action

f = marker (2) #aqui guarda la funcion action porque maker devuelve action y por lo tanto pasa de ser
# local a global (LEBG)  (funcion factoria porque construye funciones)
f(3)
f(4)