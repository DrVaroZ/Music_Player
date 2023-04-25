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

    def recommend_music(self, favourite_music):
        tracks_df = pd.read_csv(
            'D:/Python projects/Music_Player/recommendation_system/spotify_genius_track_dataset/Data '
            'Sources/augmented_spotify_tracks.csv')
        tracks_df = tracks_df.drop_duplicates(subset='name')

        favourite_names = favourite_music.strip().split(',')

        for name in favourite_names:
            if name in tracks_df['name'].values:
                continue
            else:
                new = NewTrackWindow(name)
                new.wait_window()  # wait for the window to be destroyed
                features = new.features  # get the entered features from the window
                if features is not None:
                    favourite_df = pd.DataFrame(
                        {'name': [name],
                         'danceability': [features['danceability']],
                         'energy': [features['energy']],
                         'instrumentalness': [features['instrumentalness']],
                         'tempo': [features['tempo']],
                         'valence': [features['valence']]}
                    )
                    tracks_df = tracks_df.append(favourite_df, ignore_index=True)

        print(tracks_df[['name', 'danceability', 'instrumentalness', 'energy', 'tempo', 'valence']].tail(n=5))
        tracks_df.to_csv(
            'D:/Python projects/Music_Player/recommendation_system/spotify_genius_track_dataset/Data '
            'Sources/augmented_spotify_tracks.csv')

        kmeans_model = KMeans(n_clusters=5)
        kmeans_model.fit(tracks_df[['danceability', 'instrumentalness', 'energy', 'tempo', 'valence']])

        tracks_df['type'] = kmeans_model.labels_
        tracks_df.to_csv(
            'D:/Python projects/Music_Player/recommendation_system/spotify_genius_track_dataset/Data '
            'Sources/clustered_spotify_tracks.csv')

        ids_names = tracks_df[['name', 'id', 'type']].loc[tracks_df['name'].isin(favourite_names)]
        # print(ids_names)
        ids = ids_names['id']

        # search the specified ids in this dataset and get the tracks
        favorites = tracks_df[tracks_df.id.isin(ids)]

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

        distances = pairwise_distances(kmeans_model.cluster_centers_, tracks_df[
            ['danceability', 'instrumentalness', 'energy', 'tempo', 'valence']], metric='euclidean')
        ind = [np.argpartition(i, 5)[:5] for i in distances]
        closest = [tracks_df[['name', 'id', 'type']].iloc[indexes] for indexes in ind]
        # print(closest[user_favorite_cluster])
        closest_df = pd.DataFrame(closest[user_favorite_cluster], columns=['name', 'id'])
        result_recommendation = closest_df['name'].values.tolist()
        # print(closest_df)
        # print(result_recommendation)

        return result_recommendation
