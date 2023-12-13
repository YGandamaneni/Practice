from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from time import sleep
from datetime import datetime

#date_string = f'{datetime.now():%Y-%m-%d %H:%M:%S%z}'

web_ui_url="http://ui.scaleout.dgeo.shell.com/"
near_url= "https://dgeo-scaleout-dev.s3.amazonaws.com/synthetic-data/small/seismicCubes_Runsum__15_degrees_2022.55539891/"
mid_url = "https://dgeo-scaleout-dev.s3.amazonaws.com/synthetic-data/small/seismicCubes_Runsum__25_degrees_2022.55539891/"
far_url = "https://dgeo-scaleout-dev.s3.amazonaws.com/synthetic-data/small/seismicCubes_Runsum__35_degrees_2022.55539891/"
output_foldername = "selenium_test97"
bucket_name = "dgeo-scaleout-dev"

driver = webdriver.Chrome()
driver.get(web_ui_url)

sleep(3)

near_box=driver.find_element("id", "near")
mid_box=driver.find_element("id", "mid")
far_box=driver.find_element("id", "far")

workflow_name_box=driver.find_element("id","workflow-name")

try:
    near_box.send_keys(near_url)
    sleep(1)
    mid_box.send_keys(mid_url)
    sleep(1)
    far_box.send_keys(far_url)
    sleep(1)
    workflow_name_box.send_keys("selenium_test_22")
    sleep(1)

    ok_button=driver.find_element("id", "undefined-ok-button")
    ok_button.send_keys(Keys.RETURN)
    sleep(3)

    radio_button=driver.find_element(By.XPATH, '//input[@type="radio" and @value="Suriname Shallow"]')
    #Suriname Deep

    if not radio_button.is_selected():
        radio_button.click()

    ok_button_2 =driver.find_element("id", "undefined-ok-button")
    ok_button_2.send_keys(Keys.RETURN)

    sleep(5)
    output_name = driver.find_element(By.ID,"name")
    output_directory = driver.find_element("id","directory")
    output_subfolder = driver.find_element("id","subfolder")

    output_name.send_keys(output_foldername)
    output_directory.send_keys(bucket_name)
    
    sleep(5)
    ok_button_3 =driver.find_element("id", "undefined-ok-button")
    ok_button_3.send_keys(Keys.RETURN)

    sleep(30)

except Exception as e:
    print("Exception:\n=================")
    print(e)

driver.quit()
