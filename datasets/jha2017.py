from . import dataset
import os
import pandas as pd
from io import BytesIO
from . import helpers

class Jha2017(dataset.Dataset):
    
    name = "jha2017"
    url = "https://github.com/AkshitaJha/NLP_CSS_2017/archive/master.zip"
    hash = "da7392bfa1b5c7d6aa8540b1943abd5bf941f1a8e8e12dfa37335164c9752edb"
    files = [
        {
            "name": "jha2016en_benevolent.csv",
            "language": "en",
            "type": "training",
            "platform": "twitter"
        },
        {
            "name": "jha2016en_hostile.csv",
            "language": "en",
            "type": "training",
            "platform": "twitter"
        }
    ]
    comment = """The file benevolent_sexist.tsv contains Tweet ID's of tweets that exhibit benevolent sexism. The file hostile_sexist.tsv contains Tweet ID's of tweets that are hostile in nature. The hostile sexist tweets were part of the Hate Speech Dataset (Waseem and Hovy, 2016)."""
    license = """ """

    @classmethod
    def process(cls, tmp_file_path, dataset_folder, temp_folder):
        tmp_file_path = helpers.unzip_file(tmp_file_path)
        benevolent_file = os.path.join(tmp_file_path, "NLP_CSS_2017-master/benevolent_sexist.tsv")
        hostile_file = os.path.join(tmp_file_path, "NLP_CSS_2017-master/hostile_sexist.tsv")

        benevolent_file = helpers.clean_csv(benevolent_file, ["tweet_id"])
        hostile_file = helpers.clean_csv(hostile_file, ["tweet_id"])

        hostile_file = helpers.add_column(hostile_file, "labels", ["sexist", "hostile"])
        benevolent_file = helpers.add_column(benevolent_file, "labels", ["sexist", "benevolent"])

        benevolent_file = helpers.download_tweets_for_csv(benevolent_file, "tweet_id")
        hostile_file = helpers.download_tweets_for_csv(hostile_file, "tweet_id")
        
        helpers.copy_file(hostile_file, os.path.join(dataset_folder, "jha2016en_hostile.csv"))
        helpers.copy_file(benevolent_file, os.path.join(dataset_folder, "jha2016en_benevolent.csv"))