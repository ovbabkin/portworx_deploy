import string
import sys
import json

#f0 = sys.argv[1]
#f1 = open(f0, "r")
#f2 = f1.read()
f2 = sys.stdin.read()
f3 = f2.replace('}\n{','},\n{')
f4 = '['+f3+']'
f5 = json.loads(f4)
i=0
total_iops=0
total_bw=0
total_runtime=0
total_io=0
for f6 in f5:
  i=i+1
  total_iops+=int(round(f6['jobs'][0]['write']['iops'])+round(f6['jobs'][0]['read']['iops']))
  total_bw+=int(round(f6['jobs'][0]['write']['bw_bytes']/1024/1024)+round(f6['jobs'][0]['read']['bw_bytes']/1024/1024))
  total_runtime+=int(round(f6['jobs'][0]['write']['runtime']/1000)+round(f6['jobs'][0]['read']['runtime']/1000))
  total_io+=int(round(f6['jobs'][0]['write']['io_bytes']/1024/1024)+round(f6['jobs'][0]['read']['io_bytes']/1024/1024))
#  print('Job: '+str(i)+ '|iops = ' +str(total_iops)+',BW = ' +str(total_bw)+',Runtime = '+str(total_runtime)+',IO = '+str(total_io))
print(str(total_iops)+','+str(total_bw)+' MB,'+str(total_runtime)+' sec,'+str(total_io)+' MB')
