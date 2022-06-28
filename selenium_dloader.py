def dynamic_loading(href):
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium.common.exceptions import TimeoutException
    from selenium.webdriver.chrome.options import Options

    all_hrefs = dict()
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    browser = webdriver.Chrome(
        executable_path= r".\chromedriver.exe",
        options=chrome_options
    )

    browser.get(href)
    delay = 10 # seconds
    try:
        myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'css-1hky5w4')))
        print("Page is ready!")
        #element = browser.find_element_by_css_selector(".css-1hky5w4 .question__25Pw")
        element = browser.find_elements(by=By.CSS_SELECTOR, value=".css-1hky5w4 .question__25Pw .title__1kvt") 
        # print(element)
        
        difficulties = browser.find_elements(by=By.CSS_SELECTOR, value=".question__25Pw .difficulty__ES5S") 
        for i in range(len(element)):
            all_hrefs[element[i].get_attribute("href")] = difficulties[i].get_attribute("innerHTML")
        
        
    except TimeoutException:
        print("Loading took too much time!")

    
    
    browser.quit()
    
    
    return all_hrefs
    

  