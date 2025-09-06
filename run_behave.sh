#!/bin/bash
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

echo "Running Behave tests..."
behave features/BookAPI.feature --no-capture --no-capture-stderr --show-timings -f pretty
