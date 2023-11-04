from talon import Module, actions, Context
import requests
import json, os, time
from pathlib import Path

if os.name == 'nt':
    import win32com.client

mod = Module()



@mod.action_class
class Actions:
    def robot_tts(text: str):
        '''text to speech with robot voice'''

    def natural_tts(text: str):
        """text to speech"""

        # Split the text into batches of 2400 characters
        batch_size = 2400
        batches = [text[i:i+batch_size] 
                   for i in range(0, len(text), batch_size)
                ]
        
        def send_request(batched_text: str):
            # Define the API endpoint URL
            url = 'https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM?optimize_streaming_latency=0&output_format=mp3_44100_128'
    
            # Define the request headers
            headers = {
                'accept': 'audio/mpeg',
                'xi-api-key': os.environ["11LABS_KEY"],
                'Content-Type': 'application/json',
            }
    
            # Define the request data as a Python dictionary
            data = {
                'text': batched_text,
                'model_id': 'eleven_monolingual_v1',
                'voice_settings': {
                    'stability': 0,
                    'similarity_boost': 0,
                    'style': 0,
                    'use_speaker_boost': True
                }
            }
    
            # Convert the data dictionary to JSON format
            data_json = json.dumps(data)
    
            # Make the POST request
            actions.user.notify('Requesting audio file...')
            response = requests.post(url, headers=headers, data=data_json)
    
            # Check the response status and content
            if response.status_code != 200:
                actions.user.notify(f'Request failed with status code {response.status_code}:')
                print(response.text)
            
            # Request was successful
            basename = f'output-{time.time()}.mp3'

            output_dir = 'tts'
            if len(batches) > 1:
                # first 10 chars
                dir_header = str(batches[0][:10]).strip().replace(' ', '_').replace('\\', '_')

                output_dir = os.path.join(output_dir, dir_header)

            Path(output_dir).mkdir(parents=True, exist_ok=True)
    
            full_name = os.path.join(output_dir, basename)

            with open(full_name, 'wb') as f:
                f.write(response.content)
            print('Audio file saved as ' + full_name)

        for batch in batches:
            send_request(batch)         

ctxWindows = Context()
ctxWindows.matches = r"""
os: windows
"""

@ctxWindows.action_class('user')
class UserActions:
    
    def robot_tts(text: str):
        """text to speech"""
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        speaker.Speak(text)



