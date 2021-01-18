#!/bin/sh
set -o noglob
#Correct
echo "*******************************************************************"
echo "Test Case: OK"
echo "./your-program  '*/15 0 1,15 * 1-5 /usr/bin/find'"
./your-program  "*/15 0 1,15 * 1-5 /usr/bin/find"
echo "Outcome should be:"
echo "minute        0 15 30 45"
echo "hour          0"
echo "day of month  1 15"
echo "month         1 2 3 4 5 6 7 8 9 10 11 12"
echo "day of week   1 2 3 4 5"
echo "command       /usr/bin/find"
echo "\n"
#Second Case
echo "*******************************************************************"
echo "Test Case: OK"
echo "./your-program  '1-45/15 2-23 1-5 * 1-5 /usr/bin/find'"
./your-program  "1-45/15 2-23 1-5 * 1-5 /usr/bin/find"
echo "\n"
echo "Outcome should be:"
echo "minute        1 16 31"
echo "hour          2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22"
echo "day of month  1 2 3 4"
echo "month         1 2 3 4 5 6 7 8 9 10 11 12"
echo "day of week   1 2 3 4 5"
echo "command       /usr/bin/find"
echo "\n"
#Third Case
echo "*******************************************************************"
echo "Test Case: Error - Wrong minutes"
echo "./your-program  '1-75/15 2-23 1-5 * 1-5 /usr/bin/find'"
./your-program  '1-75/15 2-23 1-5 * 1-5 /usr/bin/find'
echo "\n"
echo "Outcome should be:"
echo "minute        E r r o r"
echo "hour          2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22"
echo "day of month  1 2 3 4"
echo "month         1 2 3 4 5 6 7 8 9 10 11 12"
echo "day of week   1 2 3 4 5"
echo "command       /usr/bin/find"
echo "\n"
#Four Case
echo "*******************************************************************"
echo "Test Case: Error - Missing input parameters"
echo "./your-program  '1-75/15 2-23 1-5 * 1-5'"
./your-program  "1-75/15 2-23 1-5 * 1-5"
echo "Outcome should be:"
echo "Error - Missing input parameters"
echo "\n"
#Fifth Case
echo "*******************************************************************"
echo "Test Case: Error - wrong Hour"
echo "./your-program  '1-75/15 2-23 1-5 * 1-5'"
./your-program  "1-45/15 2-43 1-5 * 1-5 /usr/bin/find"
echo "Outcome should be:"
echo "minute        1 16 31"
echo "hour          E r r o r"
echo "month         1 2 3 4 5 6 7 8 9 10 11 12"
echo "day of week   1 2 3 4 5"
echo "command       /usr/bin/find"
echo "\n"
#Sixth Case
echo "*******************************************************************"
echo "Test Case: Error - wrong month"
echo "./your-program  '1-75/15 2-23 1-5 * 1-5'"
./your-program  "1-75/15 2-23 1-5 * 1-5"
echo "Outcome should be:"
echo "Error missing input parameters"
echo "\n"
set +o noglob