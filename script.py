#needs nltk installed locally. Run the command 'pip install nltk'

import random
import subprocess
import string
import nltk
from datetime import datetime

nltk.download('words')

# Get the list of English words
from nltk.corpus import words
words_list = words.words()

while True:
    # Get user input
    user_input = input("Enter a sentence: ")

    # Convert the user input to a basic ChucK melody
    notes = [random.randint(200, 900) for _ in range(10)]
    durations = [random.randint(100, 1000) for _ in range(10)]

    # Randomly choose a UGen
    ugen = random.choice(["SinOsc", "SawOsc", "SqrOsc"])

    chuck_code = f"{ugen} s => dac;\n"
    for note, duration in zip(notes, durations):
        chuck_code += f"{note} => s.freq;\n"
        chuck_code += f"{duration}::ms => now;\n"

    # Use current timestamp as the filename
    filename = datetime.now().strftime('%Y%m%d%H%M%S') + ".ck"

    # Save the ChucK code to a file with the timestamp in the name
    with open(filename, "w") as f:
        f.write(chuck_code)

    # Play the new file
    subprocess.run(["chuck", filename])
