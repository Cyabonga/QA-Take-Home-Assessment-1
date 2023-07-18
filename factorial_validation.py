from selenium import webdriver
from selenium.webdriver.common.by import By


# Start the Selenium WebDriver
driver = webdriver.Chrome("/Users/siyabongankosi/PycharmProjects/QA-Take-Home-Assessment/drivers/chromedriver")

# Open the web page
driver.get("http://localhost:6464/factorial")

# Fill in the number input
number_input = driver.find_element(By.ID, "number")
number_input.send_keys("7")

# Submit the form
submit_button = driver.find_element(By.ID, "getFactorial")
submit_button.click()

# Get the result
result_div = driver.find_element(By.ID, "resultDiv")
result = result_div.text
result_style = result_div.get_attribute("style")

# Check if the result is correct
expected_result = "The factorial of 7 is: 5040"
expected_style = 'color: rgb(0, 0, 0);'
assert result == expected_result, f"expected_result{expected_result}, but got {result}"
assert result_style == expected_style, f"Expected style: {expected_style}, but got {result_style}"

# Close the browser
driver.quit()
