import requests
from bs4 import BeautifulSoup

url = "https://bookxchange.in/home"  # Replace with the actual URL
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
}
def extract_links_from_element(element):
    links = []
    for tag in element.find_all('a', href=True):
        links.append(tag['href'])
    return links

def recursive_extract_links(element):
    
    links = []
    for child in element.find_all(recursive=True):
        
        links.extend(extract_links_from_element(child))
    return links
def extract_about_content(element):
    """
    Extracts the text from the current element and its descendants.
    
    Args:
        element (Tag): The element to extract text from.
        
    Returns:
        list: A list of text content from the element and its descendants.
    """
    about_elements = element.find_all(['div', 'section', 'p'], class_=lambda x: x and 'about' in x.lower() or 'about' in element.get('id', '').lower())
    about_content = []
    
    for about_element in about_elements:
        # Extract the text from the current element and its descendants
        about_text = about_element.get_text()
        about_content.append(about_text)
    
    return about_content

def extract_about_content_from_headers(element):
    about_headers = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p']  # Add all header tags you want to consider
    about_content = []

    for header_tag in about_headers:
        headers_with_about = element.find_all(header_tag, string=lambda text: text is not None and 'about' in text.lower())
        for header in headers_with_about:
            content = []
            next_sibling = header.find_next_sibling()
            while next_sibling is not None and next_sibling.name not in about_headers:
                if next_sibling.name is None:  # If it's a NavigableString (text node)
                    content.append(str(next_sibling))
                next_sibling = next_sibling.find_next_sibling()
            about_content.append(' '.join(content))

    return about_content

def extract_contact_details(element):
    contact_details = []
    # Search for specific elements or patterns that contain contact information
    # Adjust the selectors and logic based on the website's structure
    contact_elements = element.find_all(['div', 'section'], class_=lambda x: x and 'contact' in x.lower() or 'contact' in element.get('id', '').lower())
    for contact_element in contact_elements:
        contact_details.append(contact_element.get_text())
    return contact_details
def extract_meta_description(soup):
    meta_description = soup.find('meta', attrs={'name': 'description'})
    
    if meta_description and 'content' in meta_description.attrs:
        return meta_description['content']
    else:
        return None
response = requests.get(url,headers=headers)
html_content = response.content
# print(html_content)


soup = BeautifulSoup(html_content, 'html.parser')
print(soup)
all_links = recursive_extract_links(soup)
print(all_links)
about_links = []

for link in all_links:
    print(link)
    parts = link.split('/')
    for part in parts:
        if 'about' in part:
            about_links.append(link)
            break
    if about_links:
        break

link = None      
for about_link in about_links:
    link = about_link
    print("the about ",about_link)
if(link):
    if(link.startswith("https") or link.startswith("http")):
        print("hii")
        new_link = link
        about_details_response = requests.get(new_link,headers=headers)
        about_html_content = about_details_response.content
        
        about_soup = BeautifulSoup(about_html_content, 'html.parser')
        about_content = extract_about_content(about_soup)
        if(about_content):
            for content in about_content:
                    print("About content:", content.strip())
        else:
            about_content_from_headers = extract_about_content_from_headers(about_soup)
            for content in about_content_from_headers:
                print("About content from headers:", content.strip())
    else:


    
        new_link = url+link
        about_details_response = requests.get(new_link,headers=headers)
        about_html_content = about_details_response.content
        about_soup = BeautifulSoup(about_html_content, 'html.parser')
        about_content = extract_about_content(about_soup)
        if(about_content):
            for content in about_content:
                    print("About content:", content.strip())
        else:
            about_content_from_headers = extract_about_content_from_headers(about_soup)
            for content in about_content_from_headers:
                print("About content from headers:", content.strip())

        contact_details = extract_contact_details(soup)
        for detail in contact_details:
            print("Contact detail:", detail.strip())
else:
    meta_description = extract_meta_description(soup)
    print("Meta Description:", meta_description)



