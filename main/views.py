from django.shortcuts import render

from main import chatgpt, models


def index(request):
    dialogue = models.Dialogue.objects.create(slug="war-and-peace-1")
    models.Response.objects.create(
        kind="system",
        dialogue=dialogue,
        content="You are a helpful assistant who helps people understand the novel War and Peace by Leo Tolstoy.",
    )
    return render(
        request,
        "main/index.html",
        {
            "response_list": models.Response.objects.filter(dialogue=dialogue).order_by(
                "id"
            )[1:],
        },
    )


def chat(request):
    dialogue = models.Dialogue.objects.all().order_by("-id").first()
    chat_value = chatgpt.get_next_response(request.POST["talk"])
    models.Response.objects.create(
        kind="assistant",
        dialogue=dialogue,
        content=chat_value,
    )
    return render(
        request,
        "partials/chatresponse.html",
        {
            "message_list": [
                {
                    "content": request.POST["talk"],
                    "kind": "user",
                },
                {
                    "content": chat_value,
                    "kind": "assistant",
                },
            ]
        },
    )
