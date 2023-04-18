
from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

############ function encode ###################
################################################


# def encode(text, shift):
#     encode_text = ""
#     for character in text:
#         try:
#             encode_text += alphabet[alphabet.index(character) + shift]
#         except:
#             of_shift = shift - (len(alphabet) - alphabet.index(character))
#             encode_text += alphabet[of_shift]

#     print("The encoded text is: ", encode_text)


############ function decode ###################
################################################


# def decode(text, shift):
#     decode_text = ""
#     for character in text:
#         decode_text += alphabet[alphabet.index(character) - shift]

#     print("The decoded text is: ", decode_text)


################################################
################################################

# if direction == "encode":
#     encode(text, shift)
# else:
#     decode(text, shift)

############ caesar ############################
################################################

def caesar(text, shift, direction):
    c_text = ""
    if shift > 26:
        shift = shift % 26
    if direction == "decode":
        shift *= -1
    for character in text:
        if character in alphabet:
            c_text += alphabet[alphabet.index(character) + shift]
        else:
            c_text += character

    print(f"The {direction}d text is: ", c_text)
    finish()


def finish():
    answer = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if answer == "yes":
        ins()


def ins():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)


ins()
print("Goodbye!")
