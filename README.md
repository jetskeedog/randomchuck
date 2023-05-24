# RandomChucK

RandomChuck is a simple python script that creates random "songs" from a text prompt using the ChucK programming language. 

## Prerequisites
There is an optional script(ChatGPT.py) that uses the OpenAI API key. If you don't have one, sign up on the OpenAI website and obtain your API key.

## Requirements
* Python 3.x
* nltk library (Python)
* ChucK
* Optional OpenAI API

## Installation

### Python and nltk library
Python 3.x is required to run this program. To check your Python version, use python --version or python3 --version.

Install nltk library using pip:

```bash
pip install nltk
```

## Optional OpenAI API

```
ChatGPT.py

# Replace with your OpenAI API key
openai.api_key = ""
```

### ChucK
To install ChucK, please follow the instructions on the official ChucK website:
http://chuck.cs.princeton.edu/doc/build/
## Usage
Run the script by executing the following command:
```
python3 script.py
```

Or if you are using OpenAI API
```
python3 ChatGPT.py
```
The program will prompt you to enter a sentence. This input currently doesn't affect the output, but can be customized for future implementations.

After you enter a sentence, the program will generate a ChucK script that creates a 10-second random melody using a randomly selected unit generator (either SinOsc, SawOsc, or SqrOsc) from ChucK.

The script will be saved as a '.ck' file with a name based on the current timestamp (YearMonthDayHourMinuteSecond).

After the script is saved, the program will execute the ChucK script and play the generated melody.

You can run the program again for a new melody. Each run will create a new '.ck' file with a unique timestamp.


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
