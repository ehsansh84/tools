if $1 == "install"
echo "EHSAN"
fi
scp -P 3031 $1 root@ehsanshirzadi.com:/volumes/html/cdn
echo https://cdn.ehsanshirzadi.com/$1
