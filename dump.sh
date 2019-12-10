#!/bin/bash
### BEGIN INIT INFO
# Provides:          bbzhh.com
# Required-Start:    $local_fs $network
# Required-Stop:     $local_fs
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: tomcat service
# Description:       tomcat service daemon
### END INIT INFO
cd /home/abbipc/ads-b
sudo /home/abbipc/ads-b/dump1090 --device-index 0 --net-http-port 80 --interactive --net 1>/dev/null 2>/dev/null &
python2 /home/abbipc/ads-b/save_data.py 