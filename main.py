from arts import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().

def ceasar(start_text,shift_amount,cipher_direction):
  end_text=""
  if cipher_direction=="decode":
      shift_amount*=-1
  for letter in start_text:
    if letter in alphabet:
      position=alphabet.index(letter)
      new_position=position+shift_amount
      if new_position>25:
        cust_position=new_position%26
        end_text=alphabet[cust_position]
      else:
        end_text+=alphabet[new_position]
    else:
      end_text+=letter
  print(f"The {cipher_direction}d text is {end_text}")

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
should_continue=True
while(should_continue):
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift=shift%25
  ceasar(start_text=text, shift_amount=shift, cipher_direction=direction)
  choice = input("Type 'yes' if you want to go again. Otherwise type 'no' ").lower()
  if choice == "no":
    should_continue = False
    print("Good bye")


