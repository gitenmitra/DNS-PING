# DNS-PING
Way find out if DNS is down or your instance
<br><br>
<b>Problem:</B> At times it happens that DNS provider services of a website URL is down and so to reduce response time by not diagnosing the infrastructure and informing the user to check with DNS provider.
<br><br>
<b>Functionality:</b> Lambda in python pings the URL to be monitored and fetch the response. If the response code is anything other than 200 it triggers CloudWatch event and send SNS to user.<br><br>

<b>Architecture diagram</B><br><br>
<img src="https://github.com/gitenmitra/AWS/blob/main/DNS-PING.jpg?raw=true" alt="Architecture diagram" style="border:5px solid black">
