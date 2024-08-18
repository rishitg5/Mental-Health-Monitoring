from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def read_words_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read the entire contents of the file as a string
            file_content = file.read()
            # Split the content into words
            words = file_content.split()
            return words
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)

# Replace 'your_file.txt' with the path to your text file
file_path = './audio.txt'

# Call the function to read words from the file into a list
word_list = read_words_from_file(file_path)

# print("List of words:", word_list)

try:
    # print('Printing the message..')
    # text = r.recognize_google(recorded_audio, language='en-US')
    # print('Your message: {}'.format(text))

    # Sentiment analysis
    Sentence = [str(word_list)]
    analyser = SentimentIntensityAnalyzer()
    for i in Sentence:
        v = analyser.polarity_scores(i)
        print(v)

except Exception as ex:
    print("An error occured:", ex)
