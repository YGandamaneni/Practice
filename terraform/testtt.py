from selenium import webdriver
import time
from time import sleep


driver = webdriver.Chrome()

#date_string = f'{datetime.now():%Y-%m-%d %H:%M:%S%z}'

web_ui_url="https://python.org"
near_url= "https://dgeo-scaleout-dev.s3.amazonaws.com/synthetic-data/small/seismicCubes_Runsum__15_degrees_2022.55539891/"
mid_url = "https://dgeo-scaleout-dev.s3.amazonaws.com/synthetic-data/small/seismicCubes_Runsum__25_degrees_2022.55539891/"
far_url = "https://dgeo-scaleout-dev.s3.amazonaws.com/synthetic-data/small/seismicCubes_Runsum__35_degrees_2022.55539891/"
output_foldername = "selenium_test97"
bucket_name = "dgeo-scaleout-dev"


driver.get(web_ui_url)

sleep(3)

#near_box=driver.find_element("id", "near")
#mid_box=driver.find_element("id", "mid")
#far_box=driver.find_element("id", "far")

#workflow_name_box=driver.find_element("id","workflow-name")

#try:
   # near_box.send_keys(near_url)
   # sleep(1)
    #mid_box.send_keys(mid_url)
   # sleep(1)
  ## sleep(1)
    #workflow_name_box.send_keys("selenium_test_22")
    #sleep(1)

   
#finally:

driver.quit()
