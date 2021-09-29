from dataset import *

num_sentences = (
    sum(len(FEWNERD_SUPERVISED[split])
        for split in ['train', 'dev', 'test'])
)

num_tokens = (sum(len(example['tokens'])
                  for split in ['train', 'dev', 'test']
                  for example in FEWNERD_SUPERVISED[split]))

print(f'# Sentences = {num_sentences}')
print(f'# Tokens = {num_tokens}')
print()

for split, splitname in [
    (FEWNERD_SUPERVISED, 'Few-NERD (SUP)'),
    (FEWNERD_INTRA, 'Few-NERD (INTRA)'),
    (FEWNERD_INTER, 'Few-NERD (INTER)')]:

    for subset in ['train', 'dev', 'test']:
        print(f'{splitname} {subset}: {len(split[subset])}')
    print()
