import instaloader
from instabot import Bot
import time
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# Authentication to Instagram
username = 'username'
password = 'password'
bot = Bot()

# Increase sleep duration to 15 minutes
sleep_duration = 900

# Limit login attempts to 3
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    try:
        logging.info("Attempting to log in to Instagram...")
        bot.login(username=username, password=password, use_cookie=False)
        logging.info("Login successful.")
        break  # Exit the loop if login is successful
    except Exception as login_error:
        logging.error(f"Login failed: {login_error}")
        attempts += 1

        if attempts < max_attempts:
            # Implement exponential backoff
            sleep_duration *= 2
            logging.warning(f"Sleeping for {sleep_duration // 60} minutes before the next login attempt...")
            time.sleep(sleep_duration)

# List of keywords
keywords = [key words]

# Function to check and report abuse
def check_and_report_abuse(keywords):
    try:
        logging.info("Downloading posts and stories...")
        loader = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(loader.context, "mihaelaa.mika")

        for post in profile.get_posts():
            for keyword in keywords:
                if keyword in post.caption:
                    try:
                        logging.info(f"Reporting post for abuse: {post.shortcode}")
                        bot.report_user(profile.username)
                        logging.info("Post reported successfully.")
                    except Exception as report_error:
                        logging.error(f"Error reporting post: {report_error}")
                    break

        for story in profile.get_stories():
            for keyword in keywords:
                if keyword in story.caption:
                    try:
                        logging.info(f"Reporting story for abuse: {story.shortcode}")
                        bot.report_user(profile.username)
                        logging.info("Story reported successfully.")
                    except Exception as report_error:
                        logging.error(f"Error reporting story: {report_error}")
                    break

    except Exception as error:
        logging.error(f"An error occurred: {error}")

# Run the abuse check continuously
while True:
    logging.info("Starting the loop...")
    check_and_report_abuse(keywords)
    logging.info(f"Sleeping for {sleep_duration // 60} minutes...")
    time.sleep(sleep_duration)
