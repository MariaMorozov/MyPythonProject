#!/bin/bash
TAG=$1
check_result() {
  RESULT=$?
  MESSAGE=$1

  if [ $RESULT == 0 ]; then
    echo [SUCCESS] $MESSAGE
  else
    echo [FAIL] $MESSAGE
    exit 1
  fi
}

#sudo docker run $TAG | grep "lon"
for city in 'Modiin' 'Moscow'; do
  sudo docker run -c $city | grep "lon"
  check_result $city
  sudo docker run -c $city | grep "weather"
  check_result "weather"
done

exit 0