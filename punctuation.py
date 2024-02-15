print(r'''                               __                      __                  
                              /\ \__                  /\ \__  __           
 _____   __  __    ___     ___\ \ ,_\  __  __     __  \ \ ,_\/\_\    ___     ___        _____   __  __
/\ '__`\/\ \/\ \ /' _ `\  /'___\ \ \/ /\ \/\ \  /'__`\ \ \ \/\/\ \  / __`\ /' _ `\     /\ '__`\/\ \/\ \
\ \ \L\ \ \ \_\ \/\ \/\ \/\ \__/\ \ \_\ \ \_\ \/\ \L\.\_\ \ \_\ \ \/\ \L\ \/\ \/\ \  __\ \ \L\ \ \ \_\ \
 \ \ ,__/\ \____/\ \_\ \_\ \____\\ \__\\ \____/\ \__/.\_\\ \__\\ \_\ \____/\ \_\ \_\/\_\\ \ ,__/\/`____ \
  \ \ \/  \/___/  \/_/\/_/\/____/ \/__/ \/___/  \/__/\/_/ \/__/ \/_/\/___/  \/_/\/_/\/_/ \ \ \/  `/___/> \
   \ \_\                                                                                  \ \_\     /\___/
    \/_/                                                                                    \/_/     \/__/''')

import string

def extract_punctuation(input_file, output_file):
    with open(input_file, 'r') as file:
        text = file.read()

    punctuation = set(string.punctuation)
    punctuation_in_text = ''.join(char for char in text if char in punctuation)

    with open(output_file, 'w') as file:
        file.write(punctuation_in_text)

if __name__ == "__main__":
    input_file = ("/path/to/input/file.txt")
    output_file = ("/path/to/output/file.txt")
    extract_punctuation(input_file, output_file)
    print("Punctuation extracted successfully!")