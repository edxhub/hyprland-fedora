#!/bin/bash
##################################################################################################################
# Author 	: 	Erik Dubois
# Website 	: 	https://www.erikdubois.be
# Website	:	https://www.arcolinux.com
# Website	:	https://www.arcolinuxd.com
##################################################################################################################
#
#   DO NOT JUST RUN THIS. EXAMINE AND JUDGE. RUN AT YOUR OWN RISK.
#
##################################################################################################################

# checking if I have the latest files from github
#echo "Checking for newer files online first"
#git pull

# Below command will backup everything inside the project folder
git add --all .

# Give a comment to the commit if you want
printf "\e[1;34m####################################\e[0m\n"
printf "\e[1;34mWrite your commit comment!\e[0m\n"
printf "\e[1;34m####################################\e[0m\n"

echo -n 'Commit: ' && read input

echo
# Committing to the local repository with a message containing the time details and commit text

git commit -m "$input"

# Push the local files to github

git push

echo
printf "\e[1;32m################################################################\e[0m\n"
printf "\e[1;32m###################    Git Push Done      ######################\e[0m\n"
printf "\e[1;32m################################################################\e[0m\n"
