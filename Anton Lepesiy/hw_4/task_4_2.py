
name = ['Ivan', 'Ivanou']
city = 'Minsk'
country = 'Belsrus'

a = ' '.join(name)  # преобразование списка в строку

print('Привет,' + a + '! ' + 'Добро пожаловать в ' + city + ' ' + country)
# metod 2:
print('Привет, {name}! Добро пожаловать в {city} {country}'.format(name=a, city="Minsk", country='Belsrus'))
