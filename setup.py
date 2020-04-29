from setuptools import setup, find_packages

setup(
    name='convlstm',
    description='Implementation of Convolutional LSTM in PyTorch',
    author='ndrplz/ConvLSTM_pytorch',
    packages=find_packages(),
    version=0.1,
    install_requires=["torch"],
)
