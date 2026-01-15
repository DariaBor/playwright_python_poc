#!/bin/bash

# Playwright Python Test Runner Script

echo "======================================"
echo "Playwright Python Test Framework"
echo "======================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    exit 1
fi

echo "Python version:"
python3 --version
echo ""

# Check if pip is installed
if ! command -v pip &> /dev/null && ! command -v pip3 &> /dev/null; then
    echo "ERROR: pip is not installed"
    exit 1
fi

# Install dependencies if needed
echo "Installing/Updating dependencies"
pip install -q -r requirements.txt
echo "Dependencies installed"
echo ""

# Install Playwright browsers if needed
echo "Ensuring Playwright browsers are installed"
python3 -m playwright install chromium
echo "Browsers ready"
echo ""

# Run tests
echo "Execute tests"
echo "======================================"
python3 -m pytest tests/test_twitch_search_and_stream.py -v -s
TEST_RESULT=$?
echo "======================================"
echo ""

if [ $TEST_RESULT -eq 0 ]; then
    echo "Test run completed successfully!"
    echo ""
    echo "Screenshots saved in: screenshots/"
else
    echo "Test run failed with exit code: $TEST_RESULT"
fi

exit $TEST_RESULT
