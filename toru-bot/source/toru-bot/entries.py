#!/usr/bin/python

import datetime

class HourTweet:

    def __init__(self, prev, now):

        if now.hour != prev:
            self.action(now.hour)

    def action(self, hour):

        # ツイートリストの取得


        # ツイートの実行
        print u''.join([u'tweet! ', str(hour), u':00'])


class shout:


class Entries:

    def __init__(self):
        pass

    def cron(self, prev, now):
        hour = HourTweet(prev, now)

if __name__ == '__main__':
    now = datetime.datetime(2013, 1, 1, 16)
    prev = datetime.datetime(2013, 1, 1, 15)
    entries = Entries()
    entries.cron(prev, now)

