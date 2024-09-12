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

    name.append(new_name)

#function to change the list

def change_name(name):
    change_name = input('which name do you want to change?')
    if change_name in name:
        index = name.index(change_name)
        new_name = input('which name want to riplace')
        name[index]= new_name

#function to view name
def view_name(name):
    print("current the list name:")


    for i in name:
        print(i)

#function to change view all the name
def delet_name(name):
    delet_name = input('enter the delet name')
    if delet_name in name:
        name.remove(delet_name)

def manage():
    names = []
    while True:
        display_menu()
        choice = int(input('enter the option(1-5)'))

        if choice == 1:
            add_name(names)
        elif choice == 2:
            change_name(names)
        elif choice == 3:
            view_name(names)
        elif choice == 4:
            delet_name(names)

        elif choice == 5:
            break

manage()



