#Fireworks

from time import sleep

year=int(input('Enter the current year:\n'))

for countdown in range (10, -1, -1):
	print(countdown)
	sleep(1)

print(f'''Boom!
Happy {year}!!!''')
