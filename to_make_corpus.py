import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def get_text_from_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            for script in soup(["script", "style"]):
                script.extract()
            text = soup.get_text()
            text = "\n".join(line.strip() for line in text.splitlines() if line.strip())
            return text
        else:
            print(f"Failed to fetch URL: {url}")
            return None
    except Exception as e:
        print(f"An error occurred while fetching URL {url}: {e}")
        return None

def main():
    urls = [
#ici on a ajouté nos liens
    ]

    for url in urls:
        text = get_text_from_url(url)
        if text:
            filename = url.split("/")[-1] + ".txt"
            with open(filename, "w", encoding="utf-8") as file:
                file.write(text)
                print(f"Text from {url} saved to {filename}")
        else:
            print(f"Failed to get text from {url}")

if __name__ == "__main__":
    main()
