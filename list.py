#function display menu
def display_menu():
    print('Menu')
    print('1 add the name')
    print('2 change tne name')
    print('3 view all the name')
    print('4 delet the name')
    print('5 exit ')

#function to add name list

def add_name(name):
    new_name = input('enter the name')
    if new_name == True:
        name.append(new_name)

#function to change the list

def change_name(name):
    change_name = input('which name do you want to change?')
    if change_name in name:
        index = name.index(change_name)
        new_name = input('which name want to riplace')
        name[index]= new_name




