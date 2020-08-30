# AudioSet-VGGish model in pytorch
A PyTorch implementation of [Google's VGGish model for AudioSet](https://github.com/tensorflow/models/tree/master/research/audioset)

# Model
[Download the pretrained model](https://github.com/bongjun/audioset_vggish_pytorch/releases/download/v0.1/vggish_pytorch.zip) which was converted from the tensorflow checkpoints provided in [the AudioSet repo](https://github.com/tensorflow/models/tree/master/research/audioset)

# To do
To make sure the pytorch model works in the same way with the tensorflow model
- [ ] Check if they output the same embedding given an audio recording.
- [ ] Check if they classify a set of audio exampels in the same way.
