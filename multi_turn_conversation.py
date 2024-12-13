from groq import Groq

client = Groq(api_key="Your grooq api key")
completion = client.chat.completions.create(
    model="llama-3.2-11b-vision-preview",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "What is in this image?"
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://upload.wikimedia.org/wikipedia/commons/d/da/SF_From_Marin_Highlands3.jpg"
                    }
                }
            ]
        },
        {
            "role": "user",
            "content": "Tell me more about the area."
        }
    ],
    temperature=1,
    max_tokens=1024,
    top_p=1,
    stream=False,
    stop=None,
)

print(completion.choices[0].message)
