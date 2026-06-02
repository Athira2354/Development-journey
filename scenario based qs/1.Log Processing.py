# You are given a list of logs:
# logs = ["ERROR: Disk full", "INFO: User login", "ERROR: Timeout", "INFO: Logout"]
# Task: Count how many times each log level appears and return a dictionary.
logs=["ERROR: Disk full", "INFO: User login", "ERROR: Timeout", "INFO: Logout"]
result={}
for log in logs:
    level=log.split(":")[0]
    result[level]=result.get(level,0)+1
print(result)