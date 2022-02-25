#! /usr/bin/env bash
#source ~/.zshrc
echo "username: 0rion-HunterShield"
echo "Token: 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"

./encryptor.py s2.py
cp licensed.py ~/.local/bin/holzcraftsadmin.py
sudo chattr -i ~/key.txt
cp key.txt ~/key.txt
sudo chattr +i ~/key.txt

sudo chattr -i ~/settings.cfg
cp settings.cfg ~/settings.cfg
sudo chattr +i ~/settings.cfg
