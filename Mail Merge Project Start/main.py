PLACEHOLDER = '[name]'
list = []

with open("./Mail Merge Project Start/Input/Names/invited_names.txt") as invited_names:
    names = invited_names.readlines() # ['Aang\n', 'Zuko\n', 'Appa\n', 'Katara\n', 'Sokka\n', 'Momo\n', 'Uncle Iroh\n', 'Toph']
    for name in names:
        list.append(name.replace('\n', ''))
    # now list contains ['Aang', 'Zuko', 'Appa', 'Katara', 'Sokka', 'Momo', 'Uncle Iroh', 'Toph']

with open("./Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter:
    contents = letter.read()
    for name in list:
        new_letter = contents.replace(PLACEHOLDER, name)

        # with open can also CREATE a new file because it does not already exist
        with open(f'./Mail Merge Project Start/Output/ReadyToSend/letter_for_{name}.txt', mode='w') as completed_letter:
            # but the newly created file is blank. so we have to write something
            completed_letter.write(new_letter)