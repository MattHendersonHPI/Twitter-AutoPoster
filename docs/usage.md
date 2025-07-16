# Twitter Auto-Poster Usage

## Running the Script
- Ensure Python 3.6+ is installed.
- Run `pip install tweepy python-dotenv schedule`.
- Configure `.env` with Twitter API keys.
- Execute `python autoposter.py` to start posting.

## Scheduling
- Posts to @mrmatthenderson at 09:00 daily.
- Posts to @HPiRVA at 09:30 daily.
- Edit `schedule.every().day.at()` in `autoposter.py` to change times.

## Customization
- Update `templates_hpirva` and `templates_mrmatthenderson` in `autoposter.py` for custom tweets.
- Contact: [HP Investigations](https://www.hpinvestigations.com)