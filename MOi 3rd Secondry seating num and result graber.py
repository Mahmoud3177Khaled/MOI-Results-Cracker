from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()  # Or specify the path if not in PATH: webdriver.Chrome(executable_path='/path/to/chromedriver')

# Open the website
driver.get("https://g12.emis.gov.eg/")  # Replace with the actual URL of the website

results = []

n = 227000
while n<227200:
    # print(n)
    # n = n+1

    print("putting: ")
    print(str(n))

    try:
        # Wait for the page to load completely
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "input"))  # Adjust based on the expected first element
        )

        # Find the text field and input data
        text_field = driver.find_element(By.ID, "SeatingNo")  # Replace with the actual ID or other selector
        text_field.clear()
        # time.sleep(0.3)
        text_field.send_keys(str(n))  # Replace with your actual input data

        # Find the button and click it
        submit_button = driver.find_element(By.CLASS_NAME, "btn")  # Replace with the actual ID or other selector
        submit_button.click()

        # Wait for the new page to load and the table to be present
        WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.CLASS_NAME, "table"))
        )


        # Find the telephone number by locating the 'الهاتف' header and selecting its sibling <td>
        Name = None
        Name = driver.find_element(By.XPATH, "//th[text()='الإسم']/following-sibling::td").text

        # school = None
        # school = driver.find_element(By.XPATH, "//th[text()='المدرسة']/following-sibling::td").text

        # print(school)

        # Print the telephone number
        if("محمد احمد محمد سعيد" in Name):
            results.append(n)
            print("One Match Found:", Name)

        driver.back()

        # Additional logic can be added here if you need to interact with more elements or navigate further

    except Exception as e:
        print("error: num invalid")
        n = n + 1
        # driver.quit()
        continue

    n = n + 1

    # finally:
    #     # Close the browser
    #     driver.quit()


driver.quit()

print(results)
