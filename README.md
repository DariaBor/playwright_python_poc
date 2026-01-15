# Playwright Python Test Framework - Twitch Automation

This project contains an automated test suite for Twitch.tv using Playwright with Python, running on a mobile device emulator (Google Chrome Mobile - Pixel 5).

## Test Flow

The main test (`test_twitch_search_and_stream.py`) performs the following steps:

1. **Open Twitch.tv** - Navigate to https://www.twitch.tv
2. **Go to Browse tab** - Locate and click Browse tab
3. **Search StarCraft II** - Enter "StarCraft II" in the search field
4. **Scroll Down 2 Times** - Scroll through search results
5. **Select a Streamer** - Click on the streamer from results
6. **Wait for Load & Screenshot** - Wait for streamer page to fully load and capture screenshot

## Requirements

- Python 3.8+
- pip (Python package manager)
- Playwright browsers (installed via playwright)

## Installation

1. **Clone/Navigate to the project directory**

   ```bash
   cd /Users/dariaborshchik/playwright_python_poc
   ```

2. **Install dependencies**

   ```bash
   pip3 install -r requirements.txt
   ```

3. **Install Playwright browsers**
   ```bash
   python3 -m playwright install
   ```

## Running Tests

### Run all tests

```bash
python3 -m pytest
```

### Run specific test with verbose output

```bash
python3 -m pytest tests/test_twitch_search_and_stream.py -v -s
```

### Run using provided script

```bash
chmod +x run_tests.sh
./run_tests.sh
```

## Mobile Device Configuration

The tests run using a Google Chrome Mobile Emulator configured as:

- **Device**: Pixel 5
- **Viewport**: 393 x 851 pixels
- **Device Scale Factor**: 1.75
- **Touch**: Enabled
- **User Agent**: Mobile Chrome

This configuration can be modified in `config.py` under the `MOBILE_DEVICE` dictionary.

## Screenshot Outputs

Screenshots are saved in the `screenshots/` directory with timestamps.

Default screenshot: `streamer_page_mobile.png`

![floww](https://github.com/user-attachments/assets/337d6d67-a99e-466c-8b0a-60ed712826cd)

