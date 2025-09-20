import pandas as pd
# 1

df = {
    "CustomerId": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "FirstName": ["Ali", "Vali", "Hasan", "Husan", "Dilshod", 
                  "Madina", "Aziza", "Sardor", "Javlon", "Zarina"],
    "LastName": ["Karimov", "Olimov", "Rustamov", "Qodirov", "Shukurov", 
                 "Yuldasheva", "Sobirova", "Abdullayev", "Niyozov", "Toshpulatova"],
    "Country": ["Uzbekistan", "Kazakhstan", "USA", "UK", "Canada", 
                "Uzbekistan", "Russia", "Germany", "France", "Italy"],
    "TotalSpent": [120.50, 340.00, 560.75, 220.10, 410.60, 
                   150.30, 300.00, 475.25, 510.80, 280.45]
}

df = pd.DataFrame(df)


top5_customers = df.sort_values(by="TotalSpent", ascending=False).head(5)

# 2

purchases = {
    "CustomerId": [1, 1, 2, 2, 2, 3, 4, 4, 5],
    "AlbumId":    [101, 101, 101, 101, 102, 102, 103, 103, 104],
    "TrackId":    [1, 2,   1, 2, 3,   1,   1, 2,   1]
}

df_purchases = pd.DataFrame(purchases)


album_tracks = {
    101: 2,  
    102: 3,   
    103: 2,  
    104: 1}


customer_album = df_purchases.groupby(["CustomerId", "AlbumId"])["TrackId"].nunique().reset_index(name="BoughtTracks")


customer_album["TotalTracks"] = customer_album["AlbumId"].map(album_tracks)

customer_album["Type"] = customer_album.apply(
    lambda x: "Full Album" if x["BoughtTracks"] == x["TotalTracks"] else "Individual Tracks", axis=1)


customer_pref = customer_album.groupby("CustomerId")["Type"].first().reset_index()


summary = customer_pref["Type"].value_counts(normalize=True) * 100



