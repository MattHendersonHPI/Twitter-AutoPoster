import tweepy
import schedule
import time
import random
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API credentials for @HPiRVA
client_hpirva = tweepy.Client(
    consumer_key=os.getenv("HPIRVA_API_KEY"),
    consumer_secret=os.getenv("HPIRVA_API_SECRET"),
    access_token=os.getenv("HPIRVA_ACCESS_TOKEN"),
    access_token_secret=os.getenv("HPIRVA_ACCESS_TOKEN_SECRET")
)

# API credentials for @mrmatthenderson
client_mrmatthenderson = tweepy.Client(
    consumer_key=os.getenv("MRMATTHENDERSON_API_KEY"),
    consumer_secret=os.getenv("MRMATTHENDERSON_API_SECRET"),
    access_token=os.getenv("MRMATTHENDERSON_ACCESS_TOKEN"),
    access_token_secret=os.getenv("MRMATTHENDERSON_ACCESS_TOKEN_SECRET")
)

# Track recent posts to avoid duplicates
recent_posts = {"HPiRVA": [], "mrmatthenderson": []}

# Templates for @HPiRVA (PI-focused)
templates_hpirva = [
    "Uncovering truth with precision at HP Investigations. #PrivateInvestigator #RichmondVA",
    "OSINT tip: Cross-check public records for reliable insights. #OSINT #Investigations",
    "Serving Virginia with expert investigative services. Contact us! #HPInvestigations",
    "Stay vigilant: Background checks can reveal critical details. #PrivateInvestigator",
]

# Templates for @mrmatthenderson (personal/motivational)
templates_mrmatthenderson = [
    "Keep pushing forward, no matter the challenge! #Motivation #Virginia",
    "Every day is a chance to learn something new. #Python #GrowthMindset",
    "Exploring tech and truth in the Piedmont. #LifeLessons",
    "Stay curious and keep investigating! #PersonalGrowth",
]

def post_to_hpirva():
    try:
        available_templates = [t for t in templates_hpirva if t not in recent_posts["HPiRVA"]]
        if not available_templates:
            available_templates = templates_hpirva
            recent_posts["HPiRVA"].clear()
        post_text = random.choice(available_templates)
        client_hpirva.create_tweet(text=post_text)
        print(f"Posted to @HPiRVA at {time.strftime('%H:%M:%S %Y-%m-%d')}: {post_text}")
        recent_posts["HPiRVA"].append(post_text)
        if len(recent_posts["HPiRVA"]) > 3:
            recent_posts["HPiRVA"].pop(0)
    except Exception as e:
        print(f"Error posting to @HPiRVA: {e}")

def post_to_mrmatthenderson():
    try:
        available_templates = [t for t in templates_mrmatthenderson if t not in recent_posts["mrmatthenderson"]]
        if not available_templates:
            available_templates = templates_mrmatthenderson
            recent_posts["mrmatthenderson"].clear()
        post_text = random.choice(available_templates)
        client_mrmatthenderson.create_tweet(text=post_text)
        print(f"Posted to @mrmatthenderson at {time.strftime('%H:%M:%S %Y-%m-%d')}: {post_text}")
        recent_posts["mrmatthenderson"].append(post_text)
        if len(recent_posts["mrmatthenderson"]) > 3:
            recent_posts["mrmatthenderson"].pop(0)
    except Exception as e:
        print(f"Error posting to @mrmatthenderson: {e}")

# Test immediate posts
post_to_hpirva()
post_to_mrmatthenderson()

# Schedule posts (staggered for rate limits)
schedule.every().day.at("09:00").do(post_to_mrmatthenderson)
schedule.every().day.at("09:30").do(post_to_hpirva)
print("X posting script started. Waiting for scheduled posts...")
while True:
    schedule.run_pending()
    time.sleep(60)