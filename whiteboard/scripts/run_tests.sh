#!/bin/sh
set -e

# We have to explicitly change into this directory, or else tests break on Jenkins
# as it sets the working directory to an obscure directory instead of /deploy/code
cd /deploy/code

# There is a .coveragerc file which contains exclusions as well as output directory configuration 
echo "Running backend tests"
pytest --durations=10 --cov=whiteboard --cov-report html:./test-coverage --cov-report xml:./test-coverage/coverage.xml --junitxml=./test-reports/test_report.xml whiteboard/tests

chmod -R 777 /deploy/code/test-coverage
chmod -R 777 /deploy/code/test-reports
