#Программа для работы с задачами.

#Фунция для отображения списка задач.
def display_tasks(tasks):
    if not tasks:
        print("Список задач пуст!")
    else:
        print("Вот список задач:")
        #Перебираем все задачи в цикле, попутно добавляя им индекс.
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")


#main функция, вызывается при запуске скрипта.
def main():
    tasks = [] #Список задач.

    while True:
        print("\nВыберите действие.\n1. Добавить задачу.\n2.Удалить задачу.\n3. Показать задачи.\n4. Очистить список задач\n5. Выйти из программы.")

        choice = input("Введите номер действия:\n")

        if choice == '1':
            #Добавление новой задачи.
            task = input("Введите задачу:\n")
            tasks.append(task) #Добавляем задачу в конец списка.
            print(f"Задача {task} добавлена!")
        elif choice == '2':
            #Удаление задачи.
            display_tasks(tasks) #Вызываем функцию работы с задачами, передавая в неё список задач.
            #Показываем текущие задачи.
            if tasks:
                task_index = int(input("Введите номер задачи для удаления:\n")) - 1
                #Проверяем, что индекс корректен.
                if 0 <= task_index < len(tasks):
                    #Удаляем задачу по указанному индексу.
                    removed_task = tasks.pop(task_index)
                    print(f"Задача {removed_task} удалена!")
        elif choice == '3':
            #Вызываем функцию, которая покажет список задач на экране.
            display_tasks(tasks)
        elif choice == '4':
            #Очищаем список задач.
            tasks.clear()
            print("Все задачи успешно удалены!")
        elif choice == '5':
            print("Покидаем программу.")
            break #break используется для досрочной остановки программы, он доступен только внутри цикла.
        else:
            print("Похоже, вы выбрали что-то не то. Попробуйте снова.")


if __name__ == "__main__":
    main() #Вызываем функцию main.