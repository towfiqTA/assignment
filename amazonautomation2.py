from selenium import webdriver
driver = webdriver.Chrome()

def open_url(url):
    driver.get(url)
def search_item(item):
    #entering item in search button
    driver.find_element_by_id("twotabsearchtextbox").send_keys(item)
    #Pressing go button
    driver.find_element_by_xpath("//div[@class='nav-search-submit nav-sprite']//input[@class='nav-input']").click()
def sort_the_list():
    #click on the sort by featured menu
    driver.find_element_by_xpath("//span[@id='a-autoid-0-announce']").click()
    #click on Price High to low
    driver.find_element_by_xpath("//a[@id='s-result-sort-select_2']").click()
def select_second_item():
    driver.find_element_by_xpath("//div[3]//div[1]//div[1]//div[1]//div[2]//div[2]//div[1]//div[1]//div[1]//div[1]//div[1]//h2[1]//a[1]//span[1]").click()
def item_verification(itemForVerification):
    productDetail = driver.find_element_by_id("productTitle").text
    assert itemForVerification in productDetail

if __name__ =="__main__":
    url = "https://www.amazon.com"
    item = "Nikon"
    itemForVerification = "Nikon D3X"
    open_url(url)
    search_item(item)
    sort_the_list()
    select_second_item()
    item_verification(itemForVerification)

