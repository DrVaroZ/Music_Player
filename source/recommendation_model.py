import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances
import numpy as np
import warnings

from new_track_window import NewTrackWindow

warnings.filterwarnings('ignore')


class RecommendationModel:
    def __init__(self, user_music):
        # self.user_info = user_info
        self.user_music = user_music
        self.tracks_df = pd.read_csv(
            'D:/Python projects/Music_Player/recommendation_system/spotify_genius_track_dataset/Data '
            'Sources/augmented_spotify_tracks.csv')
        self.tracks_df = self.tracks_df.drop_duplicates(subset='name')

    def recommend_music(self, favourite_music):
        favourite_names = favourite_music.strip().split(',')

        # self.check_track(favourite_names)

        print(self.tracks_df[['name', 'danceability', 'instrumentalness', 'energy', 'tempo', 'valence']].tail(n=5))
        self.tracks_df.to_csv(
            'D:/Python projects/Music_Player/recommendation_system/spotify_genius_track_dataset/Data '
            'Sources/augmented_spotify_tracks.csv')

        kmeans_model = KMeans(n_clusters=5)
        kmeans_model.fit(self.tracks_df[['danceability', 'instrumentalness', 'energy', 'tempo', 'valence']])

        self.tracks_df['type'] = kmeans_model.labels_
        self.tracks_df.to_csv(
            'D:/Python projects/Music_Player/recommendation_system/spotify_genius_track_dataset/Data '
            'Sources/clustered_spotify_tracks.csv')

        ids_names = self.tracks_df[['name', 'id', 'type']].loc[self.tracks_df['name'].isin(favourite_names)]
        # print(ids_names)
        ids = ids_names['id']

        # search the specified ids in this dataset and get the tracks
        favorites = self.tracks_df[self.tracks_df.id.isin(ids)]

        # code to sort find out the maximum occurring cluster number according to user's favorite track types
        cluster_numbers = list(favorites['type'])
        clusters = {}
        for num in cluster_numbers:
            clusters[num] = cluster_numbers.count(num)

        # print(clusters)

        # sort the cluster numbers and find out the number which occurs the most
        user_favorite_cluster = [(k, v) for k, v in sorted(clusters.items(), key=lambda item: item[1])][len(clusters.items()) - 1][0]

        # finally get the tracks of that cluster
        # suggestions = tracks_df[tracks_df.type == user_favorite_cluster]
        # result_recommendation = suggestions[['name']].loc[suggestions['id'].isin(suggestions['id'].head(n=7))]

        distances = pairwise_distances(kmeans_model.cluster_centers_, self.tracks_df[
            ['danceability', 'instrumentalness', 'energy', 'tempo', 'valence']], metric='euclidean')
        ind = [np.argpartition(i, 5)[:5] for i in distances]
        closest = [self.tracks_df[['name', 'id', 'type']].iloc[indexes] for indexes in ind]
        # print(closest[user_favorite_cluster])
        closest_df = pd.DataFrame(closest[user_favorite_cluster], columns=['name', 'id'])
        result_recommendation = closest_df['name'].values.tolist()
        # print(closest_df)
        # print(result_recommendation)

        return result_recommendation
