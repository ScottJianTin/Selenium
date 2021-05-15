from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

was_source = driver.find_element_by_xpath('//*[@id="box3"]')
us_dest = driver.find_element_by_xpath('//*[@id="box103"]')
actions = ActionChains(driver)
actions.drag_and_drop(was_source, us_dest).perform()

rom_source = driver.find_element_by_xpath('//*[@id="box6"]')
ita_dest = driver.find_element_by_xpath('//*[@id="box106"]')
actions = ActionChains(driver)
actions.drag_and_drop(rom_source, ita_dest).perform()

seo_source = driver.find_element_by_xpath('//*[@id="box5"]')
sk_dest = driver.find_element_by_xpath('//*[@id="box105"]')
actions = ActionChains(driver)
actions.drag_and_drop(seo_source, sk_dest).perform()

osl_source = driver.find_element_by_xpath('//*[@id="box1"]')
nor_dest = driver.find_element_by_xpath('//*[@id="box101"]')
actions = ActionChains(driver)
actions.drag_and_drop(osl_source, nor_dest).perform()

mad_source = driver.find_element_by_xpath('//*[@id="box7"]')
spa_dest = driver.find_element_by_xpath('//*[@id="box107"]')
actions = ActionChains(driver)
actions.drag_and_drop(mad_source, spa_dest).perform()

cop_source = driver.find_element_by_xpath('//*[@id="box4"]')
den_dest = driver.find_element_by_xpath('//*[@id="box104"]')
actions = ActionChains(driver)
actions.drag_and_drop(cop_source, den_dest).perform()

sto_source = driver.find_element_by_xpath('//*[@id="box2"]')
swe_dest = driver.find_element_by_xpath('//*[@id="box102"]')
actions = ActionChains(driver)
actions.drag_and_drop(sto_source, swe_dest).perform()


