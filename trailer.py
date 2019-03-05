import mediafile

import fresh_tomatoes

bahubali2=mediafile.Tollytrailers("Bahubali:The Conclusion","Revenge Drama",
                                  "https://static.toiimg.com/photo/58344058.cms",
                                  "https://www.youtube.com/watch?v=qD-6d8Wo3do")
bharath=mediafile.Tollytrailers("Bharath ane nenu","Political Drama",
                                "https://i.ndtvimg.com/i/2018-04/mahesh-babu-instagram_650x400_61524999284.jpg",
                                "https://www.youtube.com/watch?v=orkPrGSAETs")
robo2=mediafile.Tollytrailers("Robo 2.0","Scientific Action",
                             "https://i.ytimg.com/vi/2wvq8hdGdAw/maxresdefault.jpg",
                             "https://www.youtube.com/watch?v=2wvq8hdGdAw")
mersal=mediafile.Tollytrailers("Mersal","Awareness of GST",
                               "https://img.theweek.in/content/dam/week/news/entertainment/2017/september/mersal.jpg",
                               "https://www.youtube.com/watch?v=gQDo5QuZTaw")
kaala=mediafile.Tollytrailers("Kaala","Gangster Action",
                             "https://i.ytimg.com/vi/PDaJIlTrIyU/maxresdefault.jpg",
                             "https://www.youtube.com/watch?v=mMCEvr3VWqQ")
vivegam=mediafile.Tollytrailers("Vivegam","Thriller",
                                "https://www.ssmusic.tv/wp-content/uploads/2017/08/vivegam_moview_review.jpg",
                                "https://www.youtube.com/watch?v=2FhI6gzT_m8")
movies=[bahubali2,bharath,robo2,mersal,kaala,vivegam]
fresh_tomatoes.open_movies_page(movies)
