#!/bin/bash
check_result() {
  RESULT=$?
  MESSAGE=S1
  if [ $RESULT == 0 ]; then
    echo [ SUCCESS ] $MESSAGE
  else
    echo [ FAIL ] $MESSAGE
    exit 1
  fi
}

for city in 'Modiin' 'Moscow'; do
 sudo docker run mypythonproject -c $city | grep "lon"
 check_result "lon"
 sudo docker run mypythonproject -c $city | grep "weather"
 check_result "weather"
done

exit 0