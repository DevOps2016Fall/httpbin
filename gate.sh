#!/usr/bin/env bash
while read line
do
    temp=$line
    t=${temp:1:5}
    error=10
    if [ "$t" == "error" ];then
        if [  "${temp:13:2}" -gt "$error" ]; then
          echo "Static analysis errors violation is higher than " $error "."
          echo "Commit Failed!"
          exit 1
        fi
    fi
    conventions=${temp:1:10}
    conv=100
    if [ "$conventions" == "convention" ];then
       if [  "${temp:13:3}" -gt "$conv" ]; then
          echo "Static analysis convetion violation is higher than " $conv "."
          echo "Commit Failed!"
          exit 1
        fi
    fi
done < pylint.out



while read line
do
    temp=$line
    t=${temp:26:9}
    coverage=0.70
    if [ "$t" == "line-rate" ]; then
#        if (( $(echo "$num1 > $num2" |bc -l) ))
          if (($(echo "${temp:37:5} < $coverage"|bc -l ))); then
          echo "Average code coverate is less than " $coverage "."
          echo "Commit Failed!"
          exit 1
        fi
    fi
done < coverage.xml