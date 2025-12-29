from django.core.management.base import BaseCommand, CommandError
from reddit.models.RedditPosts import RedditPosts
from reddit.models.RedditComments import RedditComments
import requests
from reddit.constants import REDDIT_POST_URL, CATEGORY_CHOICES
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

class Command(BaseCommand):
    help = "Script response for fetching & storing Reddit Post/Comments Data into DB"
    
    def call_api(self, url, headers):
        response_obj = requests.get(url, headers=headers, timeout=3).json()
        print('Res-------------->', response_obj, url)
        return response_obj.status_code, response_obj.text
    
    def handle(self, *args, **kwargs):
        try:
            reddit_data_url = REDDIT_POST_URL
            headers = {
                "User-Agent": "Stock-Sentiment-App-Local-Script/0.1 by u/NamikazeWasTaken"
            }
            
            response_list = []
            
            with ThreadPoolExecutor(max_workers=5) as executor:
                time.sleep(1)
                futures = [executor.submit(self.call_api, reddit_data_url.format(category.lower()), headers) for category in CATEGORY_CHOICES.values()]
                
                for future in futures:
                    response_list.append(future.result())
                    
            print('Response---------------->', response_list)
        
        except Exception as ex:
            self.stdout.write(self.style.ERROR(f"Exception occurred while executing Fetch Reddit Data Command : {str(ex)}"))