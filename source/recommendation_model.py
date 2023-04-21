import pandas as pd
from sklearn.cluster import KMeans
import warnings
warnings.filterwarnings('ignore')


class RecommendationModel:
    def __init__(self, user_music):
        # self.user_info = user_info
        self.user_music = user_music

    def recommend_music(self, favourite_music):
        tracks_df = pd.read_csv(
            'D:/Python projects/Music_Player/recommendation_system/spotify_genius_track_dataset/Data '
            'Sources/spotify_tracks.csv')
        tracks_df = tracks_df.drop_duplicates(subset='name')

        kmeans_model = KMeans(n_clusters=5)
        kmeans_model.fit(tracks_df[['danceability', 'instrumentalness', 'energy', 'tempo', 'valence']])

        tracks_df['type'] = kmeans_model.labels_
        tracks_df.to_csv(
            'D:/Python projects/Music_Player/recommendation_system/spotify_genius_track_dataset/Data '
            'Sources/clustered_spotify_tracks.csv')

        favourite_names = favourite_music.strip().split(',')
        ids_names = tracks_df[['name', 'id']].loc[tracks_df['name'].isin(favourite_names)]
        ids = ids_names['id']

        # search the specified ids in this dataset and get the tracks
        favorites = tracks_df[tracks_df.id.isin(ids)]

        # code to sort find out the maximum occurring cluster number according to user's favorite track types
        cluster_numbers = list(favorites['type'])
        clusters = {}
        for num in cluster_numbers:
            clusters[num] = cluster_numbers.count(num)

        # sort the cluster numbers and find out the number which occurs the most
        user_favorite_cluster = [(k, v) for k, v in sorted(clusters.items(), key=lambda item: item[1])][0][0]

        # finally get the tracks of that cluster
        suggestions = tracks_df[tracks_df.type == user_favorite_cluster]
        result_recommendation = suggestions[['name']].loc[suggestions['id'].isin(suggestions['id'].head(n=7))]

        return result_recommendation
