#!/bin/python
# 
# Copyright 2010 Tom Hayward KD7LXL <tom@tomh.us>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from socket import *

# APRS-IS login info
serverHost = 'rotate.aprs2.net'
serverPort = 14580
aprsUser = 'NOCALL-PY'
aprsPass = '00000'

# APRS packet
callsign = 'NOCALL'
btext = ''

# create socket & connect to server
sSock = socket(AF_INET, SOCK_STREAM)
sSock.connect((serverHost, serverPort))
# logon
sSock.send('user %s pass %s vers KD7LXL-Python 0.1\n' % (aprsUser, aprsPass) )
# send packet
sSock.send('%s>APRS:%s\n' % (callsign, status) )
# close socket
sSock.shutdown(0)
sSock.close()
