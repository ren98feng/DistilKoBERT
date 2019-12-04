import os
import hashlib
import gdown
from distilkobert.tokenization_kobert import KoBertTokenizer

DOWNLOAD_URL_MAP = {
    'pytorch_model': ('https://drive.google.com/uc?id=13_IcqTi2rg7qvAtdc8SO8f7L4fHo9jZH', 'pytorch_model.bin'),
    'config': ('https://drive.google.com/uc?id=1qyfjBsgIy7vw5p19sgwuzno-JWbavy25', 'config.json'),
    'tokenizer_model': ('https://drive.google.com/uc?id=1_F23OdOyp-uK79bpuUxQsRiV6lt8exBW', 'tokenizer_78b3253a26.model'),
    'vocab': ('https://drive.google.com/uc?id=1Cyty9NbmcOVvDT4JyCliDR0jRZt_j0Or', 'vocab.txt')
}


def download(url, filename,  cachedir='~/distilkobert/'):
    f_cachedir = os.path.expanduser(cachedir)
    os.makedirs(f_cachedir, exist_ok=True)
    file_path = os.path.join(f_cachedir, filename)
    if os.path.isfile(file_path):
        print('using cached model')
        return file_path
    gdown.download(url, file_path, quiet=False)
    return file_path


def get_tokenizer(cachedir='~/distilkobert/'):
    f_cachedir = os.path.expanduser(cachedir)
    download(DOWNLOAD_URL_MAP['tokenizer_model'][0], DOWNLOAD_URL_MAP['tokenizer_model'][1])
    download(DOWNLOAD_URL_MAP['vocab'][0], DOWNLOAD_URL_MAP['vocab'][1])

    return KoBertTokenizer.from_pretrained(f_cachedir)