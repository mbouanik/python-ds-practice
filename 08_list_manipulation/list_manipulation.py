def list_manipulation(lst, command, location, value=None):
    if command == 'add':
        if location == 'beginning':
            lst.insert(0,value)
        else:
            lst.append(value)
    elif command == 'remove':
        if location == 'beginning':
            lst.pop(0)
        else:
            lst.pop(-1)
    else:
        return None

