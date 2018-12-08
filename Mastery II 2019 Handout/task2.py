# Problem 2: Follow Me Not

class User:
    
    def __init__(self):
        follower = set()
        self.follower = follower
    
    def followedBy(self,that_user):
        if that_user != self:
            self.follower.add(that_user)
            
    def unfollowedBy(self,that_user):
        if that_user in self.follower:
            self.follower.remove(that_user)
        
    def isFollowedBy(self,that_user):
        if that_user in self.follower:
            return True
        return False

userA = User()
userB = User()
userC = User()
assert(userA.isFollowedBy(userB)==False)
userA.followedBy(userB)
userC.followedBy(userB)
userC.followedBy(userB)
userC.followedBy(userB)
userC.followedBy(userB)
assert(userA.isFollowedBy(userB)==True)
assert(userC.isFollowedBy(userB)==True)
assert(userC.isFollowedBy(userA)==False)
userA.unfollowedBy(userB)
assert(userA.isFollowedBy(userB)==False)
assert(userC.isFollowedBy(userB)==True)
assert(userC.isFollowedBy(userA)==False)
userC.unfollowedBy(userB)
assert(userC.isFollowedBy(userB)==False)
assert(userC.isFollowedBy(userA)==False)        
