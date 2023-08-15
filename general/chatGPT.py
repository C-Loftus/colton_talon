import requests
import json, os
from typing import Optional
from talon import Module, actions, clip

# TODO: Make it only available to run one request at a time

mod = Module()
mod.setting(
    "open_ai_fixup_prompt",
    type=str,
    default="Fix any grammar, ponctuation, and typos.",
    desc="Prompt to use when using GPT to fix misrecognitions.",
)

TOKEN = os.environ["OPENAI_API_KEY"]

def gpt_query(prompt: str, content: str) -> Optional[str]:
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

    response = requests.post(
        'https://api.openai.com/v1/chat/completions',
        headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content'].strip()

    return None

def gtp_task(prompt: str, content: str, task_name: str) -> str:
    """Run a GPT task"""
    actions.app.notify(f"GPT: Task ({task_name}) started")
    resp = gpt_query(prompt, content)

    if not resp:
        actions.app.notify('GPT: Something went wrong...')
        return None
    
    clip.set_text(resp)
    actions.app.notify(f'GPT: Task ({task_name}) finished')
    return resp


@mod.action_class
class Actions:
    def fix_grammar():
        """Grammar Check"""
        prompt = """
        Fix any mistakes or irregularities in grammar, spelling, or formatting. Use a professional business tone.
        """
        content = actions.edit.selected_text()

        return gtp_task(prompt, content, "Grammar Check")


    
    def summarize_this():
        """summarize data"""
        prompt = """
        Summarize this text into a format suitable for business notes. Use a professional business tone.
        """
        content = actions.edit.selected_text()

        return gtp_task(prompt, content, "Summarization")

 
    def add_context():
        """ add additional context"""
        prompt = """
        Add additional text to the sentence that would be appropriate to the situation and useful in consulting project.  Use a professional business tone
        """

        content = actions.edit.selected_text()

        return gtp_task(prompt, content, "Summarization")
    
