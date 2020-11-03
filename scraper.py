import wget
from selenium import webdriver
from twitter_poster import post_to_twitter
from selenium.webdriver.chrome.options import Options 
import json
import datetime
import os
import os.path
from instagram_poster import instagram_post


chrome_options = Options()  
chrome_options.add_argument("--headless") 
browser = webdriver.Chrome(chrome_options=chrome_options)
url = "https://www.youtube.com/c/KalleHallden/videos"

browser.get(url)
video = browser.find_element_by_xpath('//*[@id="video-title"]')
video_title = str(video.text)
with open('data.json','r') as f:
	data=json.load(f)
	past_title = data["title"]

if past_title == video_title:
	print("Don't post")
	l_updated=data["last_updated"]
	print("Last updated was " + l_updated)
else: 
	video.click()

	video_link = str(browser.current_url)
	video_id = video_link.split("=", 1)[1]
	thumbnailurl = 'https://img.youtube.com/vi/' + video_id + '/maxresdefault.jpg'
	thumbnail = wget.download(thumbnailurl)
	image_path = 'maxresdefault.jpg'

	while True:
		print("Do you want to post to Instagram? Y/N")
		insta_input = str(input())
		insta_input = insta_input.lower()
		if insta_input != 'n' or 'y':
			print("NOOO")
			continue
		else:
			break
	
	while True:
		print("Do you want to post to Twitter? Y/N")
		twitter_input = str(input())
		twitter_input = twitter_input.lower()
		if twitter_input != 'n' or 'y':
			continue
		else:
			break

	if insta_input == 'y':
		instagram_post(image_path, video_title)
	if twitter_input == 'y':
		post_to_twitter(image_path, video_title, video_link)

	# move image into folder
	working_dir = os.getcwd()
	old_path = os.path.join(working_dir, image_path)
	new_path = os.path.join(working_dir + "\Photos", video_title)
	os.rename(old_path, new_path)

	data["title"]=video_title
	data["last_updated"]=str(datetime.date.today())
	with open("data.json","w") as f:
		json.dump(data,f)
