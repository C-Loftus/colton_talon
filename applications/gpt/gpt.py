import requests
import json, os
from typing import Optional
from talon import Module, actions, clip, app

# TODO: Make it only available to run one request at a time

mod = Module() 
# Stores all our prompts that don't require arguments 
# (ie those that just take in the clipboard text)
mod.list("promptNoArgument", desc="GPT Prompts Without Arguments")

# Necessary for those who don't have custom notifications installed
def notify(message: str):
    try:
        actions.user.notify(message)
    except:
        app.notify(message)

def gpt_query(prompt: str, content: str) -> str:
    try:
        TOKEN = os.environ["OPENAI_API_KEY"]
    except:
        notify("GPT Failure: No API Key")   

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {TOKEN}'
    }

    data = {
        'messages': [{'role': 'user', 'content': f"{prompt}:\n{content}"}],
        'max_tokens': 2024,
        'temperature': 0.6,
        'n': 1,
        'stop': None,
        'model': 'gpt-3.5-turbo'
    }

    notify("GPT Task Started")

    response = requests.post(
        'https://api.openai.com/v1/chat/completions',
        headers=headers, data=json.dumps(data))

    if response.status_code == 200:

        notify("GPT Task Completed")

        return response.json()['choices'][0]['message']['content'].strip()
    else:
        # Necessary for those who don't have custom notifications installed
        notify("GPT Failure: Check API Key or Prompt")

        print(response.json())

        return ""

def gpt_task(prompt: str, content: str) -> str:
    """Run a GPT task"""

    resp = gpt_query(prompt, content)

    if resp:
        clip.set_text(resp)

    return resp

@mod.action_class
class UserActions:

    def gpt_prompt_no_argument(prompt: str) -> str:
        """Run a GPT task"""

        content = actions.edit.selected_text()

        return gpt_task(prompt, content)

    def gpt_fix_delimited(contentToFix: str, delimiter: str ="_"):
        """ 
        Take a list of words/phrases return them  with the proper formatting and any typos fixed in a delimited string
        """

        prompt = f"""I will give you a list of words or phrases that are survey responses. Fix these responses so they have the proper formatting and expand any abbreviations to the phrase that would make sense contextually. Return them all as a list with a '{delimiter}' separating each item. If similar words show up multiple times, they should be formatted the same way as other occurrences. So for instance, "face book" and "FB" should both be returned as "Facebook" or if the list is a list of pharmaceutical companies, "astra" should become "AstraZeneca".

        """

        result = gpt_task(prompt, contentToFix)
        print(f'{type(result)=}{result=}')
        assert type(result) != None
        return result

    def gpt_answer_question(inputText: str):
        """answer question"""
        prompt = """
        Using a professional tone, generate text that satisfies the question or request given in the prompt. 
        """

        return gpt_task(prompt, inputText)


    def gpt_arbitrary_prompt(prompt: str) -> str:
        """Run a GPT task"""

        content = actions.edit.selected_text()

        return gpt_task(prompt, content)        

