Twitter Auto-Poster
A Python script to automate posting to @HPiRVA and @mrmatthenderson on Twitter/X using Tweepy. Built to streamline social media for HP Investigations and personal branding.
Features

Posts random tweets from predefined templates to avoid duplicates.
Schedules daily posts for @HPiRVA (PI-focused) and @mrmatthenderson (motivational).
Uses environment variables for secure API key management.
Extensible for custom tweet schedules and content.

Setup

Clone the repo:git clone https://github.com/MattHendersonHPI/Twitter-AutoPoster.git


Install dependencies:pip install tweepy python-dotenv schedule


Create a .env file with your Twitter API credentials:HPIRVA_API_KEY=your_hpirva_api_key
HPIRVA_API_SECRET=your_hpirva_api_secret
HPIRVA_ACCESS_TOKEN=your_hpirva_access_token
HPIRVA_ACCESS_TOKEN_SECRET=your_hpirva_access_token_secret
MRMATTHENDERSON_API_KEY=your_mrmatthenderson_api_key
MRMATTHENDERSON_API_SECRET=your_mrmatthenderson_api_secret
MRMATTHENDERSON_ACCESS_TOKEN=your_mrmatthenderson_access_token
MRMATTHENDERSON_ACCESS_TOKEN_SECRET=your_mrmatthenderson_access_token_secret


Run:python autoposter.py



Requirements

Python 3.6+
Tweepy, python-dotenv, schedule

Notes

Get API keys at developer.x.com.
Never commit .env to GitHub.
Customize templates_hpirva and templates_mrmatthenderson in autoposter.py for your tweet content.

Author
Matt Henderson, Private Investigator at HP Investigations | Python enthusiast | Virginia-based
License
This project is licensed under the MIT License - see the LICENSE file for details.
