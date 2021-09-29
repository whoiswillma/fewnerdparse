from common import _parse

FEWNERD_SUPERVISED = {
    'train': _parse('supervised/train.txt'),
    'dev': _parse('supervised/dev.txt'),
    'test': _parse('supervised/test.txt'),
}

FEWNERD_INTRA = {
    'train': _parse('intra/train.txt'),
    'dev': _parse('intra/dev.txt'),
    'test': _parse('intra/test.txt'),
}

FEWNERD_INTER = {
    'train': _parse('inter/train.txt'),
    'dev': _parse('inter/dev.txt'),
    'test': _parse('inter/test.txt'),
}

