from helpers import alphabet_position, rotate_character
def encrypt(text, rot):
    new_text = ''
    for char in text:
      new_text = new_text + rotate_character(char,rot)
    return new_text

def main():
    user_input = input('What message would you like to send?')
    user_input_rot = input('What rot would you like to set to the message?')

    print(encrypt(user_input,int(user_input_rot)))



if __name__ == "__main__":
    main()