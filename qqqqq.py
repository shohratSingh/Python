# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# import time

# # Setup Chrome WebDriver
# chrome_options = Options()
# chrome_options.add_argument("--user-data-dir=/path/to/your/chrome/profile")  # Update this path
# service = Service('/path/to/chromedriver')  # Update this path
# driver = webdriver.Chrome(service=service, options=chrome_options)

# # Open WhatsApp Web
# driver.get('https://web.whatsapp.com')

# # Wait for user to scan QR code
# input("Press Enter after scanning QR code...")

# # Function to find and open chat with contact
# def open_chat(contact_name):
#     search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
#     search_box.clear()
#     search_box.send_keys(contact_name)
#     time.sleep(2)
#     contact = driver.find_element(By.XPATH, f'//span[@title="{contact_name}"]')
#     contact.click()

# # Function to monitor online status
# def monitor_online_status(contact_name):
#     open_chat(contact_name)
#     while True:
#         try:
#             online_status = driver.find_element(By.XPATH, '//span[text()="online"]')
#             if online_status:
#                 print(f"{contact_name} is online")
#         except:
#             print(f"{contact_name} is offline")
#         time.sleep(5)  # Adjust as needed

# # Main
# if __name__ == "__main__":
#     contact_name = 'Contact Name'  # Replace with the actual contact name
#     monitor_online_status(contact_name)

# # Remember to handle exceptions and close the browser properly







