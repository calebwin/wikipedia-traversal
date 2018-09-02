import urllib.request

# keywords that mark a page to be ignored if the page's title contains the keyword
IGNORABLE_KEYWORDS = ["Help:", "File:", "English", "Chinese", "Hindustani", "Hindi", "Spanish", "Arabic", "French", "Russian", "Portugese", "German", "Japanese", "Turkish", "Korean", "Italian", "Latin"]

def traverse(traversal_start_page_title, traversal_len):
    print()
    if traversal_len > 0:
        with urllib.request.urlopen('http://wikipedia.org/wiki/' + traversal_start_page_title) as response:
            # limit page to searchable section
            html = str(response.read())
            html = html[html.find("<p>") : len(html)] # limit to everything from start of body text
            html = html[html.find("<a href=\"/wiki/") + len("<a href=\"/wiki/") : len(html)] # limit to everything from start of first link

            # find title of next page
            next_page_title = html[0 : html.find("\"")]
            while next_page_title.find("Help:") > -1 or next_page_title.find("File:") > -1:
                html = html[html.find("<a href=\"/wiki/") + len("<a href=\"/wiki/") : len(html)] # limit to everything from start of next link
                next_page_title = html[0 : html.find("\"")]

            print(next_page_title.replace("_", " "))
            traverse(next_page_title, traversal_len - 1)

def rtraverse(traversal_start_page_title, traversal_len):
    print()
    if traversal_len > 0:
        with urllib.request.urlopen('http://wikipedia.org/wiki/' + traversal_start_page_title) as response:
            # limit page to searchable section
            html = str(response.read())
            html = html[html.find("<p>") : html.rfind("See also</span>")] # limit to body text
            html = html[0 : html.rfind("</a>")] # limit to everything from start to last link

            # find title of next page
            next_page_title_exists = True
            next_page_title = html[html.rfind(">") + 1 : len(html)]
            next_page_title_includes_ignorable_keywords = False
            for IGNORABLE_KEYWORD in IGNORABLE_KEYWORDS:
                if next_page_title.find(IGNORABLE_KEYWORD) > -1:
                    next_page_title_includes_ignorable_keywords = True
            while next_page_title_includes_ignorable_keywords:
                html = html[0 : html.rfind("</a>")] # limit to everything from start to next link
                next_page_title_exists = html.rfind(">") > -1
                next_page_title = html[html.rfind(">") : len(html)]
                next_page_title_includes_ignorable_keywords = False
                for IGNORABLE_KEYWORD in IGNORABLE_KEYWORDS:
                    if next_page_title.find(IGNORABLE_KEYWORD) > -1:
                        next_page_title_includes_ignorable_keywords = True

            print(next_page_title)
            traverse(next_page_title.replace(" ", "_"), traversal_len - 1)

def remove_spaces(txt):
    return txt.replace(" ", "_")

if __name__ == '__main__':
    if input("Traverse using last links found in pages (Y/N)? ") == "N":
        traverse(remove_spaces(input("Title of initial page: ")), int(input("Length of traversal: ")))
    else:
        rtraverse(remove_spaces(input("Title of initial page: ")), int(input("Length of traversal: ")))
