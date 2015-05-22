#!/usr/bin/python

'''
 This file is part of SlackIt

 Copyright(c) 2015 Gabriele Salvatori
 http://www.salvatorigabriele.com
 salvatorigabriele@gmail.com

 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

from notify import *
from slack_connect import *
from daemon import Daemon
import time


class Start(Daemon):

    def run(self):

        while True:

            connect = Connect()
            connect.run_instance()

            notify = Notify()
            notify.run_instance()


            # author = connect.get_last_author_from_history()
            # message = registry["last-message"]


            # notifica.set_notify_author(author)
            # notifica.set_notify_channel("dev")
            # notifica.set_notify_title("You have a new message on")
            # notifica.set_notify_description(message)

            # notifica.run_instance()

            # TODO: use schedule python module instead of sleep function
            time.sleep(check_notification_time)



# start SlackIt to pid
if __name__ == "__main__":
        daemon = Start('/var/run/slackify.pid')
        if len(sys.argv) == 2:
                if 'start' == sys.argv[1]:
                        daemon.start()
                elif 'stop' == sys.argv[1]:
                        daemon.stop()
                elif 'restart' == sys.argv[1]:
                        daemon.restart()
                else:
                        print "Unknown command"
                        sys.exit(2)
                sys.exit(0)
        else:
                print "usage: %s start|stop|restart" % sys.argv[0]
                sys.exit(2)
