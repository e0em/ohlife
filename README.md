# ohlife
Ohlife 停運後自己架設的版本，需要自己有一台主機並有Sendmail作為email 接受 的STMP 主機
marty.cmd 郵件信箱收到信後 後續的分析與存檔
## Sendmail Config:
1. add marty.cmd: "|/etc/mail/smrsh/python3.ohlife /home/marty/github/ohlife/sendmail_pipe.py" in /etc/aliases
2. $sudo newaliase
3. $sudo ln -s /home/marty/miniconda3/envs/ohlife/bin/python /etc/mail/smrsh/python3.ohlife
email 從前日記的一則給自己，
## Crontab Config:
crontab -e
add 6 19 * * * /home/marty/miniconda3/envs/ohlife/bin/python /home/marty/github/ohlife/emailduo3.py
