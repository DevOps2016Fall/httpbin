#!/usr/bin/env bash
while read line
do
    temp=$line
    t=${temp:1:5}
    error=0
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


#
#while read line
#do
#    temp=$line
#    t=${temp:26:9}
#    coverage=75
#    if [ "$t" == "line-rate" ]; then
#        x=${temp:37:5}
#        echo $x*1000 |bc
#        if [ "${temp:37:5}*1000|" -lt "$coverage" ]; then
#        echo "Average code coverate is less than " $coverage "."
#        echo "Commit Failed!"
#        exit 1
#        fi
#    fi
#done < coverage.xml