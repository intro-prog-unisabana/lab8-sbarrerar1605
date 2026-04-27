import sys
from todo_manager import read_todo_file, write_todo_file

def main():
    try:
        if len(sys.argv) < 2:
            raise IndexError("Insufficient arguments provided!")

        if sys.argv[1] == "--help":
            print("""Usage: python main.py <file_path> <command> [arguments]...

Commands:
  add "task"    - Add a task to the list.
  remove "task" - Remove a task from the list.
  view          - Display all tasks.

Examples:
  python main.py tasks.txt add "Buy groceries"
  python main.py tasks.txt remove "Do laundry"
  python main.py tasks.txt view
  python main.py tasks.txt add "Call mom" remove "Take out trash" view""")
            return

        file_path = sys.argv[1]
        tasks = read_todo_file(file_path)

        i = 2
        modified = False
        final_error = False

        while i < len(sys.argv):
            cmd = sys.argv[i]

            if cmd == "view":
                print("Tasks:")
                for t in tasks:
                    print(t)
                i += 1

            elif cmd == "add":
                if i + 1 >= len(sys.argv):
                    raise IndexError('Task description required for "add".')

                task = sys.argv[i + 1]
                tasks.append(task)
                print(f'Task "{task}" added.')
                modified = True
                i += 2

            elif cmd == "remove":
                if i + 1 >= len(sys.argv):
                    raise IndexError('Task description required for "remove".')

                task = sys.argv[i + 1]

                try:
                    tasks.remove(task)
                    print(f'Task "{task}" removed.')
                    modified = True
                except ValueError:
                    print(f'Task "{task}" not found.')

                i += 2

            else:
                print("Command not found!")
                final_error = True
                break

        # SOLO guardar si no hubo error de comando desconocido
        if not final_error:
            write_todo_file(file_path, tasks)

    except IndexError as e:
        print(e)

    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()