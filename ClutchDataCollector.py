from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

# open the file in the write mode
file = open('output.csv', 'r+', encoding="utf-8")
file.truncate(0)
# create the csv writer
file.write("SERVICES,DOMAIN,COMPANY,WEBSITE,LOCATION,RATING,REVIEW COUNT,HOURLY RATE,MIN PROJECT SIZE,EMPLOYEE SIZE" + '\n')
# instantiate a webdriver instance
driver = webdriver.Chrome()
# make it full screen
driver.maximize_window()
# navigate to the website
driver.get("https://clutch.co/")
sleep(2)
driver.find_element(by=By.XPATH, value="//a[text()='Close']").click()
driver.find_element(by=By.XPATH, value="//a[@href='/sitemap']").click()
sleep(2)
# count top level number of sitemaps, remove the last one
numberOfSitemaps = len(driver.find_elements(by=By.XPATH, value="//div[@class='sitemap-wrap']"))
for value in range(1, numberOfSitemaps):
    xpathForSitemap = "(//div[@class='sitemap-wrap'])["+str(value)+"]/button"
    sitemapValue = driver.find_element(by=By.XPATH, value=xpathForSitemap).text
    driver.find_element(by=By.XPATH, value=xpathForSitemap).click()
    sleep(1)
    # count number of menu in the sitemap
    numberOfSitemapMenu = len(driver.find_elements(by=By.XPATH, value="//ul[@class='sitemap-menu collapse show']//button"))
    for valueOfSiteMapMenu in range(1, numberOfSitemapMenu+1):
        # expand individual sitemap menu item
        xpathForSitemapMenu = "(//ul[@class='sitemap-menu collapse show']//button)[" + str(valueOfSiteMapMenu) + "]"
        sitemapMenuValue = driver.find_element(by=By.XPATH, value=xpathForSitemapMenu).text
        xpathForSitemapMenuCompanies = "(//ul[@class='sitemap-menu collapse show']//button)[" + str(valueOfSiteMapMenu) + "]/following-sibling::a"
        # click on the list of companies
        driver.find_element(by=By.XPATH, value=xpathForSitemapMenuCompanies).click()
        # switch to new window
        driver.switch_to.window(driver.window_handles[-1])
        sleep(2)
        pageURL = driver.current_url
        # click on last page
        driver.find_element(by=By.XPATH, value="//li[@class='page-item last']/a").click()
        sleep(4)
        # get last page number
        lastPageNumber = driver.find_element(by=By.XPATH, value="//li[@class='page-item active']/a").text
        for currentPageNumber in range(0, int(lastPageNumber)): # Tested with 2 pages of iteration for currentPageNumber in range(0, 2):
            currentPageURL = pageURL+"?page="+str(currentPageNumber)
            driver.get(currentPageURL)
            sleep(4)
            numberOfCompaniesInPage = len(
                driver.find_elements(by=By.XPATH, value="//li[contains(@class,'provider provider-row')]"))
            for companyNumber in range(1, numberOfCompaniesInPage+1):
                companyNameXpath = "(//li[contains(@class,'provider provider-row')])["+str(companyNumber)+"]//h3"
                websiteXpath = "(//li[contains(@class,'provider provider-row')])["+str(companyNumber)+"]//a[@class='website-link__item']"
                locationXpath = "(//li[contains(@class,'provider provider-row')])["+str(companyNumber)+"]//span[@class='locality']"
                ratingXpath = "(//li[contains(@class,'provider provider-row')])["+str(companyNumber)+"]//span[@class='rating sg-rating__number']"
                reviewCountXpath = "(//li[contains(@class,'provider provider-row')])["+str(companyNumber)+"]//a[@class='reviews-link sg-rating__reviews']"
                hourlyRateXpath = "(//li[contains(@class,'provider provider-row')])["+str(companyNumber)+"]//i[@class='list_icon icon_clock']/../../span"
                minProjectSizeXpath = "(//li[contains(@class,'provider provider-row')])["+str(companyNumber)+"]//i[@class='list_icon icon_tag']/../../span"
                employeeSizeXpath = "(//li[contains(@class,'provider provider-row')])["+str(companyNumber)+"]//i[@class='list_icon icon_person']/../../span"
                try:
                    companyNameValue = driver.find_element(by=By.XPATH, value=companyNameXpath).text
                    companyNameValue = companyNameValue.replace(",", "")
                except NoSuchElementException:
                    companyNameValue = "Not Available"
                try:
                    hrefValueFull = driver.find_element(by=By.XPATH, value=websiteXpath).get_attribute("href")
                    hrefValue, sep, tail = hrefValueFull.partition('?utm_')
                except NoSuchElementException:
                    hrefValue = "Not Available"
                try:
                    locationValue = driver.find_element(by=By.XPATH, value=locationXpath).text
                    locationValue = locationValue.replace(",", "")
                except NoSuchElementException:
                    locationValue = "Not Available"
                try:
                    ratingValue = driver.find_element(by=By.XPATH, value=ratingXpath).text
                except NoSuchElementException:
                    ratingValue = "Not Available"
                try:
                    reviewCountValue = driver.find_element(by=By.XPATH, value=reviewCountXpath).text
                except NoSuchElementException:
                    reviewCountValue = "Not Available"
                try:
                    hourlyRateValue = driver.find_element(by=By.XPATH, value=hourlyRateXpath).text
                    hourlyRateValue = hourlyRateValue.replace(",", "")
                except NoSuchElementException:
                    hourlyRateValue = "Not Available"
                try:
                    minProjectSizeValue = driver.find_element(by=By.XPATH, value=minProjectSizeXpath).text
                    minProjectSizeValue = minProjectSizeValue.replace(",", "")
                except NoSuchElementException:
                    minProjectSizeValue = "Not Available"
                try:
                    employeeSizeValue = driver.find_element(by=By.XPATH, value=employeeSizeXpath).text
                    employeeSizeValue = employeeSizeValue.replace(",", "")
                    employeeSizeValue = employeeSizeValue + " employees"
                except NoSuchElementException:
                    employeeSizeValue = "Not Available"
                print(sitemapValue+","+sitemapMenuValue+","+companyNameValue+","+hrefValue+","+locationValue+","+ratingValue+","+reviewCountValue+","+hourlyRateValue+","+minProjectSizeValue+","+employeeSizeValue)
                file.write(sitemapValue+","+sitemapMenuValue+","+companyNameValue+","+hrefValue+","+locationValue+","+ratingValue+","+reviewCountValue+","+hourlyRateValue+","+minProjectSizeValue+","+employeeSizeValue + '\n')
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
    driver.find_element(by=By.XPATH, value=xpathForSitemap).click()
    sleep(1)
driver.close()
# close the file
file.close()