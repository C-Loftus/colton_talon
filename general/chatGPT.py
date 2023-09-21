import requests
import json, os
from typing import Optional
from talon import Module, actions, clip

# TODO: Make it only available to run one request at a time

mod = Module()
# mod.setting(
#     "open_ai_fixup_prompt",
#     type=str,
#     default="Fix any grammar, ponctuation, and typos.",
#     desc="Prompt to use when using GPT to fix misrecognitions.",
# )


def gpt_query(prompt: str, content: str) -> Optional[str]:
    try:
        TOKEN = os.environ["OPENAI_API_KEY"]
    except:
        print("OPENAI API Key not loaded")
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {TOKEN}'
    }

    data = {
        'messages': [{'role': 'system', 'content': f"{prompt}:\n{content}"}],
        'max_tokens': 2024,
        'temperature': 0.6,
        'n': 1,
        'stop': None,
        'model': 'gpt-3.5-turbo'
    }

    actions.user.notify("GPT Task Started")

    response = requests.post(
        'https://api.openai.com/v1/chat/completions',
        headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        actions.user.notify("GPT Task Done")
        return response.json()['choices'][0]['message']['content'].strip()
    else:
        actions.user.notify("GPT Failure")
        print(response.json())
        return None

def gpt_task(prompt: str, content: str) -> str:
    """Run a GPT task"""

    resp = gpt_query(prompt, content)

    if resp:
        clip.set_text(resp)

    return resp


@mod.action_class
class UserActions:

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

    def gpt_fix_grammar():
        """Grammar Check"""
        prompt = """
        This is a Fix any mistakes or irregularities in grammar, spelling, or formatting. Use a professional business tone. 
        """
        content = actions.edit.selected_text()

        return gpt_task(prompt, content)


    def gpt_arbitrary_prompt(inputText: str):
        """answer question"""
        prompt = """
        Using a professional tone, generate text that satisfies the question or request given in the prompt. 
        """

        return gpt_task(prompt, inputText)

    def gpt_summarize_this():
        """summarize data"""
        prompt = """
        Summarize this text into a format suitable for business notes. Use a professional business tone.
        """
        content = actions.edit.selected_text()

        return gpt_task(prompt, content)

 
    def gpt_add_context():
        """ add additional context"""
        prompt = """
        Add additional text to the sentence that would be appropriate to the situation and useful in consulting project.  Use a professional business tone
        """

        content = actions.edit.selected_text()

        return gpt_task(prompt, content)



