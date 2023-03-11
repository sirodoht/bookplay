import openai
from django.conf import settings

from main import models

openai.api_key = settings.OPENAI_API_KEY


def get_next_response(question):
    print("calling openai api with: ", build_current_dialogue(question))
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=build_current_dialogue(question),
    )

    return response["choices"][0]["message"]["content"]


def build_current_dialogue(question):
    dialogue = models.Dialogue.objects.all().first()
    message_list = []
    for response in models.Response.objects.filter(dialogue=dialogue).order_by("id"):
        message_list.append(
            {
                "role": response.kind,
                "content": response.content,
            }
        )

    # add new question
    message_list.append(
        {
            "role": "user",
            "content": question,
        }
    )

    return message_list
