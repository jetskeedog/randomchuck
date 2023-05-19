import openai
import random
import subprocess
import datetime

# Requires OpenAI API key
openai.api_key =  ""

user_input = input("Enter a sentence: ")

response = openai.Completion.create(
  engine="text-davinci-002",
  prompt=user_input,
  temperature=0.5,
  max_tokens=100
)

generated_text = response.choices[0].text.strip()

# Convert the generated text to a random ChucK melody
notes = [random.randint(200, 900) for _ in range(10)]
durations = [random.randint(100, 1000) for _ in range(10)]

# Randomly chooses a UGen
ugen = random.choice(["SinOsc", "SawOsc", "SqrOsc"])

chuck_code = f"{ugen} s => dac;\n"
for note, duration in zip(notes, durations):
    chuck_code += f"{note} => s.freq;\n"
    chuck_code += f"{duration}::ms => now;\n"

# Saves files
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

filename = f"output_{timestamp}.ck"
with open(filename, "w") as f:
    f.write(chuck_code)

# Now you can run this python file and it will generate a random melody and play it using ChucK
subprocess.run(["chuck", filename])
