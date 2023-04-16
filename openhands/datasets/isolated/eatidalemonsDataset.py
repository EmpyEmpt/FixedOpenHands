import os
import pandas as pd
from .base import BaseIsolatedDataset
from ..data_readers import load_frames_from_video

class eatidalemonsDataset(BaseIsolatedDataset):
    """
    Turkish Isolated Sign language dataset from the paper:
    
    `AUTSL: A Large Scale Multi-modal Turkish Sign Language Dataset and Baseline Methods <https://arxiv.org/abs/2008.00932>`_
    """

    lang_code = "eal"

    def read_glosses(self):
        # Read glosses
        glosses = pd.read_csv(self.split_file)

        # Save them sorted
        self.glosses = list(set(glosses['gloss']))
    
    def read_original_dataset(self):
        # Read some mapping file file
        df = pd.read_csv(self.split_file)

        for i in range(len(df)):
            # do somethings
            instance_entry = df['filename'][i], self.gloss_to_id[df['gloss'][i]]
            self.data.append(instance_entry)

    def read_video_data(self, index):
        video_name, label = self.data[index]
        video_path = os.path.join(self.root_dir, video_name)
        imgs = load_frames_from_video(video_path)
        return imgs, label, video_name