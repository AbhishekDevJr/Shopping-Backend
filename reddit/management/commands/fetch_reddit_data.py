from django.core.management.base import BaseCommand, CommandError
from reddit.models.RedditPosts import RedditPosts
from reddit.models.RedditComments import RedditComments
import requests
from reddit.constants import REDDIT_POST_URL, CATEGORY_CHOICES, THREADS_FOR_API_CALL, REDDIT_API_HEADERS
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

class Command(BaseCommand):
    help = "Script response for fetching & storing Reddit Post/Comments Data into DB"
    
    def call_api(self, url, headers):
        response_obj = requests.get(url, headers=headers, timeout=3)
        return {
            "status_code": response_obj.status_code,
            "res": response_obj.json()
        }
    
    def handle(self, *args, **kwargs):
        try:
            reddit_data_url = REDDIT_POST_URL            
            response_list = []
            
            with ThreadPoolExecutor(max_workers=THREADS_FOR_API_CALL) as executor:
                time.sleep(1)
                futures = []
                
                for category in CATEGORY_CHOICES:
                     futures.append(
                         executor.submit(self.call_api, reddit_data_url.format(category.lower()), REDDIT_API_HEADERS)
                     )
                
                for future in futures:
                    response_list.append(future.result())

        except Exception as ex:
            self.stdout.write(self.style.ERROR(f"Exception occurred while executing Fetch Reddit Data Command : {str(ex)}"))