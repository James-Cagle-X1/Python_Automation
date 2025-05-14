import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options (optional)
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Open browser in maximized mode

# Use webdriver-manager to automatically download and manage ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navigate to google.com
driver.get("https://www.google.com")

# Optional: Close the browser after a delay
time.sleep(60)
driver.quit()