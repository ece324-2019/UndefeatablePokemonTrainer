from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pickle
import time
import os
import getpass

username = "UndefeatableNN"
password = "feedforward"

# Looks for word in logs
# Inputs: logs (list of dictionaries)
#		  word (str)
def find_in_log(logs, word):
	for log in logs:
		# print (log)
		if word in log["message"]:
			return 1
	return 0

# Gets opponent's pokemon name
def get_opp_pokemon(logs):
	for log in logs:
		if find_in_log([log], "p2a"):
			opp = log["message"].split('\\n')[4].split('|')[3].split(',')[0]
			# If p1 is opponent
			if opp != "Haxorus":
				return opp
			# p2 is opponent
			return log["message"].split('\\n')[5].split('|')[3].split(',')[0]
	return 0

# TODO: Start timer every battle
# clear console and read it periodically to see if repeat
def main():
    # Enables browser logging
	d = DesiredCapabilities.CHROME
	d['goog:loggingPrefs'] = {'browser': 'ALL'}

	browser = webdriver.Chrome(get_chromedriver_path(), desired_capabilities=d)
	open_pokemon_showdown(browser)
	login(browser, username, password)
	play_game(browser)
	create_team(browser)
	start_battle(browser)

	opponent = 0
	# while battle has not ended
	while (not browser.find_elements_by_name("closeAndMainMenu")):

		if (not opponent):
			time.sleep(1)
			logs = browser.get_log('browser')

			# Finds opponent's pokemon
			opponent = get_opp_pokemon(logs)
			if opponent:
				print ("opponent is ", opponent)
			continue

		# Wait for chooseMove to come up
		if (browser.find_elements_by_name("chooseMove") == []):
			time.sleep(1)
			continue

		# Makes desired move
		make_move(browser, "Outrage")

	# print ("done")

    # prints browser log
	# for entry in browser.get_log('browser'):
	# 	print(entry)


def get_chromedriver_path():
	your_os = os.name
	if your_os == "posix":
		username = getpass.getuser()
		return("/Users/" + username + "/PycharmProjects/chromedriver_win32")
	if your_os == "nt":
		return ("C:/Users/martyn wei/PycharmProjects/chromedriver_win32/chromedriver")

# Enters Pokemon Showdown Website
def open_pokemon_showdown(browser):
	browser.get('https://pokemonshowdown.com/') # open the website
	time.sleep(2)
	browser.find_element_by_class_name("mainbutton").click() # play online
	time.sleep(2)

# Logins to Pokemon Showdown
def login(browser, username, password):
	browser.find_element_by_name("login").click() # choose name
	time.sleep(1)
	browser.find_element_by_name("username").send_keys(username)
	time.sleep(1)
	browser.find_element_by_xpath("/html/body/div[4]/div/form/p[2]/button[1]").click()  # submit username
	time.sleep(1)
	browser.find_element_by_name("password").send_keys(password)
	time.sleep(1)
	browser.find_element_by_name("password").send_keys(Keys.RETURN)
	time.sleep(1)

# Creates pokemon team
def create_team(driver):
	driver.find_element_by_name("joinRoom").click()
	driver.find_element_by_name("newTop").click()
	driver.find_element_by_xpath(
		"(.//*[normalize-space(text()) and normalize-space(.)='you have no pokemon lol'])[1]/following::button[1]").click()
	driver.find_element_by_xpath(
		"(.//*[normalize-space(text()) and normalize-space(.)='Save'])[1]/following::textarea[1]").clear()
	driver.find_element_by_xpath(
		"(.//*[normalize-space(text()) and normalize-space(.)='Save'])[1]/following::textarea[1]").send_keys(
		"Haxorus @ Choice Scarf  \nAbility: Mold Breaker  \nEVs: 252 Atk / 4 SpD / 252 Spe  \n- Outrage  \n- Iron Tail  \n- Rock Slide  \n- Superpower  \n\nSwampert-Mega @ Swampertite  \nAbility: Swift Swim  \nEVs: 4 HP / 252 Atk / 252 Spe  \n- Hydro Pump  \n- Earthquake  \n- Rest  \n- Protect  \n\nWobbuffet @ Assault Vest  \nAbility: Shadow Tag  \nEVs: 252 HP / 252 Def / 4 SpD  \nIVs: 0 Atk  \n- Destiny Bond  \n- Counter  \n- Charm  \n- Encore")
	driver.find_element_by_xpath(
		"(.//*[normalize-space(text()) and normalize-space(.)='Import/Export'])[1]/following::button[1]").click()
	driver.find_element_by_xpath(
		"(.//*[normalize-space(text()) and normalize-space(.)='Format:'])[2]/following::button[1]").click()
	driver.find_element_by_xpath(
		"(.//*[normalize-space(text()) and normalize-space(.)='Anything Goes'])[2]/following::button[1]").click()
	driver.find_element_by_xpath(
		"(.//*[normalize-space(text()) and normalize-space(.)='Home'])[1]/preceding::i[1]").click()

# Starts battle and chooses Haxorus
def start_battle(driver):
	driver.find_element_by_name("format").click()
	driver.find_element_by_xpath(
		"(.//*[normalize-space(text()) and normalize-space(.)='Anything Goes'])[2]/following::button[1]").click()
	driver.find_element_by_xpath(
		"(.//*[normalize-space(text()) and normalize-space(.)='wobbuffet'])[1]/following::strong[1]").click()
	while(driver.find_elements_by_name("chooseTeamPreview") == []):
		time.sleep(1)
	driver.find_element_by_name("chooseTeamPreview").click()

# Makes the desired move
def make_move(driver, move):
    if move == "Outrage":
        driver.find_element_by_name("chooseMove").click()
    elif move == "Iron Tail":
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Dragon'])[1]/following::button[1]").click()
    elif move == "Rock Slide":
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Steel'])[1]/following::button[1]").click()
    elif move == "Superpower":
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Rock'])[1]/following::button[1]").click()
    else:
        print ("Invalid Move!")
    time.sleep(1)

def play_game(browser):
	browser.find_element_by_xpath("//*[@id=\"room-\"]/div/div[1]/div[2]/div[1]/form/p[1]/button").click() # select battle type
	# time.sleep(2)
	browser.find_element_by_xpath("/html/body/div[4]/ul[1]/li[14]/button").click() # choose 1v1
	# time.sleep(2)

if __name__ == "__main__":
	main()
