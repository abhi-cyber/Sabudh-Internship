import requests
from bs4 import BeautifulSoup

def fetch_webpage(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve the webpage: {response.status_code}")
        return None

def parse_html(html_content):
    soup = BeautifulSoup(html_content, 'html5lib')
    return soup

def extract_data(soup):
    headings = []
    for heading in soup.find_all(['h1', 'h2', 'h3']):
        headings.append(heading.get_text())
    return headings

def main():
    url = "https://www.geeksforgeeks.org/python-programming-language/"
    html_content = fetch_webpage(url)
    if html_content:
        soup = parse_html(html_content)
        data = extract_data(soup)
        print("Extracted Data:")
        for item in data:
            print(item)

if __name__ == "__main__":
    main()