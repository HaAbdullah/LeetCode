import heapq

class Twitter:
    def __init__(self):
        self.tweets = {}
        self.follows = {}
        self.time = 0
    
    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((tweetId, self.time))
        self.time += 1

    def getNewsFeed(self, userId: int):
        follower_list = self.follows.get(userId, [])
        all_users = [userId] + follower_list
        
        all_tweets = []
        for user in all_users:
            if user in self.tweets:
                all_tweets.extend(self.tweets[user])
        
        # Use heap to get 10 most recent (largest time values)
        # nlargest returns in descending order by default
        top_10 = heapq.nlargest(10, all_tweets, key=lambda x: x[1])
        return [tweet[0] for tweet in top_10]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = []
        if followeeId not in self.follows[followerId]:
            self.follows[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows and followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
# Your Twitter object will be instantiated and called as such:

twitter = Twitter()
twitter.postTweet(1, 5)  # User 1 posts a new tweet (id = 5).
twitter.getNewsFeed(1)   # User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
twitter.follow(1, 2)     # User 1 follows user 2.
twitter.postTweet(2, 6)  # User 2 posts a new tweet (id = 6).
twitter.getNewsFeed(1)   # User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.unfollow(1, 2)   # User 1 unfollows user 2.
twitter.getNewsFeed(1)   # User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.