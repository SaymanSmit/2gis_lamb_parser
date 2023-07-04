from selenium import webdriver
from selenium.webdriver.chrome.options import Options
opts = Options()
opts.add_argument("user-agent=whatever you want")

driver = webdriver.Chrome(chrome_options=opts)
