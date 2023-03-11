from django.db import models


class Dialogue(models.Model):
    slug = models.CharField(max_length=10)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.slug


class Response(models.Model):
    dialogue = models.ForeignKey(Dialogue, on_delete=models.CASCADE)
    content = models.TextField()

    # options: "system", "user", "assistant"
    kind = models.CharField(max_length=50)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.content[:30] + "..."
