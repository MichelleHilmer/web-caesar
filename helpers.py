def alphabet_position(letter):
    alphabet_l = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_u = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    if letter in alphabet_l:
        return(alphabet_l.find(letter))
    else:
        if letter in alphabet_u:
            return(alphabet_u.find(letter))
def rotate_character(char, rot):
    alphabet_l = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_u = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_char = ''
    if char.isalpha() == False:
      return char
    else:
        if char in alphabet_l:
            num_char = (alphabet_position(char)+ rot) % 26
            new_char = alphabet_l[num_char]
           
        else:
           if char in alphabet_u:
                num_char = (alphabet_position(char)+ rot) % 26
                new_char = alphabet_u[num_char]
    return(new_char)