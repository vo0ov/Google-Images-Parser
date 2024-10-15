import requests
from bs4 import BeautifulSoup


def get_images(q: str, count: int) -> list:
    results = []

    start_counter = 0
    while len(results) < count:
        url = f'https://www.google.no/search?q={q}&client=opera&hs=cTQ&source=lnms&tbm=isch&sa=X&ved=0ahUKEwig3LOx4PzKAhWGFywKHZyZAAgQ_AUIBygB&biw=1920&bih=982&filter=0&safe=off&start={start_counter}'

        page = requests.get(url).text
        soup = BeautifulSoup(page, 'html.parser')

        imgs = soup.find_all('img')
        if len(imgs) == 0:
            break

        for raw_img in imgs:
            link = raw_img.get('src')

            if start_counter >= count:
                break

            if link and 'http' in link:
                results.append(link)
                start_counter += 1

    return results
