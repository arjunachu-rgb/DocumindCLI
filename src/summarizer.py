import sumy
import json
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer


def summarize_data(data, sentence_count=3):
    if isinstance(data, str):
        text = data

    elif isinstance(data, (dict, list)):
        text = json.dumps(data, ensure_ascii=False)

    else:
        text = str(data)

    text = text.strip()

    if not text:
        return "No text available to summarize."

    parser = PlaintextParser.from_string(
        text, Tokenizer("english")
    )

    summarizer = LexRankSummarizer()
    summary = summarizer(
        parser.document, sentence_count
    )

    if not summary:
        return text

    return " ".join(str(sentence) for sentence in summary)
