import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

class scrape:
	def init(self):
		pass

	def loadURL(self): 
		chrome_options = webdriver.ChromeOptions()
		chrome_options.add_argument("--disable-notifications")

		self.driver = webdriver.Chrome('chromedriver.exe')
		self.driver.get(URL)
		time.sleep(2)

	def getVideoNames(self):
		self.loadURL()
		elements = self.driver.find_elements_by_xpath('//*[@id="video-title"]')
		VideoNames = ''

		for element in elements:
			VideoNames += element.text + "\n"

		return VideoNames

	def saveToFile(self, URL):
		self.URL = URL 

		VideoNames = self.getVideoNames()
		text_file = open("PlaylistVideoNames.txt", "w")
		n = text_file.write(VideoNames)
		text_file.close()

		self.driver.close()

		print("Video Names Extraction Complete")

if __name__ == '__main__':
	scrapeObj = scrape()
	URL = input("Enter the URL you want to load : ")
	scrapeObj.saveToFile(URL)
