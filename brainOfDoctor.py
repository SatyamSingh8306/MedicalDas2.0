import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
load_dotenv()

#setup GARO API Key
GAOQ_API_KEY = os.environ.get("GAOQ_API_KEY")

#convert image into required format
import base64
# image_path = "acne.jpg"
# image_file = open(image_path,"rb")
# encoded_image = base64.b64encode(image_file.read()).decode("utf-8")

def encode_image(image_path):   
    image_file=open(image_path, "rb")
    return base64.b64encode(image_file.read()).decode('utf-8')
#steup multimodel LLM

model_name = "llama-3.2-90b-vision-preview"


def analyze_image_with_query(query, model, encoded_image):
    
    client = ChatGroq(
        model=model
    )
    messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text", 
                        "text": query
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{encoded_image}",
                        },
                    },
                ],
            }
        ]

    result = client.invoke(messages)
    return result.content