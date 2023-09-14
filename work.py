import tkinter as tk
import os

# Путь к файлу work.txt
file_path = os.path.join(os.path.dirname(__file__), "work.txt")

# Список для хранения контактов
phone_book = []

# Индекс выбранного контакта для редактирования
selected_contact_index = None

# Функция для добавления контакта в справочник
def add_contact():
    last_name = last_name_entry.get()
    first_name = first_name_entry.get()
    phone_number = phone_number_entry.get()
    contact = {
        "Фамилия": last_name,
        "Имя": first_name,
        "Номер телефона": phone_number
    }
    phone_book.append(contact)
    update_contact_list()
    clear_entries()
    save_to_file()
    message_label.config(text="Контакт успешно добавлен!")

# Функция для загрузки контактов из файла
def load_from_file():
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split(', ')
                if len(parts) == 3:
                    last_name, first_name, phone_number = parts
                    contact = {
                        "Фамилия": last_name,
                        "Имя": first_name,
                        "Номер телефона": phone_number
                    }
                    phone_book.append(contact)
                    update_contact_list()

# Функция для сохранения контактов в файл
def save_to_file():
    with open(file_path, 'w', encoding='utf-8') as file:
        for contact in phone_book:
            file.write(f"{contact['Фамилия']}, {contact['Имя']}, {contact['Номер телефона']}\n")

# Функция для обновления списка контактов
def update_contact_list():
    contact_list.delete(0, tk.END)
    for contact in phone_book:
        contact_list.insert(tk.END, f"{contact['Фамилия']} {contact['Имя']} ({contact['Номер телефона']})")

# Функция для очистки полей ввода
def clear_entries():
    last_name_entry.delete(0, tk.END)
    first_name_entry.delete(0, tk.END)
    phone_number_entry.delete(0, tk.END)

# Функция для выбора контакта для редактирования
def select_contact(event):
    global selected_contact_index
    selected_contact_index = contact_list.curselection()[0]
    selected_contact = phone_book[selected_contact_index]
    last_name_entry.delete(0, tk.END)
    first_name_entry.delete(0, tk.END)
    phone_number_entry.delete(0, tk.END)
    last_name_entry.insert(0, selected_contact['Фамилия'])
    first_name_entry.insert(0, selected_contact['Имя'])
    phone_number_entry.insert(0, selected_contact['Номер телефона'])

# Функция для изменения контакта
def edit_contact():
    global selected_contact_index
    if selected_contact_index is not None:
        last_name = last_name_entry.get()
        first_name = first_name_entry.get()
        phone_number = phone_number_entry.get()
        contact = {
            "Фамилия": last_name,
            "Имя": first_name,
            "Номер телефона": phone_number
        }
        phone_book[selected_contact_index] = contact
        update_contact_list()
        clear_entries()
        save_to_file()
        message_label.config(text="Контакт успешно изменен!")
        selected_contact_index = None

# Функция для удаления контакта
def delete_contact():
    global selected_contact_index
    if selected_contact_index is not None:
        del phone_book[selected_contact_index]
        update_contact_list()
        clear_entries()
        save_to_file()
        message_label.config(text="Контакт успешно удален!")
        selected_contact_index = None

# Создание главного окна
root = tk.Tk()
root.title("Телефонный справочник")

# Создание виджетов
last_name_label = tk.Label(root, text="Фамилия:")
last_name_entry = tk.Entry(root)
first_name_label = tk.Label(root, text="Имя:")
first_name_entry = tk.Entry(root)
phone_number_label = tk.Label(root, text="Номер телефона:")
phone_number_entry = tk.Entry(root)
add_button = tk.Button(root, text="Добавить контакт", command=add_contact)
edit_button = tk.Button(root, text="Изменить контакт", command=edit_contact)
delete_button = tk.Button(root, text="Удалить контакт", command=delete_contact)
message_label = tk.Label(root, text="")
contact_list = tk.Listbox(root)

# Привязываем событие выбора элемента в списке к функции select_contact
contact_list.bind('<<ListboxSelect>>', select_contact)

# Загрузка контактов из файла при запуске приложения
load_from_file()
update_contact_list()

# Размещение виджетов на главном окне
last_name_label.grid(row=0, column=0)
last_name_entry.grid(row=0, column=1)
first_name_label.grid(row=1, column=0)
first_name_entry.grid(row=1, column=1)
phone_number_label.grid(row=2, column=0)
phone_number_entry.grid(row=2, column=1)
add_button.grid(row=3, column=0)
edit_button.grid(row=3, column=1)
delete_button.grid(row=3, column=2)
message_label.grid(row=4, column=0, columnspan=3)
contact_list.grid(row=5, column=0, columnspan=3)

# Главный цикл приложения
root.mainloop()