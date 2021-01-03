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

containerName=$(echo $TAG | cut -d'-' -f2)

sudo docker rm -f $(sudo docker ps -aq)
echo "removed"
sudo docker run -d -p 5000:5000 --name $containerName $TAG
echo "run"
sleep 5
for city in 'Modiin' 'Moscow'; do
  echo $city
  curl -s -X POST --header "Content-Type: application/json" --data '{"city":"'$city'"}' http://localhost:5000 | grep $city
  check_result $city

#RUN="sudo docker run $TAG"
##sudo docker run $TAG | grep "lon"
#for city in 'Modiin' 'Moscow'; do
#  $RUN -c $city | grep $city
#  check_result "city_name $city"
#  $RUN -c $city | grep "lon"
#  check_result "$city longitude"
#  $RUN -c $city | grep "weather"
#  check_result "$city weather"

done

exit 0

