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
git push https://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@github.com/0rion-HunterShield/Home2Bar_Qt-DRM-Tools

