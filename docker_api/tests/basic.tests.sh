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


RUN="sudo docker run $TAG"
#sudo docker run $TAG | grep "lon"
for city in 'Modiin' 'Moscow'; do
  $RUN -c $city | grep $city
  check_result "city_name $city"
  $RUN -c $city | grep "lon"
  check_result "$city longitude"
  $RUN -c $city | grep "weather"
  check_result "$city weather"

done

exit 0

