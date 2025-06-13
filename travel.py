import google.generativeai as genai
from config import api_key

genai.configure(api_key = api_key)

#function to generate travel itinerary based on user input
def generate_itinerary(destination, days, nights, description):
  generation_config = {
    "temperature": 0.4,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
  }

  #initialize the generative model
  model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config
  )

  #start a new chat session with the model
  chat_session = model.start_chat(
  history = [
    {
      "role": "user",
      "parts": [
        f"""write me a travel itinerary to {destination} for {days} days
        and {nights} nights including day-wise activities, accommodation, 
        local food, transport, tips, and tailored to {description}""",
      ],
    },
  ]
  )

  #send the message to the chat and get the response
  response = chat_session.send_message(
  f"""Create a detailed travel itinerart for {days} days 
  and {nights} nights in {destination} tailored to {description}"""
  )

  return response.text