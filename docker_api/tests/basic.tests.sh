#!/bin/bash
#TAG=$1
check_result() {
  RESULT=$?
  MESSAGE=$1
18.223.184.126
  if [ $RESULT == 0 ]; then
    echo [SUCCESS] $MESSAGE
  else
    echo [FAIL] $MESSAGE
    exit 1
  fi
}

for city in 'Modiin' 'Moscow'; do
 sudo docker run --city $city | grep "lon"
 check_result $city
 sudo docker run --city $city | grep "weather"
 check_result $city
done

exit 0