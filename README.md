# Message generator app
This app automates the process for generating messages to share voucher codes for certification exams. Simply select the message you want to generate from the dropdown menu and paste the URL of your batch's
instructor comments sheet. Finally, select the **first** assigned test date on the calendar widget.

Messages are returned one at a time in Slack-formatted text. Simply use the copy button and paste into private messages to your students. *Be aware* that this app is not aware of nicknames or preferred use of second/third/family names. In these cases, please edit the message in Slack before sending.

Because the Sheets being read are restricted, this application does rely on secrets to work. For this reason, forking the repo to work on changes will require you to receive a copy of the secrets. Please reach out if you want to contribute.
