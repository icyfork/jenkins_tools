# Simple Python CLI for Jenkins
## Python cli with two sub commands to:
- List all jobs with name contain a keyword:
	Ex: ./cli find report
	-> result: - auto_clear_request_report_queue
             - auto_report_aging_daily
- Trigger build for a specific job
	Ex: ./cli build auto_clear_request_report_queue
	-> result: jenkins job build link