# Clutch Data Scraper
## _Built for Automation interview for GetDefault_

This web scraper is built in Python using Selenium.

## Features
- Code is ready and tested to scrape complete data about all the companies from the website. This has been tested for 9000+ data sets where for each domain 2 pages of data was read, but the code is already in place to read the complete list of data.
- Output taken to CSV which can be formatted to xlsx in less than a minute.
- Error handling done for scenarios where data is not available.
- Pagination handled and all data are taken dynamically i.e., tomorrow if we have new sitemap items or domains then we need not change anything.
- Proper sleep time given for handling page loads.
- Graceful exits of Webdriver and file.
- Edge cases scenarios such as non English characters, extra characters in Company Website etc. all handled.

## Tech

All open sourced tools were used for this:

- [Python](https://www.python.org/) - Python Programming Language
- [Selenium](https://www.selenium.dev/) - Selenium Framework
- [PyCharm](https://www.jetbrains.com/pycharm/) - PyCharm IDE for development


## Installation

This requires [Selenium](https://pypi.org/project/selenium/) dependency on Python to run.

Install the dependencies and then compile the code.

```sh
pip install selenium
```


## License

MIT

**Free Data Scraper for Clutch !!**
