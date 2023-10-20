import openai
import speech_recognition as sr

class language_model:
    def __init__(self, secret_key):

        self.secret_key = secret_key

        self.pre_prompt_1 = ("Here are instructions I want you to follow for the next prompt.\n"+
                             "1. Try and detect if the text is trying to address 'robot' in any way\n"+
                             "2. If the text is trying to address the robot then output 'there is a robot'\n"+
                             "3. If the text is not trying to address the robot then output 'there is no robot'\n"+
                             "4. Do not output anything else.")

        self.pre_prompt_2 = ("Here are instructions I want you to follow for the next prompt.\n"+
                             "1. Rewrite the exact same text but only the text after the word robot\n"+
                             "2. Do not output anything else.")

        self.pre_prompt_3 = ("Here are instructions I want you to follow for the next prompt.\n"+
                             "1. Ignore any text that seems redundant.\n"+
                             "2. The text should be descibing characteristics of an object. Create a list that divided by commas.\n"+
                             "3. If you detect that more then one object is being described, only create a list from the first object mentioned.\n"+
                             "4. Include no other text\n"+
                             "Example: 'I have a bottle of water with a blue ribbon and a red cap on top.' turns into 'bottle of water, blue ribbon, red cap on top'")

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