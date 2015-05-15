#!/usr/bin/python

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
                        daemon.run()
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