#! /usr/bin/env bash

./encryptor.py s2.py
cp licensed.py ~/.local/bin/holzcraftsadmin.py
sudo chattr -i ~/key.txt
cp key.txt ~/key.txt
sudo chattr +i ~/key.txt

sudo chattr -i ~/settings.cfg
cp settings.cfg ~/settings.cfg
sudo chattr +i ~/settings.cfg

git add . 
git commit -am "added new tool options"
git push
