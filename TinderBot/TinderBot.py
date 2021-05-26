from selenium import common
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import messages
from random import seed
from webdriver_manager.chrome import ChromeDriverManager
from random import randint

seed(1)


class TinderBot:

    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

        # Łuki
        self.email = ''
        self.password = ''

        # Martyna
        # self.email = ''
        # self.password = ''
        self.decision_if_match_found = 1
        # just skip 1
        # write message 2

    def log_in(self):
        self.driver.get('https://tinder.com')

        pref_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[2]/button')
        pref_btn.click()

        time.sleep(0.3)
        acc_pref_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div[3]/div[3]/button')
        acc_pref_btn.click()

        log_in_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div['
                                                       '1]/div/div/header/div[1]/div[2]/div/button')
        log_in_btn.click()

        time.sleep(5)
        log_in_with_fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div['
                                                               '3]/span/div[2]/button')
        log_in_with_fb_btn.click()

        # switch to log in popup
        time.sleep(1)
        base_window = self.driver.window_handles[0]
        popup_window = self.driver.window_handles[1]

        self.driver.switch_to.window(popup_window)

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(self.email)

        password_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        password_in.send_keys(self.password)

        final_log_in_btn = self.driver.find_element_by_xpath('//*[@id="loginbutton"]')
        final_log_in_btn.click()

        self.driver.switch_to.window(base_window)

        time.sleep(5)
        allow_loc_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        allow_loc_btn.click()

        deny_notification_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div['
                                                                  '3]/button[2]')
        deny_notification_btn.click()

    def like(self):
        like_btn = self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div['
                                                        '1]/div/div[2]/div[2]/button')
        dislike_btn.click()

    def auto_swipe(self):
        time.sleep(5)
        continue_swapping = True
        swaps = 0
        matches = 0
        try:
            while swaps < 120:
                try:
                    time.sleep(0.5)
                    swaps += 1
                    self.like()

                except common.exceptions.ElementClickInterceptedException:
                    try:
                        try:
                            self.match_found()
                            continue_swapping = False
                            swaps -= 1
                            matches += 1
                        except common.exceptions.NoSuchElementException:
                            self.popup_add_to_home_screen_dismissed()
                    except common.exceptions.NoSuchElementException:
                        self.super_like_user()

        except Exception:
            print('Forced exit ->')

        print('Swaps done = ', swaps, '\nMatched = ', matches)
        time.sleep(5)

    def super_like_user(self):
        not_send_super_like_button = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/button[2]')
        not_send_super_like_button.click()

    def match_found(self):
        # just skip
        if self.decision_if_match_found == 1:
            skip_btn = self.driver.find_element_by_xpath(
                '//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/button')
            skip_btn.click()
        # write message
        if self.decision_if_match_found == 2:
            message_in = self.driver.find_element_by_xpath('//*[@id="chat-text-area"]')
            self.insert_and_send_message(message_in)

            # if method insert_and_send_message is sending msg correctly you can delete code below

            # send_btn = self.driver.find_element_by_xpath(
            #     '//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/div[3]/form/button')
            # send_btn.click()

    def insert_and_send_message(self, message_in):
        # message_in - text field
        # combine_message = messages.pickup_lines[randint(0, 3)]
        combine_message = messages.pickup_lines[6]
        lines = combine_message.split('\n')
        rows = len(lines)
        for i in range(rows):
            line = lines[i]
            message_in.send_keys(line)
            if i == rows - 1:
                continue

            ActionChains(self.driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(
                Keys.ENTER).perform()
        message_in.send_keys(Keys.ENTER)

    def popup_add_to_home_screen_dismissed(self):
        not_interested_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        not_interested_btn.click()

    def message_already_matched(self):
        # message_btn = self.driver.find_element_by_xpath('//*[@id="messages-tab"]')
        # message_btn.click()
        messages_sent = 0
        while True:
            try:
                matches_btn = self.driver.find_element_by_xpath('//*[@id="match-tab"]')
                matches_btn.click()
                time.sleep(1)
                first_match_btn = self.driver.find_element_by_xpath('//*[@id="matchListNoMessages"]/div[1]/div[2]')
                first_match_btn.click()

                message_in = self.driver.find_element_by_xpath('//*[@id="chat-text-area"]')
                self.insert_and_send_message(message_in)
                time.sleep(1)
                messages_sent += 1

            except Exception:
                messages_sent -= 1
                break

        print('Messages sent = ', messages_sent)


bot = TinderBot()

bot.log_in()

# time.sleep(1)
bot.auto_swipe()

