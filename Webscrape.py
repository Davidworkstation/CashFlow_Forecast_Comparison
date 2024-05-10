from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Initialize a Selenium WebDriver instance
driver = webdriver.Chrome()  # Or use any other WebDriver you prefer

# Load the webpage
url = 'https://www.macrotrends.net/stocks/charts/JPM/jpmorgan-chase/cash-flow-statement'
driver.get(url)

# Wait for the jqxGrid to load (adjust the CSS selector as needed)
wait = WebDriverWait(driver, 30)
jqxgrid = wait.until(EC.presence_of_element_located((By.ID, 'jqxgrid')))

# Once the jqxGrid is loaded, extract its HTML content
html_content = driver.page_source

# Close the WebDriver
driver.quit()

# Now you can parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
print(soup.prettify())

print("//")
print("//")
print("//")
rows = soup.select('div[id^="row"]')

for row in rows:
    # Find all div elements within the row representing cells
    cells = row.find_all('div', class_=['jqx-grid-cell'])

    # Extract and print the values from each cell
    for cell in cells:
        # Extract the text content of the cell and strip any leading/trailing whitespace
        cell_text = cell.text.strip()
        
        # Print the cell value
        print(cell_text)

    # Add a separator between rows for clarity
    print('-' * 20)