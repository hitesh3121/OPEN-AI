from fastapi import HTTPException
from openai import OpenAI
from settings import settingsConstants


async def openAI_API():
    secretKey = settingsConstants["OPEN_AI_KEY"]
    try:
        client = OpenAI(api_key=secretKey)
        completion = await client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
                {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
            ]
        )
        return completion
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
