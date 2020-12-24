#!/bin/bash
check_result() {
  RESULT=$?
  MESSAGE1=$1
  MESSAGE2=$2
  if [ $RESULT == 0 ]; then
    echo [ SUCCESS ] $MESSAGE1 $MESSAGE2
  else
    echo [ FAIL ] $MESSAGE1 $MESSAGE2
    exit 1
  fi
}

for city in 'Modiin' 'Moscow'; do
 sudo docker run mypythonproject -c $city | grep "lon"
 check_result $city lontitude
 sudo docker run mypythonproject -c $city | grep "weather"
 check_result $city weather
done

exit 0