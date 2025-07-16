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
    "Need answers? HP Investigations delivers discreet, professional results. www.hpinvestigations.com #PrivateInvestigator",
    "OSINT tip: Public records can unlock critical insights. Contact us! #OSINT #RichmondVA",
    "Serving Virginia with expert investigations since 2019. #HPInvestigations",
    "Trust and precision in every case. Reach out at www.hpinvestigations.com #PrivateInvestigator",
    "Uncover the truth with our advanced investigative tools. #VirginiaPI",
]

# Templates for @mrmatthenderson (motivational/personal)
templates_mrmatthenderson = [
    "Every challenge is a chance to grow. Keep pushing! #Motivation #Virginia",
    "Learning Python one script at a time. Join me! #Coding #Tech",
    "Stay curious, stay learning. #GrowthMindset #PiedmontPathfinder",
    "Life’s mysteries are worth exploring. #PersonalGrowth",
    "Building tools and chasing goals in VA. #Python #Motivation",
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