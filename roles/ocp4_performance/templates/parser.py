import string
import sys
import json

#f2 = sys.stdin.read()
with open(sys.argv[1], 'r') as f2:
  f3 = f2.read().replace('}\n{','},\n{')
f4 = '['+f3+']'
f5 = json.loads(f4)
total_iops = 0
total_bw = 0
#total_runtime = 0
total_io = 0
#runtime = 0
for f6 in f5:
  total_iops+=int(round(f6['jobs'][0]['write']['iops'])+round(f6['jobs'][0]['read']['iops']))
  total_bw+=int(round(f6['jobs'][0]['write']['bw_bytes']/1024/1024)+round(f6['jobs'][0]['read']['bw_bytes']/1024/1024))
#  runtime=int(round(f6['jobs'][0]['write']['runtime']/1000)+round(f6['jobs'][0]['read']['runtime']/1000))
#  if runtime > total_runtime:
#     total_runtime = runtime
  total_io+=int(round(f6['jobs'][0]['write']['io_bytes']/1024/1024)+round(f6['jobs'][0]['read']['io_bytes']/1024/1024))

print(str(total_iops)+','+str(total_bw)+' MB,'+str(total_io)+' MB')
