#!/usr/bin/env python
#google+ id = 118395007763860659363
#google+ rss = http://rss2lj.net/g+/118395007763860659363
#facebook id = 609492035741264
#facebook rss = https://www.facebook.com/feeds/notifications.php?id=100004779697987&viewer=100004779697987&key=AWgQWF1TFQ0oWdf-&format=rss20
import sys, feedparser
def main():
    gfeed = feedparser.parse("http://planetcallofduty.gamespy.com/show_rss.php")
    ffeed = feedparser.parse("http://www.minecraftforum.net/rss/writ/1-news/")

    username = raw_input("Please enter google to continue: ")

    while username != 'google' and username != 'Google' and username != 'facebook' and username != 'Facebook':
        print("\n" + "Non authorized feed, please try again." + "\n")
        username = raw_input("Please enter it again: ")

    if username == 'google' or username == 'Google':
        for i in range(2):
            print "\n" + gfeed.entries[i].title + "\n"
            print gfeed.entries[i].link
            print gfeed.entries[i].description
    if username == 'facebook' or username == 'Facebook':
        for i in range(2):
            print "\n" + ffeed.entries[i].title + "\n"
            print ffeed.entries[i].link
            print ffeed.entries[i].description
main()
#    username = raw_input("Enter a new feed you want. ")
#    elif username == 'facebook':
#        for i in range(3):
#            print "\n" + ffeed.entries[i].title + "\n"
#    print "Thanks for playing!"
#else:
#        username == 'facebook':
#        for i in range(3):
#            print ffeed.entries[i].title + "\n"
#    username = raw_input("Enter a new feed you want. ")
#    if username =='tumblr':
#        for i in range(3):
#           print tfeed.entries[i].title + "\n"
#            username = raw_input("Enter a new feed you want. ")
#print " "
#    for post in rfeed.entries:
#        print rfeed['feed']['title'] + "\n"
#        print rfeed['feed']['summary'] + "\n"
#        print rfeed['feed']['link'] + "\n"