"""
Question:
Pick one IP from each region, find network latency from via the below code snippet
(ping 3 times), and finally sort the average latency by region.
http://ec2-reachability.amazonaws.com/

Expected Output for all 15 regions:
1. us-west-1 [50.18.56.1] - 100ms (Smallest average latency)
2. xx-xxxx-x [xx.xx.xx.xx] - 200ms
3. xx-xxxx-x [xx.xx.xx.xx] - 300ms
...
15. xx-xxxx-x [xx.xx.xx.xx] - 1000ms (Largest average latency)
"""
import subprocess
import re

host = [("us-east-1","23.23.255.255"),\
("us-east-2","13.58.0.253"),\
("us-west-1","13.56.63.251"),\
("us-west-2","34.208.63.251"),\
("us-gov-west-1","34.208.63.251"),\
("ca-central-1","35.182.0.251"),\
("eu-west-1","34.240.0.253"),\
("eu-central-1","18.194.0.252"),\
("eu-west-2","35.176.0.252"),\
("ap-northeast-1","13.112.63.251"),\
("ap-northeast-2","13.124.63.251"),\
("ap-southeast-1","13.228.0.251"),\
("ap-southeast-2","13.54.63.252"),\
("ap-south-1","13.126.0.252"),\
("sa-east-1","18.231.0.252")]


for x in range(0,15):
	ping = subprocess.Popen(
    	["ping", "-c", "3", host[x][1]],
    	stdout = subprocess.PIPE,
    	stderr = subprocess.PIPE
	)

	out, error = ping.communicate()
	#print (str(out))
	matchObj = re.findall('time=\d+.\d+',str(out))
	matchObj = re.findall('\d+.\d+', str(matchObj))
	average = (float(matchObj[0])+float(matchObj[1])+float(matchObj[2]))/3
	average = float("{0:.2f}".format(average))
	#print(host[x][0],average)
	host[x] = host[x] +(average,)

#print(host)
host = sorted(host,key=lambda ping: ping[2])

print(str(1)+'.',str(host[0][0]),'['+str(host[0][1])+']'+' - '+str(host[0][2])+'ms'+' (Smallest average latency)')

for x in range(1,14):
	print(str(x+1)+'.',str(host[x][0]),'['+str(host[x][1])+']'+' - '+str(host[x][2])+'ms')

print(str(15)+'.',str(host[14][0]),'['+str(host[14][1])+']'+' - '+str(host[14][2])+'ms'+' (Largest average latency)')
