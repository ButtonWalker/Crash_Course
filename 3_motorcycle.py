motorcycle = ['honda', 'yamaha', 'suzuki']
motorcycle.insert(0, 'ducati')
print(motorcycle)

del motorcycle[0]
print(motorcycle)

motorcycle.append('ducati')
print(motorcycle)

motorbike = []
motorbike.append('honda')
motorbike.append('yamaha')
motorbike.append('suzuki')
print(motorbike)

motorcycle = ['honda', 'yamaha', 'suzuki']
print(motorcycle)

popped_motorcycle = motorcycle.pop()
print(motorcycle)
print(popped_motorcycle)

motorcycle = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycle.pop(0)
print('the last motorcycle I owned was a ' + last_owned.title() + '.')

motorcycle = ['honda', 'yamaha', 'suzuki', 'ducati']
too_exspensive = 'ducati'
motorcycle.remove(too_exspensive)
print(motorcycle)
print('\nA ' + too_exspensive.title() + ' is way too exspensive for me.')