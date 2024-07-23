from selenium import webdriver
import time

def play(video_title):
    driver = webdriver.Chrome()  # You need to have Chrome WebDriver installed
    driver.get("https://www.youtube.com/")
    time.sleep(2)  # Allow time for page to load
    search_box = driver.find_element_by_name("search_query")
    search_box.send_keys(video_title)
    search_box.submit()
    time.sleep(2)  # Allow time for search results to load
    videos = driver.find_elements_by_css_selector("ytd-video-renderer")
    if videos:
        first_video = videos[0]
        first_video.click()
    else:
        print("No videos found")
    time.sleep(5)  # Allow time for video to start playing
    driver.quit()
