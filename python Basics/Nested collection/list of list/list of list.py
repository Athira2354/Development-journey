social_media_post=[
                [1,"ajay","good_morning",500,888],
                [2,"vipin","good_evening",100,999],
                [3,"rahul","have a good_daay",499,1200],
                [4,"goutam","hakuna matata",1000,1111],
                [5,"ashna","explore the travel vibes",1000,1111],

            ]
print(social_media_post[2][2])

all_names=[lst[1] for lst in social_media_post]
print(all_names)

all_post=[lst[2] for lst in social_media_post]
print(all_post)

insta_views=[lst[3] for lst in social_media_post ]
print(insta_views)

fb_views=[lst[4] for lst in social_media_post ]
print(fb_views)

insta_views_filter=[lst[1] for lst in social_media_post if lst[3]==1000]
print (insta_views_filter)
fb_views_filter=[lst[1] for lst in social_media_post if lst[4]==1111]
print (fb_views_filter)


max_insta_views=max([lst[3] for lst in social_media_post])
max_views=[lst[1]for lst in social_media_post if lst[3]==max_insta_views]
print(max_insta_views)

min_like_post=max([lst[2]for lst in social_media_post])
min_likes=[lst[1] for lst in social_media_post if lst[4]==min_like_post]

print(min_like_post)
