"""
Round any given number to the closest 0.5 step

I.E.

round05(4.2) = 4
round05(4.3) = 4.5
round05(4.6) = 4.5
round05(4.8) = 5"""

def round05(n):
    return round(2 * n) / 2

if __name__ == '__main__':
	
	assert round05(4.2) == 4
	assert round05(4.3) == 4.5
	assert round05(4.6) == 4.5
	assert round05(4.8) == 5