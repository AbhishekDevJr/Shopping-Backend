from django.core.management.base import BaseCommand, CommandError
from reddit.models.RedditPosts import RedditPosts
from reddit.models.RedditComments import RedditComments
import requests
from reddit.constants import REDDIT_POST_URL, CATEGORY_CHOICES, THREADS_FOR_API_CALL, REDDIT_API_HEADERS
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

class Command(BaseCommand):
    help = "Script response for fetching & storing Reddit Post/Comments Data into DB"
    
    def fetch_cookie_data(self):
        try:
            FETCH_COOKIE_API_HEADERS = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
            }
            
            FETCH_COOKIE_API_URL = "https://shop.amul.com/en/product/amul-high-protein-blueberry-shake-200-ml-or-pack-of-30"
            
            cookie_api_response = requests.get(FETCH_COOKIE_API_URL, FETCH_COOKIE_API_HEADERS, timeout=3)
            
            if cookie_api_response.status_code:
                cookie_data = cookie_api_response.headers.get('Set-Cookie')
                return cookie_data
            
            else:
                # NOTIFY & LOG COOKIE API ISSUE HERE
                return None
        
        except Exception as ex:
            pass
            # Handle Notify Email Here
    
    def handle(self, *args, **kwargs):
        try:
            cookie_data = self.fetch_cookie_data()
            
            if cookie_data:
                PRODUCT_API_URL = "https://shop.amul.com/api/1/entity/ms.products?q=%7B%22alias%22:%22amul-high-protein-blueberry-shake-200-ml-or-pack-of-30%22%7D&limit=1"
                
                PRODUCT_API_HEADERS = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36",
                    "Accept": "application/json, text/plain, */*",
                    "Cookie": cookie_data
                }
                
                product_api_response = requests.get(PRODUCT_API_URL, PRODUCT_API_HEADERS, timeout=3)
                
                
            
            else:
                # LOG & MAIL NOTI HERE
                pass

        except Exception as ex:
            self.stdout.write(self.style.ERROR(f"Exception occurred while executing Fetch Reddit Data Command : {str(ex)}"))