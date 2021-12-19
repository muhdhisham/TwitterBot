from django.core.management.base import BaseCommand

from bot_app.models import LastFollower, OutBoundDirectMessage

from bot_app.utils import get_auth_api

class Command(BaseCommand):
    
    def handle(self, *args,**kwargs):
        
        try:
            
            api= get_auth_api()
            
            last_follower_id = LastFollower.objects.get().last_follower_id
            
            message = OutBoundDirectMessage.objects.get().message
            
            for follower in api.followers_ids():
                if follower == last_follower_id:
                    break
                else:
                    api.send_direct_message(follower, message)
            
        except LastFollower.DoesNotExist:
            
            api = get_auth_api()
            
            last_follower_id = api.followers_ids()[0]
            
            LastFollower.objects.create(last_follower_id=last_follower_id)
            
        except Exception as e:
            
            print(e)
            