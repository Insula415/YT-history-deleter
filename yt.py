#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from time import sleep
from selenium import webdriver
from secrets import *

class YTbot:
    def __init__(self, email, pw):
        try:
            num = int(input("How many Youtube videos do you want to delete from your history? "))
            print("Starting")
        except:
            print("Error, input a sensible integer")


        self.driver = webdriver.Chrome()
        self.email = email
        self.driver.get("https://www.youtube.com/") #going to URL
        sleep(2)

        self.driver.find_element_by_xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-button-renderer/a/paper-button/yt-formatted-string")\
        .click() #signin
        self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")\
        .send_keys(email) #logging in email
        sleep(0.5)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]")\
        .click() #enter
        sleep(0.5)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")\
        .send_keys(pw) #logging in password
        sleep(0.5)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]")\
        .click() #enter
        sleep(1)
        self.driver.get("https://www.youtube.com/feed/history") #going to YouTube history
        sleep(2)

        ##deleting videos
        count = 0
        anothcount = 1
        while num > count:
            self.driver.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/div/ytd-menu-renderer/div/ytd-button-renderer/a/yt-icon-button/button/yt-icon")\
            .click()
            self.driver.get("https://www.youtube.com/feed/history")
            sleep(1)
            print("Successfully deleted",anothcount)
            sleep(0.5)
            count += 1
            anothcount += 1
        print("Finished")






YTbot(email, pw)
