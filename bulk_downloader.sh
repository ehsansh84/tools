# This script reads download links a file names dl.txt, 1 link in each line
for i in $(cat dl.txt);
do 
echo $i 
wget "${i}"
done

