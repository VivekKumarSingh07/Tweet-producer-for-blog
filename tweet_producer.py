def setup_tweet(categories, hashtags):
    link = input("Please Enter the link :")
    category = int(input("Enter the category (1/2):"))
    hashtag = categories[category]
    print(hashtags[hashtag])
    print(link)


if __name__ == "__main__":
    leetcode_hashtag_list = ['leetcode', 'leetcoder', 'blog', 'blogger']
    ctf_hashtag_list = ['hacking', 'hack', 'ctf', 'hustle', 'hackingculture', 'blog', 'blogger']

    categories = {1: "Leetcode", 2: "Capture the flag"}
    hashtags = {"Leetcode": leetcode_hashtag_list, "Capture the Flag": ctf_hashtag_list}
    setup_tweet(categories, hashtags)    