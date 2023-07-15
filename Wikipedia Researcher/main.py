import wikipedia
import os
import sumy
import pyttsx3

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer


#Variable that loops if the user wants to play again

#Create a function to replay the code easily
def ResearchTopic():

    #initializes the speaker
    converter = pyttsx3.init()
#lets set up the speaker
    speaker_rate = 190
    converter.setProperty('rate', speaker_rate)
    converter.setProperty('volume', 0.6)
    #This is the file path for one of the speakers
    voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
    converter.setProperty('voice', voice_id)

    #take user input to see what to research
    user_topic = input("\n\n What is it you want me to research?")
    converter.runAndWait()
    #Format the output
    print("_" * 50)
    print("\n\n Okay, researching " + user_topic + ", here we go!")
    converter.say("Okay, researching " + user_topic + ", here we go!")
    converter.runAndWait()
    print("_" * 50)
    print("\n\n")
    #API call
    wiki_page = wikipedia.page(user_topic)
    #Format the output
    print("\n\n" + wiki_page.title + "\n")
    print("_" * 50)
    print("\n\n" + wiki_page.summary + "\n")
    print("_" * 50)

# Create logic for saving research


    #Write to the text file to save the research
    Research = open( 'SavedResearch.txt', 'a')
    #Research.write(wiki_page.title + "\n \n" + wiki_page.summary + "\n\n")
    Research.write(wiki_page.title +"\n" + wiki_page.summary+ "\n\n")

    #Always close the text file!
    Research.close()

def SummarizeTopic():
    #initializes the speaker
    converter = pyttsx3.init()
#lets set up the speaker
    speaker_rate = 160
    converter.setProperty('rate', speaker_rate)
    converter.setProperty('volume', 0.6)
    #This is the file path for one of the speakers
    voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    converter.setProperty('voice', voice_id)
    converter.say("Okay thanks David I can take it from here. I am better with words than you are after all!")
    converter.runAndWait()
    converter.say("Okay lets summarize what we have!")
    converter.runAndWait()
    print("\n Okay! Lets summarize what we have!")
    #Open file
    Research = open( 'SavedResearch.txt', 'r')
    data = Research.read()
    Research.close()
    print(data)

    parser = PlaintextParser.from_string(data, Tokenizer("english"))

    summarizer = LexRankSummarizer()
    NumOfSentence = 6
    summary = summarizer (parser.document, NumOfSentence)
    print("Here is your summary!")
    for sentence in summary:
        print(sentence)
        converter.say(sentence)
        converter.runAndWait()
    return summary

def main():

    #initializes the speaker
    converter = pyttsx3.init()
#lets set up the speaker
    speaker_rate = 160
    converter.setProperty('rate', speaker_rate)
    converter.setProperty('volume', 0.6)
    #This is the file path for one of the speakers
    voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
    converter.setProperty('voice', voice_id)


        #Intro sequence
    print("\n\n Welcome to The Study Bot! I can help you research many different topics.\n")
    print("\n Lets take a look at a few relevant topics and summarize them to save you some time!\n")
    print("\n Kindly enter three seperate topics to research one at a time. If you want to use the result save when prompted to!\n")
    converter.say("Hi I am The Study Bot kindly read the instructions and let me know when you are ready.")
    converter.runAndWait()
        #Use a while loop to allow the user to research again
    loop = True
    while loop == True:
        #Function call
        ResearchTopic()
    #Create a variable for yes and no answer
        print("\n Select Y to add another topic or N to summarize current topic(s).\n")
        converter.say("Anything else?")
        converter.runAndWait()
        YorN = input("Want to add another topic? Y or N\n\n")
        

    #Play again logic
        if (YorN == "Y" or YorN == "y"):
            converter.say("Well lets keep going then!")
            converter.runAndWait()
            print("Well lets keep going then!\n\n")
        elif (YorN == "N" or YorN == "n"):
            SummarizeTopic()
            os.remove('SavedResearch.txt')
            loop = False
    
if __name__ == "__main__":
    main()