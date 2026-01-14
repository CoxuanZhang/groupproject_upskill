import requests
from bs4 import BeautifulSoup

url = "https://www.wellesley.edu/academics/department/computer-science#faculty"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())

faculty_boxes = soup.find_all('div', class_='faculty_related_item')
faculty_data = []
for faculty_box in faculty_boxes:
    name_element = faculty_box.find('span', class_='faculty_related_item_title_link_label')
    name = name_element.get_text(strip=True) if name_element else None

    image_element = item.find('img', class_='faculty_related_item_image')
    headshot = image_element['src'] if image_element else None

    position_element = item.find('p', class_='faculty_related_item_position')
    position = position_element.get_text(strip=True) if position_element else None

    faculty_data.append({
        'name': name,
        'headshot': headshot,
        'position': position
    })

for faculty in faculty_data:
