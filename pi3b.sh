sudo pkill fbi
sudo pkill mplayer
rm ./Content/v*/samplescreen*
python create_content.py $1
sudo python screen_update.py $2 $3 $4 $5 $6 $7
echo "Job done! and I am awesome!"
