import re

def user_welcome():
    """
    this function contains a 
    display message for the user to describe the game.
    """
    print("""
***********************************************************************************************
**                         Welcome to this program of Madlibs!                               **
**                                                                                           **   
**       Madlibs shortly is combining words and synonyms together from the user              **   
**  to create a short story line, enter your words and let's see how it will result!         **
***********************************************************************************************   
    """)


def read_template(file_path):
    '''
    reading the file from the path 
    and raising an error if it won't open
    '''
    try:
        # open to read the file
        opened_file = open(file_path, "r")
        # actually reading the file 
        read_file = opened_file.read()

    except FileNotFoundError as e:
        raise e

    return read_file


def parse_template(read_file):
    '''
    selecting words between curly brackets 
    from the text file and replace it with other inputs
    '''

    reg_ex = r"{.[^}]*}"

    changeable_words = re.findall(reg_ex, read_file)

    return changeable_words, reg_ex



def merge(bare_template, changeable_words, reg_ex, read_file):
    '''
    storing the new inputs 
    and the changed words between brackets into a list
    '''

    # list to store user's input
    user_words = []

    for word in changeable_words:
        user_input = input(f"please enter a word as {word} ")
        user_words.append(user_input)

    

    new_text = re.sub(reg_ex, user_words[0], read_file, count=1)

    for index in range(1, len(user_words)):
        new_text = re.sub(reg_ex, user_words[index], new_text, count=1)

    # to write / as file
    with open(bare_template, 'w') as file:
        file.write(new_text)

    return user_words, new_text
    



user_welcome()

display_file = read_template(file_path="assets/video_game.txt")
print(f"original template:  {display_file}")


language_parts, reg_ex = parse_template(display_file)
print(f"language parts: {language_parts}")

inserted_words, new_template = merge(bare_template="new_madlips.txt", changeable_words=language_parts, read_file=display_file, reg_ex=reg_ex)
print(f"inserted words: {inserted_words}")
print(f"new template is : {new_template}")