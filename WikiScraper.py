import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}


def findLinks(link):
    global traverse_count, found, traversed_links
    print("Traversing: " + link)

    page = requests.get(link, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    found_links = []
    count_list = []
    traversed_links.append(link)
    traverse_count += 1

    for a in soup.find_all('a', href=True):
        if desired_page[30:] == a["href"][6:]:
            found = True
        elif a["href"].startswith("/wiki/") and a["href"][6:] not in found_links and checkUrl(a["href"]) is True and "https://en.wikipedia.org" + a["href"] not in traversed_links:
            found_links.append(a["href"][6:])

    link_scale = int(((len(found_links) - 10) / (2600 - 10))*100) + 1
    print(">> " + str(len(found_links)) + " more links discovered")
    print(">> Scanning " + str(link_scale) + " for further matches")

    if found:
        print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print(">> " + desired_page + " found on page: " + link)
        printTraversed()
    else:
        for i in range(link_scale):
            count_list.append(scan("https://en.wikipedia.org/wiki/" + found_links[i]))
            print(str(found_links[i]) + " || COMMON LINKS: " + str(count_list[i]))
            if count_list[i] > 70:
                print("!!!! " + str(found_links[i]) + " has over 70! Stopping search and traversing...")
                break

        max_pos = count_list.index(max(count_list))

        print(">> " + found_links[max_pos] + " has the best match to your end link with " + str(count_list[max_pos]) + " links in common")
        findLinks("https://en.wikipedia.org/wiki/" + found_links[max_pos])


def printTraversed():
    print("Links traversed in order:")
    for i in range(len(traversed_links)):
        print(str(i) + " " + traversed_links[i])


def checkUrl(url):
    for error in errors:
        if error in url:
            return False
    return True


def init_scan(link):
    global desired_page_links
    page = requests.get(link, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    for a in soup.find_all('a', href=True):
        if a["href"].startswith("/wiki/") and a["href"][6:] not in desired_page_links and checkUrl(a["href"]) is True:
            desired_page_links.append(a["href"][6:])


def scan(link):
    global desired_page_links
    page = requests.get(link, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    scan_links = []

    for a in soup.find_all('a', href=True):
        if a["href"].startswith("/wiki/") and a["href"][6:] not in scan_links and checkUrl(a["href"]) is True:
            scan_links.append(a["href"][6:])

    return len(frozenset(desired_page_links).intersection(scan_links)) - 2


errors = [".pdf", "download", ".jpg", ".png", ".JPG", ".svg", ".ogg", "help", "Wikipedia", "Help", "Special", "Template"]
traversed_links = []
traverse_count = 0
desired_page_links = []
found = False
desired_page = input("Enter full Wikipedia destination URL: ")[:-1]
init_scan(desired_page)
starting_page = input("Please enter your full Wikipedia starting URL, or enter 'r' for a random page: ")
if starting_page == "r":
    findLinks("https://en.wikipedia.org/wiki/Special:Random")
else:
    findLinks(starting_page[:-1])
