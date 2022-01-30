from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium
import time
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager



def al_results(start, end):
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.get("https://www.doenets.lk/examresults")
    driver.set_window_size(500, 1000)
    exam = driver.find_element(by="xpath", value="/html/body/app-root/div/app-layout-horizontal-sidenav/div/div/div/div/div/app-exam-results-container/app-exam-results/div[1]/div/div[2]/div[2]/div[1]/div/div[1]/div/select")
    exam.send_keys("G.C.E. (A/L)")
    exam.send_keys(Keys.ENTER)

    yr = driver.find_element(by="xpath", value="/html/body/app-root/div/app-layout-horizontal-sidenav/div/div/div/div/div/app-exam-results-container/app-exam-results/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div/select")
    yr.send_keys("2020")
    yr.send_keys(Keys.ENTER)
    for i in range(start, end):

        index = driver.find_element(by="xpath", value="/html/body/app-root/div/app-layout-horizontal-sidenav/div/div/div/div/div/app-exam-results-container/app-exam-results/div[1]/div/div[2]/div[2]/div[2]/div/div/input")
        if i != start:
            index.send_keys(Keys.CONTROL, "a")
        index.send_keys(i)
        index.send_keys(Keys.ENTER)
        time.sleep(0.6)
        try:
            driver.find_element(by="xpath", value="/html/body/app-root/div/app-layout-horizontal-sidenav/div/div/div/div/div/app-exam-results-container/app-exam-results/div[1]/div/div[2]/div[5]/div/div").click()

        except selenium.common.exceptions.NoSuchElementException or selenium.common.exceptions.InvalidArgumentException:
            print(i)
        else:
            try:
                name = driver.find_element(by="xpath", value="/html/body/app-root/div/app-layout-horizontal-sidenav/div/div/div/div/div/app-exam-results-container/app-exam-results/div[1]/div/div[2]/div[5]/div/div/div[3]/div[2]/div[4]/div/div[2]").text
            except selenium.common.exceptions.NoSuchElementException or selenium.common.exceptions.StaleElementReferenceException:
                name = "Not Given"
                pass
            try:
                ind = driver.find_element(by="xpath", value="/html/body/app-root/div/app-layout-horizontal-sidenav/div/div/div/div/div/app-exam-results-container/app-exam-results/div[1]/div/div[2]/div[5]/div/div/div[3]/div[2]/div[5]/div/div[2]").text
            except selenium.common.exceptions.NoSuchElementException or selenium.common.exceptions.StaleElementReferenceException:
                ind = "Not Given"
                pass
            try:
                nic = driver.find_element(by="xpath", value="/html/body/app-root/div/app-layout-horizontal-sidenav/div/div/div/div/div/app-exam-results-container/app-exam-results/div[1]/div/div[2]/div[5]/div/div/div[3]/div[2]/div[6]/div/div[2]").text
            except selenium.common.exceptions.NoSuchElementException or selenium.common.exceptions.StaleElementReferenceException:
                nic = "Not Given"
                pass
            try:
                sub1 = driver.find_element(by="xpath", value="/html/body/app-root/div/app-layout-horizontal-sidenav/div/div/div/div/div/app-exam-results-container/app-exam-results/div[1]/div/div[2]/div[5]/div/div/div[3]/div[3]/div[1]/div[2]").text
            except selenium.common.exceptions.NoSuchElementException or selenium.common.exceptions.StaleElementReferenceException:
                sub1 = "Not Given"
                pass
            try:
                sub2 = driver.find_element(by="xpath", value="/html/body/app-root/div/app-layout-horizontal-sidenav/div/div/div/div/div/app-exam-results-container/app-exam-results/div[1]/div/div[2]/div[5]/div/div/div[3]/div[3]/div[2]/div[2]").text
            except selenium.common.exceptions.NoSuchElementException or selenium.common.exceptions.StaleElementReferenceException:
                sub2 = "Not Given"
                pass
            try:
                sub3 = driver.find_element(by="xpath", value="/html/body/app-root/div/app-layout-horizontal-sidenav/div/div/div/div/div/app-exam-results-container/app-exam-results/div[1]/div/div[2]/div[5]/div/div/div[3]/div[3]/div[3]/div[2]").text
            except selenium.common.exceptions.NoSuchElementException or selenium.common.exceptions.StaleElementReferenceException:
                sub3 = "Not Given"
                pass
            try:
                sub4 = driver.find_element(by="xpath", value="/html/body/app-root/div/app-layout-horizontal-sidenav/div/div/div/div/div/app-exam-results-container/app-exam-results/div[1]/div/div[2]/div[5]/div/div/div[3]/div[3]/div[4]/div[2]").text
            except selenium.common.exceptions.NoSuchElementException or selenium.common.exceptions.StaleElementReferenceException:
                sub4 = "Not Given"
                pass
            try:
                sub5 = driver.find_element(by="xpath", value="/html/body/app-root/div/app-layout-horizontal-sidenav/div/div/div/div/div/app-exam-results-container/app-exam-results/div[1]/div/div[2]/div[5]/div/div/div[3]/div[3]/div[5]/div[2]").text
            except selenium.common.exceptions.NoSuchElementException or selenium.common.exceptions.StaleElementReferenceException:
                sub5 = "Not Given"
                pass
            try:
                sub1_r = driver.find_element(by="xpath", value="/html/body/app-root/div/app-layout-horizontal-sidenav/div/div/div/div/div/app-exam-results-container/app-exam-results/div[1]/div/div[2]/div[5]/div/div/div[3]/div[3]/div[1]/div[3]").text
            except selenium.common.exceptions.NoSuchElementException or selenium.common.exceptions.StaleElementReferenceException:
                sub1_r = "Not Given"
                pass
            try:
                sub2_r = driver.find_element(by="xpath", value="/html/body/app-root/div/app-layout-horizontal-sidenav/div/div/div/div/div/app-exam-results-container/app-exam-results/div[1]/div/div[2]/div[5]/div/div/div[3]/div[3]/div[2]/div[3]").text
            except selenium.common.exceptions.NoSuchElementException or selenium.common.exceptions.StaleElementReferenceException:
                sub2_r = "Not Given"
                pass
            try:
                sub3_r = driver.find_element(by="xpath", value="/html/body/app-root/div/app-layout-horizontal-sidenav/div/div/div/div/div/app-exam-results-container/app-exam-results/div[1]/div/div[2]/div[5]/div/div/div[3]/div[3]/div[3]/div[3]").text
            except selenium.common.exceptions.NoSuchElementException or selenium.common.exceptions.StaleElementReferenceException:
                sub3_r = "Not Given"
                pass
            try:
                sub4_r = driver.find_element(by="xpath", value="/html/body/app-root/div/app-layout-horizontal-sidenav/div/div/div/div/div/app-exam-results-container/app-exam-results/div[1]/div/div[2]/div[5]/div/div/div[3]/div[3]/div[4]/div[3]").text
            except selenium.common.exceptions.NoSuchElementException or selenium.common.exceptions.StaleElementReferenceException:
                sub4_r = "Not Given"
                pass
            try:
                sub5_r = driver.find_element(by="xpath", value="/html/body/app-root/div/app-layout-horizontal-sidenav/div/div/div/div/div/app-exam-results-container/app-exam-results/div[1]/div/div[2]/div[5]/div/div/div[3]/div[3]/div[5]/div[3]").text
            except selenium.common.exceptions.NoSuchElementException or selenium.common.exceptions.StaleElementReferenceException:
                sub5_r = "Not Given"
                pass
            l = [len("Name"), len("Index No"), len("Nic"), len(sub1), len(sub2), len(sub3), len(sub4), len(sub5)]
            m = max(l)

            f = open(f"./{start}-{end}.txt", "a")
            f.write(f"""
Name{(m - len("Name")) * " "} : {name}
Index No{(m - len("Index No")) * " "} : {ind}
Nic{(m - len("Nic")) * " "} : {nic}
{sub1}{(m - len(sub1)) * " "} : {sub1_r}
{sub2}{(m - len(sub2)) * " "} : {sub2_r}
{sub3}{(m - len(sub3)) * " "} : {sub3_r}
{sub4}{(m - len(sub4)) * " "} : {sub4_r}
{sub5}{(m - len(sub5)) * " "} : {sub5_r}
""")

            print(name, nic)


print("Please Enter the range of index numbers")
start = int(input("From : "))
end = int(input("To   : "))
print(" ")
while (end < start) or (len(str(start)) != 7) or (len(str(end)) != 7):
    if end < start:
        print("Please enter a valid range")
    if (len(str(start)) != 7):
        print(f"length of index number should be 7, but {len(str(start))} given")
    if (len(str(end)) != 7):
        print(f"length of index number should be 7, but {len(str(end))} given")

    start = int(input("From : "))
    end = int(input("To   : "))
    print(" ")

al_results(start, end)
