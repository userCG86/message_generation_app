# Message generator app
This app automates the process for generating messages to share login information for LinkedIn Learning or voucher codes for certification exams. Simply select the message you want to generate from the dropdown menu and paste the relevant URL
* for LinkedIn Learing, use the admissions intake sheet for your batch.
* for certification vouchers, use the instructor comments sheet and select the **first** assigned test date on the calendar widget.

Messages are returned one at a time in formatted Markdown text. Simply copy and paste into private messages to your students. *Be aware* that because app this reads from official documents, it is not aware of nicknames or preferred use of second/third/family names. In these cases, please edit the message in your DM.

Because the Sheets being read are restricted, this application does rely on secrets to work. For this reason, forking the repo to work on changes will require you to receive a copy of the secrets. Please reach out if you want to contribute to the project.
