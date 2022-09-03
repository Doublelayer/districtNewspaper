import crawler
import db.file_provider as file_provider
import messenger.whats_app as whats_app

url = "https://schenefelder-bote.de/archiv/"
db = "luruper.txt"


def get_file_name(href):
    return href.split("/")[-1]

def run():
    soup = crawler.get_soup(url)
    hrefs = crawler.find_all_anchor_href(soup)
    filtered_href = list(filter(lambda href: href.endswith("pdf"), hrefs))
    unknown_hrefs = get_unknown_hrefs(filtered_href)
    whats_app.send_notification("Luruper Nachrichten", unknown_hrefs)
    file_provider.write_hrefs(unknown_hrefs, db)


def get_unknown_hrefs(found_hrefs: list):
    return list(set(found_hrefs) - set(file_provider.get_file_content_as_list(db)))
