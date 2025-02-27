from sklearn import svm
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline

from sentiment_model.processing.features import preprocess_text


def create_pipeline() -> Pipeline:
    return Pipeline(
        [
            (
                "tfidf",
                TfidfVectorizer(
                    preprocessor=preprocess_text, use_idf=True, stop_words="english"
                ),
            ),
            ("clf", svm.SVC(kernel="linear", verbose=True)),
        ]
    )
