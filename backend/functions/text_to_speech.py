import requests
from decouple import config

ELEVEN_LABS_API_KEY = config("111d5292eb4c9b66d2f4fc7fa211b56f", default="111d5292eb4c9b66d2f4fc7fa211b56f")

# Eleven labs
# Convert text to speech
def convert_text_to_speech(message):

    # Define data (Body)
    body = {
        "text": message,
        "voice_settings": {
            "stability": 0,
            "similarity_boost": 0,
        }
    }

    # Define voice
    voice_rachel = "21m00Tcm4TlvDq8ikWAM"
    
    # Constructing headers and endpoint
    headers = {"xi-api-key": ELEVEN_LABS_API_KEY, "Content-Type": "application/json", "accept": "audio/mpeg"}
    endpoint = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_rachel}"

    # Send request
    try:
        response = requests.post(endpoint, json=body, headers=headers)
    except Exception as e:
        return 

        # Check for a successful response
    if response.status_code == 200:
        return response.content  # Return the binary audio content

     # Handle exceptions appropriately
    else: 
        return # Handle cases where the response is not successful
