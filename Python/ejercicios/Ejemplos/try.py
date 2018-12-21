sep = '-' * 45 +'\n'

print(sep + 'EXEPTION RAISED AND CAUGHT')
try:
	x=7/0

except ZeroDivisionError:

	print('except run')

finally:
	print('finally run')
print('after run')

print(sep + 'NO EXEPTION RAISED')
try:
	x = 'spam'[3]

except IndexError:
	print('except run')
finally:
	print('finally run')
print('after run')

print(sep + 'NO EXCEPTION RAISED, WITH ELSE')
try:
	x = 'spam'[3]
except IndexError:
	print('except run')
else:
	print('else run')
finally:
	print('finally run')
	print('after run')
	print(sep + 'EXCEPTION RAISED BUT NOT CAUGHT')
try:
	x = 1 / 0
except ZeroDivisionError:
	print('except run')
else:
	print('teoria fallida')
finally:
	print('finally run')
	print('after run')