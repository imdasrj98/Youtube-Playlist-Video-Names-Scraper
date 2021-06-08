import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from datetime import datetime

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
		self.elements = self.driver.find_elements_by_xpath('//*[@id="video-title"]')
		VideoNames = []

		for element in self.elements:
			VideoNames.append(element.text)

		return VideoNames

	def getVideoUploadDates(self):
		videoLinks = []

		for element in self.elements:
		    videoLinks.append(element.get_attribute('href'))

		videoUploadDates = []

		for videoLink in videoLinks:
		    self.driver.get(videoLink)
		    time.sleep(2)
		    
		    videoUploadDates.append(str(datetime.strptime(self.driver.find_element_by_xpath('//*[@id="date"]/yt-formatted-string').text, '%b %d, %Y')))

		return videoUploadDates

	def getVideoNamesSortedByUploadDate(self):
		VideoNames = self.getVideoNames()
		VideoUploadDates = self.getVideoUploadDates()

		videoNamesSortedByUploadDate = []

		for i in range(len(VideoNames)):
			videoNamesSortedByUploadDate.append([VideoUploadDates[i], VideoNames[i]])

		videoNamesSortedByUploadDate = sorted(videoNamesSortedByUploadDate, key=lambda x: x[0])

		videos = ''
		for videoNameSortedByUploadDate in videoNamesSortedByUploadDate:
			videos += videoNameSortedByUploadDate[1] + '\n'

		return videos


	def saveToFile(self, URL):
		self.URL = URL 

		videos = self.getVideoNamesSortedByUploadDate()
		text_file = open("PlaylistVideoNames.txt", "w")
		n = text_file.write(videos)
		text_file.close()

		self.driver.close()

		print("Video Names Extraction Complete")

if __name__ == '__main__':
	scrapeObj = scrape()
	URL = input("Enter the URL you want to load : ")
	scrapeObj.saveToFile(URL)
