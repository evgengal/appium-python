from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'Nexus 5'
#desired_caps['unicodeKeyboard'] = 'true'
#desired_caps['resetKeyboard'] = 'true'
desired_caps['appPackage'] = 'com.mapswithme.maps.pro'
desired_caps['appActivity'] = 'com.mapswithme.maps.DownloadResourcesActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
