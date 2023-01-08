## Lab 2

We take the texts, split them into sentences, clear any interpunction and lowercase
every word (the words may be very rare so I think that lowercasing is a good idea, this
is not tested though).

### Training embeddings

1. `corpus.txt` + `full.txt` -> `data/`
1. `extract_sentences.py`
1. `train_embeddings.py`

### Training classification models

1. `extract_problem.py`
1. `experiments.ipynb`

### Custom embeddings (other than fasttext)

Create another dataset in `data.py` that will extract the embeddings, the template is
already there (we extract them once to speed up the training process, as the dataset
fits into memory).
