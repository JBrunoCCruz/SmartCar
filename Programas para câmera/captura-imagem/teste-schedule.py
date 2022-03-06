Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import schedule
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import schedule
ModuleNotFoundError: No module named 'schedule'
>>> import schedule
>>> import time
>>> def job():
	print("I'm working")

	
>>> schedule.every(1).minutes.do(job)
Every 1 minute do job() (last run: [never], next run: 2020-08-05 12:00:47)
>>> while True:
	schedule.run_pending()
	time.sleep(1)

	
I'm working
