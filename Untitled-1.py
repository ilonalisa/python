n = int(input("Введіть кількість елементів у масиві:"))
array = []

for i in range(n):
    element = int(input("Введіть{24}-й елемент:".format(i+1)))
    array.append(element)

max_element = max(array)
reversed_array = array[::-1]

print("Максимальний елемент:",max_element)
print("Масив у зворотньому порядку:", reversed_array)