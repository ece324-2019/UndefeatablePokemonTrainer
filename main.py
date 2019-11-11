from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pickle
import time
import os
import getpass

username = "UndefeatableNN"
password = "feedforward"


def main():
    # Enables browser logging
	d = DesiredCapabilities.CHROME
	d['goog:loggingPrefs'] = {'browser': 'ALL'}

	browser = webdriver.Chrome(get_chromedriver_path(), desired_capabilities=d)
	open_pokemon_showdown(browser)
	login(browser, username, password)
	play_game(browser)
	create_team(browser)
    # prints browser log
	for entry in browser.get_log('browser'):
		print(entry)


def get_chromedriver_path():
	# your_os = os.name
	return ("C:/Users/martyn wei/PycharmProjects/chromedriver_win32/chromedriver")
	# if your_os == "posix":
	# 	username = getpass.getuser()
	# 	return("/Users/" + username + "/PycharmProjects/chromedriver_win32")
	# if your_os == "nt":
	# 	return ""

def open_pokemon_showdown(browser):
	browser.get('https://pokemonshowdown.com/') # open the website
	time.sleep(2)
	browser.find_element_by_class_name("mainbutton").click() # play online
	time.sleep(2)

def login(browser, username, password):
	# browser.find_element_by_xpath("//*[@id=\"header\"]/div[3]/button[1]").click() # choose name
	# time.sleep(2)
	# browser.find_element_by_xpath("/html/body/div[4]/div/form/p[1]/label/input").send_keys(username)
	# time.sleep(2)
	# browser.find_element_by_xpath("/html/body/div[4]/div/form/p[2]/button[1]").click() #submit username
	# time.sleep(2)
	# browser.find_element_by_xpath("/html/body/div[4]/div/form/p[4]/label/input").send_keys(password)
	# time.sleep(2)
	# browser.find_element_by_xpath("/html/body/div[4]/div/form/p[5]/button[1]").click() #submit password
	# time.sleep(2)
	browser.find_element_by_name("login").click() # choose name
	time.sleep(1)
	browser.find_element_by_name("username").send_keys(username)
	time.sleep(1)
	browser.find_element_by_xpath("/html/body/div[4]/div/form/p[2]/button[1]").click()  # submit username
	time.sleep(1)
	browser.find_element_by_name("password").send_keys(password)
	time.sleep(1)
	# browser.find_element_by_xpath("/html/body/div[4]/div/form/p[5]/button[1]").click() #submit password
	browser.find_element_by_name("password").send_keys(Keys.RETURN)
	time.sleep(1)

# Creates pokemon team and starts battle
def create_team(driver):
	driver.find_element_by_name("joinRoom").click()
	driver.find_element_by_name("newTop").click()
	driver.find_element_by_xpath(
		"(.//*[normalize-space(text()) and normalize-space(.)='you have no pokemon lol'])[1]/following::button[1]").click()
	driver.find_element_by_xpath(
		"(.//*[normalize-space(text()) and normalize-space(.)='Save'])[1]/following::textarea[1]").clear()
	driver.find_element_by_xpath(
		"(.//*[normalize-space(text()) and normalize-space(.)='Save'])[1]/following::textarea[1]").send_keys(
		"Charizard-Mega-X @ Charizardite X  \nAbility: Tough Claws  \nEVs: 4 HP / 252 Atk / 252 Spe  \n- Dragon Claw  \n- Fire Fang  \n- Rest  \n- Will-O-Wisp  \n\nSwampert-Mega @ Swampertite  \nAbility: Swift Swim  \nEVs: 4 HP / 252 Atk / 252 Spe  \n- Hydro Pump  \n- Earthquake  \n- Rest  \n- Protect  \n\nWobbuffet @ Assault Vest  \nAbility: Shadow Tag  \nEVs: 252 HP / 252 Def / 4 SpD  \nIVs: 0 Atk  \n- Destiny Bond  \n- Counter  \n- Charm  \n- Encore")
	driver.find_element_by_xpath(
		"(.//*[normalize-space(text()) and normalize-space(.)='Import/Export'])[1]/following::button[1]").click()
	driver.find_element_by_xpath(
		"(.//*[normalize-space(text()) and normalize-space(.)='Format:'])[2]/following::button[1]").click()
	driver.find_element_by_xpath(
		"(.//*[normalize-space(text()) and normalize-space(.)='Anything Goes'])[2]/following::button[1]").click()
	driver.find_element_by_name("validate").click()
	# driver.find_element_by_xpath(
		# u"(.//*[normalize-space(text()) and normalize-space(.)='Add Pokémon'])[1]/following::strong[1]").click()
	driver.find_element_by_name("validate").send_keys(Keys.RETURN)
	driver.find_element_by_xpath(
		"(.//*[normalize-space(text()) and normalize-space(.)='Home'])[1]/preceding::i[1]").click()
	driver.find_element_by_name("format").click()
	driver.find_element_by_xpath(
		"(.//*[normalize-space(text()) and normalize-space(.)='Anything Goes'])[2]/following::button[1]").click()
	driver.find_element_by_xpath(
		"(.//*[normalize-space(text()) and normalize-space(.)='wobbuffet'])[1]/following::strong[1]").click()
	# driver.find_element_by_xpath(
	# 	"(.//*[normalize-space(text()) and normalize-space(.)='Charizard'])[1]/span[1]").click()
	# driver.find_element_by_name("megaevo").click()
	# driver.find_element_by_xpath(
	# 	"(.//*[normalize-space(text()) and normalize-space(.)='Dragon'])[1]/following::button[1]").click()
	# driver.find_element_by_xpath(
	# 	"(.//*[normalize-space(text()) and normalize-space(.)='Dragon'])[1]/following::button[1]").click()

def play_game(browser):
	browser.find_element_by_xpath("//*[@id=\"room-\"]/div/div[1]/div[2]/div[1]/form/p[1]/button").click() # select battle type
	time.sleep(2)
	browser.find_element_by_xpath("/html/body/div[4]/ul[1]/li[14]/button").click() # choose 1v1
	time.sleep(2)


main()


'''def setup_team():

def find_match():





time.sleep(1)
time.sleep(1)
browser.find_element_by_xpath("/html/body/div[4]/div/form/p[5]/button[1]/strong").click()
time.sleep(2)
browser.find_element_by_xpath("//*[@id=\"room-\"]/div/div[1]/div[2]/div[1]/form/p[3]/button").click()
'''
