
import instaloader
ig=instaloader.Instaloader()
dp=input("Enter Instagram Username: ")
ig.download_profile(dp,profile_pic_only=True)
