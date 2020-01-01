import random

dishes = ['Biryani', 'Burger', 'Rice-Curry-Omelette', 'Rice-Curry-Chicken Roast', 'Speghetti', 'Speghetti-Curry', 'Black Pepper Chicken', 'Maggie']
i=0
dis_number = []
for i in range(0,10):
    dis_num = random.choice(dishes)
    dis_number.append(dis_num)
    my_dish = list(dict.fromkeys(dis_number))


print('The Timetable for week !')

mon = 'Monday: {}'
print(mon.format(my_dish[0]))

tue = 'Tuesday: {}'
print(tue.format(my_dish[1]))

wed = 'Wednesday: {}'
print(wed.format(my_dish[2]))

thu = 'Thursday: {}'
print(thu.format(my_dish[3]))

fri = 'Friday: {}'
print(fri.format(my_dish[4]))

sat = 'Saturday: {}'
print(sat.format(my_dish[5]))

sun = 'Sunday: {}'
print(sun.format(my_dish[1]))
