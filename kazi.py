import feedparser
from datetime import datetime, timezone, timedelta, date
from time import gmtime

TIMELIMIT = 90000 # Around 25 hours
TAGS = ["front-end", "Python", "full-stack", "Ruby on Rails"]

def check_if_myjobmag_offer_is_valid(entry):
    # Not valid if older than TIMELIMIT
    now = datetime.timestamp(datetime.now(timezone.utc))
    parsed_date = entry.get('published', 'Thu, 24 Jan 1991 03:00:00 +0000')
    entry_date = datetime.strptime(parsed_date, '%a, %d %b %Y %H:%M:%S %Z').timestamp()

    if now - entry_date > TIMELIMIT:
        return False

    # Not valid if just for USA
    invalid_regions = ['USA Only', 'North America Only']
    entry_region = entry.get('region', '')

    if entry_region in invalid_regions:
        return False

    # Not valid if the summary does not contain any of the tags
    #tags = [t.replace('+', ' ').upper() for t in TAGS]
    #entry_summary = entry.get('summary', '').upper()

    #if not any(t in entry_summary for t in tags):
    #    return False

    return True

def get_myjobmag_offers():
    print('Getting MyJobMag offers...')
    rss = feedparser.parse('https://www.myjobmag.com/jobsxml.xml')
    entries = rss.entries

    offers = [e for e in entries if check_if_myjobmag_offer_is_valid(e) is True]

    return [
        {
            'title': offer.get('title'),
            'company': offer.get('company_name'),
            'date': datetime.strptime(offer.get('published'), '%a, %d %b %Y %H:%M:%S %Z').strftime('%d-%m-%Y'),
            'location': offer.get('region'),
            'link': offer.get('link')
        }
    for offer in offers]

print(get_myjobmag_offers())


def check_if_weworkremotely_offer_is_valid(entry):
    # Not valid if older than TIMELIMIT
    now = datetime.timestamp(datetime.now(timezone.utc))
    parsed_date = entry.get('published', 'Thu, 24 Jan 1991 03:00:00 +0000')
    entry_date = datetime.strptime(parsed_date, '%a, %d %b %Y %H:%M:%S %z').timestamp()

    if now - entry_date > TIMELIMIT:
        return False

    # Not valid if just for USA
    invalid_regions = ['USA Only', 'North America Only']
    entry_region = entry.get('region', '')

    if entry_region in invalid_regions:
        return False

    # Not valid if the summary does not contain any of the tags
    tags = [t.replace('+', ' ').upper() for t in TAGS]
    entry_summary = entry.get('summary', '').upper()

    if not any(t in entry_summary for t in tags):
        return False

    return True

def get_weworkremotely_offers():
    print('Getting We Work Remotely offers...')
    rss = feedparser.parse('https://weworkremotely.com/categories/remote-programming-jobs.rss')
    entries = rss.entries

    offers = [e for e in entries if check_if_weworkremotely_offer_is_valid(e) is True]

    return [
        {
            'title': offer.get('title'),
            'company': offer.get('company_name'),
            'date': datetime.strptime(offer.get('published'), '%a, %d %b %Y %H:%M:%S %z').strftime('%d-%m-%Y'),
            'location': offer.get('region'),
            'link': offer.get('link')
        }
    for offer in offers]
print(get_weworkremotely_offers())

def check_if_remoteio_offer_is_valid(entry):
    # Not valid if older than TIMELIMIT
    now = datetime.timestamp(datetime.now(timezone.utc))
    parsed_date = entry.get('published', '1991-01-24 03:00:00')
    entry_date = datetime.strptime(parsed_date, '%Y-%m-%d %H:%M:%S').timestamp()

    if now - entry_date > TIMELIMIT:
        return False

    # Not valid if no tags are in the summary or the title
    tags = [t.upper() for t in TAGS]
    entry_summary = entry.get('summary', '').upper()
    entry_title = entry.get('title', '').upper()

    if not any(t in entry_summary for t in tags) and not any(t in entry_title for t in tags):
        return False

    return True

def get_remoteio_offers():
    print('Getting remote.io offers...')
    rss = feedparser.parse('https://s3.remote.io/feed/rss.xml/')
    entries = rss.entries

    offers = [e for e in entries if check_if_remoteio_offer_is_valid(e) is True]

    return [
        {
            'title': offer.get('title'),
            'company': offer.get('company'),
            'date': datetime.strptime(offer.get('published'), '%Y-%m-%d %H:%M:%S').strftime('%d-%m-%Y'),
            'link': offer.get('link')
        }
    for offer in offers]


print(get_remoteio_offers())