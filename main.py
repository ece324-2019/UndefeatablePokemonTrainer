from selenium import webdriver
import time
import os
import getpass

username = "UndefeatableNN"
password = "feedforward"


def main():
	browser = webdriver.Chrome(get_chromedriver_path())
	open_pokemon_showdown(browser)
	login(browser, username, password)
	play_game(browser)


def get_chromedriver_path():
	your_os = os.name
	if your_os == "posix":
		username = getpass.getuser()
		return("/Users/" + username + "/Downloads/chromedriver")
	if your_os == "nt":
		return ""

def open_pokemon_showdown(browser):
	browser.get('https://pokemonshowdown.com/') # open the website
	time.sleep(2)
	browser.find_element_by_class_name("mainbutton").click() # play online
	time.sleep(2)

def login(browser, username, password):
	browser.find_element_by_xpath("//*[@id=\"header\"]/div[3]/button[1]").click() # choose name
	time.sleep(2)
	browser.find_element_by_xpath("/html/body/div[4]/div/form/p[1]/label/input").send_keys(username)
	time.sleep(2)
	browser.find_element_by_xpath("/html/body/div[4]/div/form/p[2]/button[1]").click() #submit username
	time.sleep(2)
	browser.find_element_by_xpath("/html/body/div[4]/div/form/p[4]/label/input").send_keys(password)
	time.sleep(2)
	browser.find_element_by_xpath("/html/body/div[4]/div/form/p[5]/button[1]").click() #submit password
	time.sleep(2)

# def create_team(browser):

def play_game(browser):
	browser.find_element_by_xpath("//*[@id=\"room-\"]/div/div[1]/div[2]/div[1]/form/p[1]/button").click() # select battle type
	time.sleep(2)
	browser.find_element_by_xpath("/html/body/div[4]/ul[1]/li[14]/button").click() # choose 1v1
	time.sleep(5)


main()


'''def setup_team():

def find_match():





time.sleep(1)
time.sleep(1)
browser.find_element_by_xpath("/html/body/div[4]/div/form/p[5]/button[1]/strong").click()
time.sleep(2)
browser.find_element_by_xpath("//*[@id=\"room-\"]/div/div[1]/div[2]/div[1]/form/p[3]/button").click()
'''
