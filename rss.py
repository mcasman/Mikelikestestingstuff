#!/usr/bin/env python
import sys, feedparser
def main():

    username = raw_input("Please enter google or facebook to continue: ")

    if username not in set (['google','Google','facebook','Facebook']):
        print("\n" + "Non authorized feed, please try again." + "\n")
        username = raw_input("Please enter it again: ")

    else:
        if username in set (['google','Google']):
            gfeed = feedparser.parse("http://planetcallofduty.gamespy.com/show_rss.php")
            print len(gfeed.entries)
            for i in range(0, 4):
                print "\n" + gfeed.entries[i].title + "\n"
                print gfeed.entries[i].link
                print gfeed.entries[i].description
                print i
            loadmore = raw_input("Cool, want some more?")
            if loadmore in set(['yes','Yes']):
                for i in range(4, 9):
                    print gfeed.entries[i].link
                    print i
            else:
                print "OK. Thanks for playing!"
        if username in set (['facebook','Facebook']):
            ffeed = feedparser.parse("http://www.minecraftforum.net/rss/writ/1-news/")
            print len(ffeed.entries)
            for i in range(0, 4):
                print "\n" + ffeed.entries[i].title + "\n"
                print ffeed.entries[i].link
                print ffeed.entries[i].description    
                print i
            loadmore = raw_input("Nice, want some more?")
            if loadmore in set(['yes', 'Yes']):
                for i in range(4, 9):
                    print ffeed.entries[i].link
                    print i
            else:
                print"OK. Thanks for playing!"
main()
