from django.db.models.signals import post_save  # this signal gets fired when an object is saved, in this case we need a
#post_save signal when a user is created

from django.contrib.auth.models import User  #User model here is a sender since it's going to be what's sending a signal

from django.dispatch import receiver  # a reciever is going to be a function that gets this signal and performs a task

from .models import Profile



'''Here user sends the post_save signal to the receiver(create_profile) which gives all these arguments(including
instance and created). If the user is created then the profile with that instance of user is created'''
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
