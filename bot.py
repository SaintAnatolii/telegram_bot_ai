import asyncio
from mistralai import Mistral
from conf import CONF


async def main_bot(content):
    api_key = CONF['mistral']
    mistral = Mistral(api_key=api_key)

    res = await mistral.chat.complete_async(
        model= "mistral-large-latest",
        messages = [
            {
                "role": "user",
                "content": content,
            },
        ],
        stream=False
    )
    return res.choices[0].message.content