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
  sudo docker run $TAG -c $city | grep "lon"
  check_result "lon"
  sudo docker run $TAG -c $city | grep "weather"
  check_result "weather"
  if [ sudo docker run $TAG -c $city  ['city_name'] = $city ]
  then
  check_result $city
  else
  echo "City name problem"
  fi
done

exit 0

