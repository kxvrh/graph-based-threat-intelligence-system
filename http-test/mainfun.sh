cat 2018-12-03.csv | awk -F ',' '{print $7}'| awk -F '?' '{print $1; system("bash mkpath.sh "$1)}'
bash rmdir.sh
cat 2018-12-03.csv | awk -F ',' '{print $7}'| awk -F '?' '{print $1; system("bash touchfile.sh "$1)}'
