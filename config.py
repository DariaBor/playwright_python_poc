
BASE_URL = "https://www.twitch.tv"

MOBILE_DEVICE = {
    "user_agent": "Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36",
    "viewport": {"width": 393, "height": 851},
    "device_scale_factor": 1.75,
    "is_mobile": True,
    "has_touch": True,
}

BROWSER_LAUNCH_OPTIONS = {
    "headless": False,  # change if u need
    "slow_mo": 1000,  
    "devtools": False,  
}

SCREENSHOTS_DIR = "screenshots"
