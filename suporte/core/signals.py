from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Funcionario

@receiver(post_save, sender=User)
def criar_funcionario(sender, instance, created, **kwargs):
    if created:
        Funcionario.objects.create(usuario=instance, cargo="Técnico")
