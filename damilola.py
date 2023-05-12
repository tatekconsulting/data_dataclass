from datetime import datetime

#1. Python script to select date from the file_name

def getpart():
    file_name = "colossus_input_data_energy_20230326.csv"

    dd = file_name.split("_")[-1].split(".")[0]
    print(dd)
##################
    datetime_obj = datetime.strptime(dd,'%Y%m%d').strftime('%Y-%m-%d')
    return datetime_obj
IUHIHPIP[JMPHPIJN]

#2a Python script to create a list and print out all elements in the list
fruit_list = "Mango_banana_orange_pineapple_carrot_cucumba_pears_breadfruit_kiwi_cherry_apple"

amended_list = fruit_list.split("_")
print(amended_list)

print(type(amended_list))

#2b. Create a new list name my_new_fruit and add all fruits to list
my_new_fruit =[]
for i in amended_list:
    my_new_fruit.append(i)
print(my_new_fruit)

#2c  Use list_cmprehension to create my_new_fruit_list. using comp_fruit as a name in place of my_new_fruit_list to avoid duplaicate name.
comp_fruit = [i for i in amended_list]
print(comp_fruit)


3#a Create a list without duplicates
fruit_new = "Mango_banana_orange_pineapple_carrot_cucumba_banana_pear_breadfruit_kiwi_cherry_apple_pineapple"
amended_fruit_new = fruit_new.split("_")
new_set = set(amended_fruit_new)
new_list = list(new_set)
print(new_list)

print(type(new_list))

#3b.
two_fruit= []
for i in new_list:
    if i  == "apple" or i == "banana":
        two_fruit.append(i)
print(two_fruit)

#3b Use list comprehension to select only apple and banana

two_fruit_list = [i for i in new_list if i =="apple" or i == "banana"]

print(two_fruit_list)





