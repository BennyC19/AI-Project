#steps for this to work:
# 1. start recording when audio peaks and after the sound is gone for a certain period of time.
# 2. transcribe the audio into text.
# 3. put the text into the ai model.
# 4. if 'hello robot' is detected, eliminate all text before the words 'hello robot'.
# 5. if 'hello robot' is not detected then output something saying that it did not detect anything.
# 5. detect if the text is trying to find a certain object or if it is trying to describe a new object to remember.
# 6. if it is trying to describe an object, output something that can signal other parts of the program to start up.

import openai
import speech_recognition as sr

class language_model:
    def __init__(self, secret_key):

        self.secret_key = secret_key

        self.pre_prompt_1 = ("Here are instructions I want you to follow for the next prompt.\n"+
                             "1. Try and detect the words 'hello robot', it may be slightly misspeled.\n"+
                             "2. If 'hello robot' is not present then output ")

        self.pre_prompt_2 = ("Here are instructions I want you to follow for the next prompt.\n"+
                             "1. Ignore all text before the words 'hello robot'. If the words 'hello robot' seem slightly misspeled then it is valid.\n" +
                             "2. Ignore any text that seems redundant.\n"+
                             "3. The words after 'hello robot' should be descibing characteristics of an object. Create a list that divided by commas.\n"+
                             "4. If you detect that more then one object is being described, only create a list from the first object mentioned.\n"+
                             "5. Include no other text\n"+
                             "6. Do not include 'hello robot'\n"+
                             "Example: 'heya uh what is the blue and long pole that is in Canada with uh heluh helllo robot. I have a bottle of water with a blue ribbon and a red cap on top.' turns into 'bottle of water, blue ribbon, red cap on top'")
    
    def run_model_text(self, pre_prompt, prompt):
        openai.api_key = self.secret_key
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                    {"role":"system", "content": f"{pre_prompt}"},
                    {"role":"user", "content": f"{prompt}"}
                ]
        )
        return response

    def transcribe(self, audio_data):

        recongnizer = sr.Recognizer()

        audio = sr.AudioData(audio_data, sample_rate=44100, sample_width=2)

        try:
            text = recongnizer.recognize_google(audio)
            return text 
        except sr.UnknownValueError:
            print("Could not understand the audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

    def extract_text(self, input):
        return input["choices"][0]["message"]["content"]

