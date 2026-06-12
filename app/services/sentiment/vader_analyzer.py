from vaderSentiment.vaderSentiment import (
    SentimentIntensityAnalyzer,
)


class VaderAnalyzer:

    def __init__(self):

        self.analyzer = (
            SentimentIntensityAnalyzer()
        )

    def analyze(
        self,
        text: str,
    ) -> dict:

        return self.analyzer.polarity_scores(
            text
        )