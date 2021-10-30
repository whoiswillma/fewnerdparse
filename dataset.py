import os
from typing import Optional

FEWNERD_COARSE_TYPES: list[str] = [
    'location',
    'person',
    'organization',
    'building',
    'art',
    'product',
    'event',
    'other'
]

FEWNERD_COARSE_TYPES_TO_FINE_TYPES: dict[str, list[str]] = {
    'location': [
        'GPE',
        'bodiesofwater',
        'island',
        'mountain',
        'park',
        'road/railway/highway/transit',
        'other',
    ],
    'person': [
        'actor',
        'artist/author',
        'athlete',
        'director',
        'politician',
        'scholar',
        'soldier',
        'other',
    ],
    'organization': [
        'company',
        'education',
        'government/governmentagency',
        'media/newspaper',
        'politicalparty',
        'religion',
        'sportsleague',
        'sportsteam',
        'showorganization',
        'other',
    ],
    'building': [
        'airport',
        'hospital',
        'hotel',
        'library',
        'restaurant',
        'sportsfacility',
        'theater',
        'other',
    ],
    'art': [
        'music',
        'film',
        'writtenart',
        'broadcastprogram',
        'painting',
        'other'
    ],
    'product': [
        'airplane',
        'car',
        'food',
        'game',
        'ship',
        'software',
        'train',
        'weapon',
        'other',
    ],
    'event': [
        'attack/battle/war/militaryconflict',
        'election',
        'disaster',
        'protest',
        'sportsevent',
        'other',
    ],
    'other': [
        'astronomything',
        'award',
        'biologything',
        'chemicalthing',
        'currency',
        'disease',
        'educationaldegree',
        'god',
        'language',
        'law',
        'livingthing',
        'medical',
    ]
}

FEWNERD_COARSE_FINE_TYPES: list[tuple[str, str]] = [
    (coarse, fine)
    for coarse, fine_types in FEWNERD_COARSE_TYPES_TO_FINE_TYPES.items()
    for fine in fine_types
]

def _parse(filename):
    examples = []

    id: int = 0
    current_tokens: list[str] = []
    current_coarse: list[Optional[str]] = []
    current_fine: list[Optional[str]] = []

    def init_current():
        nonlocal current_tokens
        nonlocal current_coarse
        nonlocal current_fine

        current_tokens = []
        current_coarse = []
        current_fine = []

    def add_to_examples():
        nonlocal id
        nonlocal current_tokens
        nonlocal current_coarse
        nonlocal current_fine

        assert len(current_tokens) != 0
        assert len(current_tokens) == len(current_coarse)
        assert len(current_tokens) == len(current_fine)

        examples.append({
            'id': id,
            'tokens': current_tokens,
            'coarse_labels': current_coarse,
            'fine_labels': current_fine
        })

        id += 1

    init_current()

    with open(filename) as f:
        for line in f:
            line = line.strip()

            if line:
                token, label = line.split('\t')
                current_tokens.append(token)
                if label != 'O':
                    coarse, fine = label.split('-')
                    current_coarse.append(coarse)
                    current_fine.append(fine)
                    assert coarse in FEWNERD_COARSE_TYPES, coarse
                    assert fine in FEWNERD_COARSE_TYPES_TO_FINE_TYPES[coarse], (coarse, fine)
                else:
                    current_coarse.append(None)
                    current_fine.append(None)

            else:
                add_to_examples()
                init_current()

    if current_tokens:
        add_to_examples()

    return examples

_SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))

FEWNERD_SUPERVISED = {
    'train': _parse(os.path.join(_SCRIPT_DIR, 'supervised', 'train.txt')),
    'dev': _parse(os.path.join(_SCRIPT_DIR, 'supervised', 'dev.txt')),
    'test': _parse(os.path.join(_SCRIPT_DIR, 'supervised', 'test.txt')),
}

FEWNERD_INTRA = {
    'train': _parse(os.path.join(_SCRIPT_DIR, 'intra', 'train.txt')),
    'dev': _parse(os.path.join(_SCRIPT_DIR, 'intra', 'dev.txt')),
    'test': _parse(os.path.join(_SCRIPT_DIR, 'intra', 'test.txt')),
}

FEWNERD_INTER = {
    'train': _parse(os.path.join(_SCRIPT_DIR, 'inter', 'train.txt')),
    'dev': _parse(os.path.join(_SCRIPT_DIR, 'inter', 'dev.txt')),
    'test': _parse(os.path.join(_SCRIPT_DIR, 'inter', 'test.txt')),
}
