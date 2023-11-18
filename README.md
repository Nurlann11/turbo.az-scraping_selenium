# Premium Ads Scraper

This Python script is designed to scrape premium car advertisements from Turbo.az using Selenium and Firefox WebDriver.

## Requirements

- Python 3.x
- Selenium
- GeckoDriver (Firefox WebDriver)

### Installation

1. Clone or download this repository to your computer.

2. Install the required Python libraries using the following command:

    ```bash
    pip install -r requirements.txt
    ```

   Note: Make sure you have Firefox installed on your machine.

## Usage

1. Set up the necessary paths and configurations in the script:

    - Update the path to the GeckoDriver in the `Service('./geckodriver.exe')` line.
    - Uncomment and update the ChromeDriver line if you prefer using Chrome.
    - Adjust the scrolling parameters and any other settings as needed.

2. Run the script in the terminal or command prompt:

    ```bash
    python script_name.py
    ```

   Note: Replace `script_name.py` with the actual name of your Python script.

3. The script will open Turbo.az, scroll down slowly, and collect information on premium car ads.

4. The collected data will be saved in a JSON file named 'PREMIUM_ADS_cars.json' in the script's directory.

## Notes

- Make sure you have the necessary web drivers (GeckoDriver or ChromeDriver) installed.
- Adjust the waiting times and scrolling parameters based on your internet speed and system performance.

Feel free to customize the script and contribute to its improvement. Happy coding!
