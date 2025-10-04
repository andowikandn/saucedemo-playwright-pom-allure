
### Overview

A brief project does and who it's for Web automation testing saucedemo services till end to end.


### Tools

- Playwright
- Python
- Pytest
- Allure Report

### Installation

First of all create your folder project, makesure already installed Python, and Allure.

Create virtual environment
```bash
python3 -m venv env_name
```
    
Activation virtual environment
```bash
source env_name/bin/activate
```

Install Selenium
```bash
pip3 install playwright
playwright install
```

Install Pytest+Allure
```bash
pip3 allure-pytest
```

Makesure already installed
```bash
pip3 list
```
Output:
```bash
allure-pytest         2.15.0
pytest                8.4.2
playwright            1.55.0
```

### How to Run

```bash
pytest
allure serve reports
```
