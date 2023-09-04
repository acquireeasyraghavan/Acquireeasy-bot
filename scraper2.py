import requests
from bs4 import BeautifulSoup

def clean_file():
    file_path = 'company_info.txt'  # Replace with the actual file path

    with open(file_path, 'r+', encoding='utf-8') as file:
        content = file.read()
        content_without_spaces = ''.join(content.split())
        file.seek(0)
        file.write(content_without_spaces)
        file.truncate()

def scrape_company_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    output_file = 'company_info.txt'
    output_string = ''

    with open(output_file, 'w', encoding='utf-8') as file:
        # Define a list of potential HTML tags that may contain company information
        tag_list = ['h1', 'h2', 'h3', 'p', 'span', 'header']

        # Search for the company information in the different HTML tags
        for tag_name in tag_list:
            elements = soup.find_all(tag_name)
            for element in elements:
                # Write the tag name and its corresponding content to the file
                file.write(f'Tag: {tag_name}\n')
                file.write(f'Content: {element.text.strip()}\n')
                file.write('---\n')

                # Add the tag name and content to the output string
                output_string += f'Tag: {tag_name}\n'
                output_string += f'Content: {element.text.strip()}\n'
                output_string += '---\n'

        # Search for company information within <div> elements based on their contents
        div_elements = soup.find_all('div')
        for div_element in div_elements:
            if 'company' in div_element.text.lower() or 'about' in div_element.text.lower():
                # Write the tag name and its corresponding content to the file
                file.write('Tag: div\n')
                file.write(f'Content: {div_element.text.strip()}\n')
                file.write('---\n')

                # Add the tag name and content to the output string
                output_string += 'Tag: div\n'
                output_string += f'Content: {div_element.text.strip()}\n'
                output_string += '---\n'

        # Search for company information within <section> elements based on their contents
        section_elements = soup.find_all('section')
        for section_element in section_elements:
            if 'company' in section_element.text.lower() or 'about' in section_element.text.lower():
                # Write the tag name and its corresponding content to the file
                file.write('Tag: section\n')
                file.write(f'Content: {section_element.text.strip()}\n')
                file.write('---\n')

                # Add the tag name and content to the output string
                output_string += 'Tag: section\n'
                output_string += f'Content: {section_element.text.strip()}\n'
                output_string += '---\n'

    print(f"Company information saved to {output_file}")

    return output_string

# Example usage
url = 'https://grouppal.in'  # Replace with the actual website URL
output_string = scrape_company_info(url)

# Print the entire output string
print(output_string)
