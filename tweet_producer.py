import random


phrase1 = ["My latest blog post on ", " I just wrote a blog post on ", "Have you checked my last blog post on ", "My blog post on ", " I just wrote on ", "Did you guys checked my post on ", "Check my post on ", "Hello World my blog post on ", "Hey guys I wrote on ", "Check this blog post out. Its on " ]
phrase3 = ["Show some love", "Can use your opinions", "Feedback please", "Please look into it", "Hope you all will like", "See you soon", "Feedbacks?", "More coming soon",  "Can use some support", "Give it a read"]
hashtag_list = {"Leetcode" : ['leetcode', 'leetcoder', 'blog', 'blogger'], "Capture the flag": ['hacking', 'hack', 'ctf', 'hustle', 'hackingculture', 'blog', 'blogger']}


def setup_tweet(category):
    # link = input("Please Enter the link :")
    # category = int(input("Enter the category (1/2):"))
    # title = input("Enter the title:")
    link = "www.google.com"
    title = "Dummy" #Change the title everytime
    tweet = phrase1[random.randint(0,9)] + title + " " + str(link) + " " + phrase3[random.randint(0,9)]
    for hashtag in hashtag_list[category]:
        tweet = tweet + " #" + hashtag 
    print(len(tweet))
    return tweet



if __name__ == "__main__":
    categories = {1: "Leetcode", 2: "Capture the flag"}
    f = open("tweet_file.txt", "w")
    category = int(input("Enter the category (1/2):"))
    for i in range(10):
        f.write(setup_tweet(categories[category]) + '\n')
    f.close() 