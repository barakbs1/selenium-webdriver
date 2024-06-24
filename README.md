# selenium-webdriver

These selenium-webdriver tests run against https://stephenchou1017.github.io/scheduler react-based scheduler app. Test module can be found in: `main.py`.

### run selenium
1. Pull the selenium standalone docker image: `docker pull selenium/standalone-chrome`
2. Run the image in docker container: `docker run -d -p 4444:4444 -p 7900:7900 --shm-size="2g" selenium/standalone-chrome:latest`

### Setup test
1. Get test code from: https://github.com/barakbs1/selenium-webdriver
2. Install dependencies (preferably use python 3.12 and virtual environment): `pip install -r requirements.txt`
3. Activate virtual environment (if used), navigate to project root and run: `python main.py`
