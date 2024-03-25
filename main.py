

import pyautogui
import pytesseract
import webbrowser
import time
import re
import winsound


# Set the path to the Tesseract executable (change this according to your installation)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

# Function to capture the screen and search for a specific word and sentence
# Function to capture the screen and search for a specific word and sentence
def search_word_and_get_data(word, phrase, score_phrase):

    Accept_check=""
    username=""
    score=""

    # Capture the entire screen
    screenshot = pyautogui.screenshot()

    # Use Tesseract OCR to extract text from the screenshot
    extracted_text = pytesseract.image_to_string(screenshot)

    # Check if the word exists in the extracted text
    if word.lower() in extracted_text.lower():
        #print(f"The word '{word}' is found on the screen.")
        Accept_check="Accepted";
    else:
        Accept_check="Not Accepted"
        #print(f"The word '{word}' is not found on the screen.")

    # Find and get the sentence after the specified phrase
    match = re.search(f"{re.escape(phrase)}(.*?)(\\. |\\n|$)", extracted_text, re.IGNORECASE)

    if match:
        sentence_after_phrase = match.group(1).strip()
        #print(f"The sentence after '{phrase}' is: {sentence_after_phrase}")
        username= sentence_after_phrase
    else:
        #print(f"No sentence found after the phrase '{phrase}' on the screen.")
        username="N/A"

    # Find and get the number after the specified score phrase
    match_score = re.search(f"{re.escape(score_phrase)}\\s*(\\d+\\.?\\d*)", extracted_text, re.IGNORECASE)

    if match_score:
        score_value = match_score.group(1)
        #print(f"The number after '{score_phrase}' is: {score_value}")
        score = score_value
    else:
        #print(f"No number found after the phrase '{score_phrase}' on the screen.")
        score="N/A"

    with open('scores.txt', 'a') as file:
        file.write(f'{score}\n')

    with open('accept.txt', 'a') as file:
        file.write(f'{Accept_check}\n')

    with open('usernames.txt', 'a') as file:
        file.write(f'{username}\n')


def open_in_chrome(url):
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'  # Change the path based on your system
    webbrowser.get(chrome_path).open(url)
    time.sleep(3)  # Wait for the page to load


# Main function
def main(url):
    #url = 'https://www.hackerrank.com/contests/circuit-analyzer/challenges/circuit-analyzer-task-1/submissions/code/1375750570'
    open_in_chrome(url)

    # Word to search for
    word_to_search = "Status: Accepted"

    # Phrase to search for
    phrase_to_search = "belongs to"

    # Score phrase to search for
    score_phrase_to_search = "Scare: "

    # Search for the word, sentence after the phrase, and number after the score phrase on the screen
    search_word_and_get_data(word_to_search, phrase_to_search, score_phrase_to_search)

# Execute the main function
if __name__ == "__main__":


    with open('usernames.txt', 'w') as file:
        file.write(f'')
    with open('scores.txt', 'w') as file:
        file.write(f'')
    with open('accept.txt', 'w') as file:
        file.write(f'')



    # Open the text file
    with open('source.txt', 'r') as file:
        # Read all lines and store them in a list
        lines = file.readlines()

    for line in lines:
        main(line)
        time.sleep(2)
        print("/////////////////////////////////////////////////////////")

    duration = 1000  # milliseconds
    freq = 440  # Hz
    winsound.Beep(freq, duration)


"""
import pyautogui
import pytesseract
import webbrowser
import time

# Set the path to the Tesseract executable (change this according to your installation)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

# Function to capture the screen and search for a specific word
def search_word_on_screen(word):
    # Capture the entire screen
    screenshot = pyautogui.screenshot()

    # Use Tesseract OCR to extract text from the screenshot
    extracted_text = pytesseract.image_to_string(screenshot)

    # Check if the word exists in the extracted text
    if word.lower() in extracted_text.lower():
        print(f"The word '{word}' is found on the screen.")
    else:
        print(f"The word '{word}' is not found on the screen.")



def open_in_chrome(url):
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'  # Change the path based on your system
    webbrowser.get(chrome_path).open(url)
    time.sleep(5)  # Wait for the page to load


# Main function
def main(url):
    #url = url
    open_in_chrome(url)

    # Word to search for
    word_to_search = "accepted"

    # Search for the word on the screen
    search_word_on_screen(word_to_search)

# Execute the main function
if __name__ == "__main__":
    # Open the text file
    with open('source.txt', 'r') as file:
        # Read all lines and store them in a list
        lines = file.readlines()

    for line in lines:
        main(line)
        time.sleep(3)

"""