toprow = ["q","w","e","r","t","y","u","i","o","p"] #the first line of the keyboard, listed 1 to 9 in string
middlerow = ["a","s","d","f","g","h","j","k","l"]#the second line of the keyboard, listed 10 to 18 in string
bottomrow = ["z","x","c","v","b","n","m",",","."]#the third line of the keyboard, listed 19 to 25 in string

def move_letter_e(letter_position, displacement, array):
    #find total letter displacement
    total_displacement = int(letter_position) + int(displacement)
    #confirm the total displacement is in bounds
    if total_displacement  > len(array)-1:
        #if out of bounds change displacement value
        total_displacement = total_displacement - len(array)
    #find index of new letter at displacement
    shifted = array[total_displacement]
    return shifted

def move_letter_d(letter_position, displacement, array):
    #find total letter displacement
    total_displacement = int(letter_position) - int(displacement)
    #confirm the total displacement is in bounds
    if total_displacement < 0:
        #if out of bounds change displacement value
        total_displacement = total_displacement + len(array)
    #find index of new letter at displacement
    shifted = array[total_displacement]
    return shifted

def encrypt(text, encryptKey):
    output = ""
    encryptKey = str(encryptKey)
    if len(encryptKey) != 3:
            encryptKey += encryptKey[0]
            encryptKey += encryptKey[0]

    toprow_off = encryptKey[0]
    middlerow_off = encryptKey[1]
    bottomrow_off = encryptKey[2]

    for character in text:
        if character == " ":
            output += " "
            continue
        if character.islower() or character == "," or character == ".":
            is_lower = True
        else:
            is_lower = False
            character = str.lower(character)
        if character in toprow:
            index = toprow.index(character)
            shifted = move_letter_e(index, toprow_off, toprow)
        elif character in middlerow:
            index = middlerow.index(character)
            shifted = move_letter_e(index, middlerow_off, middlerow)
        elif character in bottomrow:
            index = bottomrow.index(character)
            shifted = move_letter_e(index, bottomrow_off, bottomrow)
        else:
            shifted = character

        if not is_lower:
            #change as necessary lowercase/uppercase letters
            if shifted == ",":
                shifted = "<"
            if shifted == ".":
                shifted = ">"
            else:
                shifted = str.upper(shifted)
        output +=(shifted)
    return output

def decrypt(text, encryptKey):
    output = ""
    encryptKey = str(encryptKey)
    if len(encryptKey) != 3:
            encryptKey += encryptKey[0]
            encryptKey += encryptKey[0]


    toprow_off = encryptKey[0]
    middlerow_off = encryptKey[1]
    bottomrow_off = encryptKey[2]

    for character in text:
        if character.islower() or character == "," or character == ".":
            is_lower = True
        elif character == " ":
            output += " "
            continue
        else:
            is_lower = False
            character = str.lower(character)

        if character in toprow:
            index = toprow.index(character)
            shifted = move_letter_d(index, toprow_off, toprow)
        elif character in middlerow:
            index = middlerow.index(character)
            shifted = move_letter_d(index, middlerow_off, middlerow)
        elif character in bottomrow:
            index = bottomrow.index(character)
            shifted = move_letter_d(index, bottomrow_off, bottomrow)

        if not is_lower:
            #change as necessary lowercase/uppercase letters
            if shifted == ",":
                shifted = "<"
            elif shifted == ".":
                shifted = ">"
            else:
                shifted = str.upper(shifted)
        output +=(shifted)
    return output
