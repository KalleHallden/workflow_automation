import wget
from selenium import webdriver
from twitter_poster import post_to_twitter
from selenium.webdriver.chrome.options import Options

chrome_options = Options()  
chrome_options.add_argument("--headless") 
browser = webdriver.Chrome(chrome_options=chrome_options)
url = "https://www.youtube.com/c/KalleHallden/videos"

browser.get(url)
video = browser.find_element_by_xpath('//*[@id="video-title"]')
video_title = str(video.text)
F = open('titles.txt', 'r')
past_title = F.readline()

if past_title == video_title:
	print("Don't post")
else: 
	video.click()

	video_url = str(browser.current_url)
	video_id = video_url.split("=", 1)[1]
	thumbnailurl = 'https://img.youtube.com/vi/' + video_id + '/maxresdefault.jpg'
	thumbnail = wget.download(thumbnailurl)
	image_path = 'maxresdefault.jpg'
	post_to_twitter(image_path, video_title, video_url)
	F = open('titles.txt', 'w')
	F.write(video_title)
