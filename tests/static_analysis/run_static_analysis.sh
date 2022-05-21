#!/bin/bash

result=0

echo "=== black ==="
black --diff --check .
result=$(($result + $?))

echo "=== isort ==="
isort -c --diff .
result=$(($result + $?))

echo "=== flake8 ==="
flake8 .
result=$(($result + $?))

echo "=== mypy ==="
python -m mypy .
result=$(($result + $?))

echo "=== check all imports are absolute ==="
relative_path_number=$( grep -rnE "from \..*import" src/ | wc -l | tr -d ' ' )
relative_paths=$(grep -rnE "from \..*import" src/)
echo "relative_path_number=${relative_path_number}"
echo "relative_paths=[${relative_paths}]"
result=$(($result + $relative_path_number))

echo "static-analysis result: ${result}"
exit $result
