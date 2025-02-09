# Function declarations 

# Print menu 
def print_menu():
    print('\n Done IT: ')
    print('1. View Tasks')
    print('2. Add a Task')
    print('3. Remove a Task')
    print('4. Exit')
    
    
#  get the choice of the user
def get_choice():
    while True:
        choice = input('Enter your Choice here: ')
        valid_choices = ('1', '2', '3', '4')
        if choice not in valid_choices:
            print('Invalid Choice')
            continue
        else:
            return choice
        
# show task from task list
def display_tasks(tasks):
    if not tasks:
        print('No tasks in the list')
        return 
    
    for index, task in enumerate(tasks, start=1):
        print(f'{index}. {task}')
    
    
# Function to add task
def add_task(tasks):
    while True:
        task = input('Kindly enter new task: ').strip()
        if len(task) != 0:
            tasks.append(task)
            break
        else:
            print('Invalid task!')

# Delete the task
def remove_task(tasks):
    display_tasks(tasks)
    
    while True:
        try:
            task_number = int(input('Enter the task number: '))
            if 1 <= task_number <= len(tasks):
                tasks.pop(task_number - 1)
                break
            else:
                raise ValueError
        except ValueError:
            print('Invalid task number entered')
            
            
#  Main function
def main():
    tasks = []
    
    while True:
        print_menu()
        
        choice = get_choice()
        
        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        else:   
            break
        

if __name__ == '__main__':
    main()