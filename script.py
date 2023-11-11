import requests
import time
import sys
import random
import string

# Get command line arguments
delay = int(sys.argv[1])  # Delay in seconds
website_link = sys.argv[2]  # Website link
comment_content = sys.argv[3]  # Comment content
comment_name = sys.argv[4]  # Name for the comments
start_post_id = int(sys.argv[5])  # Start post ID
end_post_id = int(sys.argv[6])  # End post ID
comments_per_post = int(sys.argv[7])  # Quantity of comments per post

# Get proxy list from user
use_proxy = input("Do you want to use a proxy? (y/n): ")
proxies = None
if use_proxy.lower() == "y":
    proxy_list = input("Enter the list of proxies (separated by commas): ").split(",")
    proxy_index = 0

# Set the URL of your WordPress site's API
api_url = f"{website_link}/wp-json/wp/v2/comments"

# Set the headers for the API request
headers = {
    "Content-Type": "application/json",
}

# Send the API requests to post comments
for post_id in range(start_post_id, end_post_id + 1):
    for i in range(comments_per_post):
        # Generate random characters
        random_chars = ''.join(random.choices(string.ascii_lowercase + string.digits, k=3))
        
        # Add random characters to comment content
        comment_content_with_chars = f"{comment_content} {random_chars}"
        
        # Generate random email address
        email = f"{random_chars}@gmail.com"
        
        comment_data = {
            "content": comment_content_with_chars,
            "post": post_id,
            "author_name": comment_name,
            "author_email": email
        }
        
        if use_proxy.lower() == "y":
            # Get the current proxy
            proxy = { "http": proxy_list[proxy_index], "https": proxy_list[proxy_index] }
            
            # Send the API request with the current proxy
            response = requests.post(api_url, headers=headers, json=comment_data, proxies=proxy)
            
            # Move to the next proxy after every 10 comments
            if (i + 1) % 10 == 0:
                proxy_index = (proxy_index + 1) % len(proxy_list)
        else:
            # Send the API request without a proxy
            response = requests.post(api_url, headers=headers, json=comment_data)
        
        if response.status_code == 201:
            print(f"Comment {i+1} on Post {post_id} posted successfully.")
        else:
            print(f"Failed to post comment {i+1} on Post {post_id}. Error: {response.text}")
        time.sleep(delay)
