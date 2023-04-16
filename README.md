# Reproduce

I've tried to save the folder structure I have, but did not push any files  
Also I've saved the exact config file I used so you can have a look

## Installation

```bash
# create venv
python -m venv venv

# activate venv
.\venv\scripts\activate

# install libs
pip install -r requirements.txt
```

## Running inference

***This example is for running inference on WLASL pretrained BERT***

The exact filenames and config variables (like `data.*_pipiline.dataset._target_`) whould differ, but you should get the idea
Here're the main steps:

- Download desired metadata and model from [here](https://openhands.ai4bharat.org/en/latest/instructions/models.html)
- Unzip them in the main folder (where the test.py is)
- Add videos you'd like to inference on in the `wlasl_metadata/videos/` *(that said it could be any folder, you just have to specify that in the config)*
- Change paths in `pretrained` (.ckpt file), `data.test_pipiline.dataset.split_file` (asl*.json) and `data.test_pipiline.dataset.root_dir` (path to videos) to the paths on your machine
- Put the config I provided into `wlasl_bert/wlasl/bert/`, so you whould override the existing one (for inference) ((the one I used is already there))
- run `test.py`

This whould automatically convert you videos into .pkl files and run inference on them

## Things I've changed

You might need to do the same for other datasets if wish to use them:

1. openhands/datasets/isolated/base.py
   - `def __getitem_pose()` -> `def getitem_pose()`
   - `self.__getitem = self.__getitem_pose` -> `self.__getitem = self.getitem_pose`

2. openhands/apis/inference.py
   - `dataloader.dataset.id_to_gloss[pred_index]` -> `dataloader.dataset.id_to_gloss[int(pred_index)]`

I might've changed something else, but I don't really remember

## Other useful things to know

To run inference you have to create `test_pipeline` in the `config`, it should look like `valid_pipeline` but with added `inference_mode: true` in the .dataset
Also if you wish to use pretrained model you have to add path to `.ckpt` at the start of the config

## Fine-tuning models and training them on you own datasets

To do that you'd have to create you own dataset parser in `openhands/apis/datasets/isolated/` in the format they provide. There is an example somewhere in docs. You might need to change model loading (for example WLASL pretrained BERT loads with classifier for 2000 words and you'd need to change that if your dataset has less labels)  

You also have to convert your files to `.pkl` and they provide a script for that.

There're also problems with running `DPC self-supervised learning`, but it's fixed but downgrading PyTorch. I don't remember the exact version right now, but it's something like 1.11 with CUDA 10.x of 11.x
