while True:
    try:
        filename = input('Enter the name of the text file you want to open: ')

        with open(filename, 'r') as file:
            content = file.read()
            print('\nFile content:\n', content)

        choice = input('\nDo you want to write to the same file or a new file? Answer "same" or "new": ')
        if choice.lower() == 'same':
            write_filename = filename
        elif choice.lower() == 'new':
            write_filename = input('Enter the name of the new file: ')
        else:
            print('Invalid choice. Exiting.')
            break

        data_to_write = input('Enter the content you want to write: ')

        try:
            with open(write_filename, 'w') as file:
                file.write(data_to_write)
        except FileNotFoundError:  # I guess this in not needed, because we open the file in write mode
            print('ERROR: The file was not found.')
            continue
        except Exception as e:
            print(f'An error occurred while opening the file: {e}')
            continue
        else:
            print('\nWriting was successful!')
        finally:
            print('Closing the program.')
            break

    except FileNotFoundError:
        print('ERROR: The file was not found. Please provide a valid filename.')
    except ValueError:
        print('ERROR: Invalid input. Please provide a valid filename.')
