# from datetime import datetime

# data_log = datetime.now()


def input_name():
    return input('Введите заголовок заметки: ').title()


def input_address():
    return input('Введите тело заметки: ').title()


def create_zamet():

    name = input_name()
    address = input_address()
    # return f'{name}{address}\n\n'
    return f'*** Заголовок заметки:\n{name} \n*** Тело заметки:\n[{address}]\n\n'
  

def add_contact():
    contact_str = create_zamet()
    with open("notes.csv", 'a', encoding='utf-8') as file:
        # file.write(str(data_log) + '\n')                         
        file.write(contact_str + '\n')
           
def print_contacts():
    with open("notes.csv", 'r', encoding='utf-8') as file:
        contacts_str = file.read()
    contacts_list = contacts_str.rstrip().split('\n\n')
    for contact in contacts_list:
        print(contact)
 
# 
def copy():
    
    with open("notes.csv", 'r', encoding='utf-8') as file:
        contacts_str = file.read()
        a_list = contacts_str.split('\n\n')
        a = 0
        for i in a_list:
            a +=1
            if a < len(a_list):
                print("Номер заметки : ", a)
            print(i)
        de = int(input('Введите номер заметки для редактирования: '))

        a_list[de-1] = create_zamet()
        with open("notes.csv", 'w', encoding='utf-8') as file:
            for ar in a_list:
                
                file.writelines(ar)
                file.writelines('\n\n')
            
        print('Заметка успешно отредактирована.')

def dell():
    
    with open("notes.csv", 'r', encoding='utf-8') as file:
        contacts_str = file.read()
        a_list = contacts_str.split('\n\n')
        a = 0
        for i in a_list:
            a +=1
            if a < len(a_list):
                print("Номер заметки : ", a)
            print(i)
        de = int(input('Введите номер заметки для удоления: '))

        del a_list[de-1]
        with open("notes.csv", 'w', encoding='utf-8') as file:
            for ar in a_list:
                file.writelines(ar)
                file.writelines('\n\n')
            
        print('Заметка успешно удалена.')
                

def interface():
    with open("notes.csv", 'a', encoding='utf-8'):
        pass

    var = 0
    while var != '5':
        print(
            'Возможные варианты:\n'
            '1. Добавить заметку:\n'
            '2. Вывести на экран все заметки:\n'
            '3. Редактирования заметку:\n'
            '4. Удаление заметки:\n'
            '5. Выход'
            )
        print()
        var = input('выберите вариант действия: ')
        while var not in ('1', '2', '3', '4','5'):
            print('некорректный ввод!')
            var = input('выберите вариант действия: ')
        print()    

        match var: 
            case '1':
                add_contact()
            case '2':
                print_contacts()
            case '3':
                copy()
            case '4':
                dell()
            case '5': 
                print('До свидания')  
        print()        

if __name__ == '__main__':
    interface()

