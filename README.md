# AudioSet-VGGish model in pytorch
A PyTorch implementation of [Google's VGGish model for AudioSet](https://github.com/tensorflow/models/tree/master/research/audioset)

# Model
[Download the pretrained model](https://drive.google.com/open?id=1W_cIgB4Y3k10Un8445UTL3EL0QhI9BNd) which was converted from the tensorflow checkpoints provided in [the AudioSet repo](https://github.com/tensorflow/models/tree/master/research/audioset)

# To do
To make sure the pytorch model works in the same way with the tensorflow model
- [ ] Check if they output the same embedding given an audio recording.
- [ ] Check if they classify a set of audio exampels in the same way.
