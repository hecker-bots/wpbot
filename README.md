# wpbot
Simple bot to post comments on WordPress sites
# To use it
1. apt update && apt upgrade
2. apt install git python
3. git clone https://github.com/hecker-bots/wpbot/
4. pip install requests
5. cd && cd /wpbot
6. python script.py [delay] "https://your-wordpress-site" "Your comment." "Name" [first post] [last post] [comments quantity]

Example:
python script.py 12 "https://your-wordpress-site" "This is an automatic comment." "John Doe" 1 5 2
