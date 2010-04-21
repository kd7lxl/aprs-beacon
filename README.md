# aprs-beacon.py

aprs-beacon.py will send an APRS packet to the APRS-IS. It is designed to be run once, or on a schedule via an external scheduling program like cron.

## Configuration

Before using aprs-beacon.py you will need to edit aprs-beacon.py to add your callsign, passcode, and APRS packet. The APRS packet payload should be entered as you would for the BTEXT in a TNC2.

## Usage

To run the program once, open a terminal and change to the aprs-beacon directory. Then type:

    python aprs-beacon.py

To run aprs-beacon.py on a schedule, add something similar to the following to your crontab:

    */2 * * * * /usr/bin/python /home/tom/src/aprs-beacon/aprs-beacon.py # executes aprs-beacon.py twice every hour