from django.db import models
#database kuhu laeme markdowni file ja paneme ka pealkirja. Algul oli meil eraldi page, kus oli form, millega üles laadida, aga me otsustasime admin page kasutada, kuna see veidi lihtsam ja kiirem. Lisak saame markdown file koheselt muuta.
class Tekst(models.Model):
    title = models.CharField(max_length=100, null=True)
    dokument = models.FileField(null=True)

