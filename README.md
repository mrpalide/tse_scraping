## TSE Scraping
Let's get data from Tehran Stock Exchange. [tsetmc.com](tsetmc.com)

### Requirements
All required python packages are included in requirement.txt and just install them by **pip**

```
pip install -r requirement.txt
```

Also for selenium that used here to get data, you must have installed *chromedrive* and *google chrome* on your system.

You can use following commands to install them on any debian-based linux distributions. 

<sub>Note: use google to find installation guide for your os.</sub>

#### Installing Google Chrome

```
sudo curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
sudo echo "deb [arch=amd64]  http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
sudo apt-get -y update
sudo apt-get -y install google-chrome-stable
```

#### Installing ChromeDriver
```
wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/bin/chromedriver
sudo chown root:root /usr/bin/chromedriver
sudo chmod +x /usr/bin/chromedriver
```

Path of google-chrome-stable and chromedriver used in selenium configuration in code, that located in ```/usr/bin/``` as default.

### Usage

To run the script, you should run ``` python main.py ``` and get data and create a csv file with updated informations of Tehran Securities Exchange.

You can edit **main.py** file to store data to any arbitrary db that you use in your project instead create csv.
