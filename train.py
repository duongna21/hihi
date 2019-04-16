from torch.optim.adam import Adam
from flair.training_utils import Metric, init_output_file, WeightExtractor, clear_embeddings, EvaluationMetric

from flair.optim import SGDW, AdamW
from flair.data import TaggedCorpus
from flair.data_fetcher import NLPTaskDataFetcher

# define columns
columns = {0: 'text', 1: 'ner'}

# this is the folder in which train, test and dev files reside
data_folder = '/Users/naduong1001/Downloads/flair/resources/taggers/conll_03'

# retrieve corpus using column format, data folder and the names of the train, dev and test files
corpus: TaggedCorpus = NLPTaskDataFetcher.load_column_corpus(data_folder, columns,
                                                             train_file='train.txt',
                                                             test_file='test.txt',
                                                             dev_file='dev.txt')

from flair.data import TaggedCorpus
from flair.data_fetcher import NLPTaskDataFetcher, NLPTask
from flair.embeddings import TokenEmbeddings, WordEmbeddings, StackedEmbeddings
from typing import List

# 2. what tag do we want to predict?
tag_type = 'ner'

# 3. make the tag dictionary from the corpus
tag_dictionary = corpus.make_tag_dictionary(tag_type=tag_type)
print(tag_dictionary.idx2item)

from flair.embeddings import CharacterEmbeddings
from flair.embeddings import FlairEmbeddings



embedding_types: List[TokenEmbeddings] = [
    WordEmbeddings('glove'),
    #FlairEmbeddings('/Users/naduong1001/Downloads/flair/resources/taggers/No_Flair/best-model.pt')
]

embeddings: StackedEmbeddings = StackedEmbeddings(embeddings=embedding_types)

# 5. initialize sequence tagger
from flair.models import SequenceTagger
tagger: SequenceTagger = SequenceTagger(hidden_size=256,
                                        embeddings=embeddings,
                                        tag_dictionary=tag_dictionary,
                                        tag_type=tag_type,
                                        use_crf=True)
from flair.trainers import ModelTrainer

trainer: ModelTrainer = ModelTrainer(tagger, corpus, optimizer = SGDW)

# trainer.train('resources/taggers/No_Flair',
#               learning_rate=0.12,
#               mini_batch_size=16,
#               max_epochs=2)
trainer.final_test('/Users/naduong1001/Downloads/flair/resources/taggers/TMDT', True, EvaluationMetric.MICRO_F1_SCORE, 16)