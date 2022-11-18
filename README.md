# DNS-PING  
Way to find out if DNS is down or your instance
<br><br>
<b>Problem:</B> At times it happens that DNS provider services of a website URL is down and so to reduce response time by not diagnosing the infrastructure and informing the user to check with DNS provider.
<br><br>
<b>Functionality:</b> Lambda in python pings the URL to be monitored and fetch the response. If the response code is anything other than 200 it triggers CloudWatch event and send SNS to user.<br><br>

<b>Architecture diagram</B><br><br>
<img src="https://github.com/gitenmitra/AWS/blob/main/DNS-PING.jpg?raw=true" alt="Architecture diagram" style="border:5px solid black"><br><br>
<b>How to Run the Script :</b>  Create a Lambda function called "DNS-PING" the run-time version Python 3.6 and above by using the attach code. 
Creation of the Lambda function will in turn create CloudWatch Logs groups for its logging.
Lamda can be call every 5 mins or as per your business requirement.
