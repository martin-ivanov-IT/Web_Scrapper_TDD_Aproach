import collections
class Article:
    def __init__(self, title, date, content, comments):
        self.title = title
        self.date = date
        self.content = content
        self.comments = comments
        self.most_used_word = None

    def set_most_used_words(self):
        wordcount = {}
        for word in self.content.lower().split():
            word = word.replace(".", "")
            word = word.replace(",", "")
            word = word.replace(":", "")
            word = word.replace(";", "")
            word = word.replace("\n", " ")
            word = word.replace("\n\n", " ")
            word = word.replace("\"", "")
            word = word.replace("„", "")
            word = word.replace("“", "")
            word = word.replace("!", "")
            word = word.replace("?", "")
            word = word.replace(")", "")
            word = word.replace("(", "")
            word = word.replace("*", "")
            if len(word) < 4:
                continue

            if word not in wordcount:
                wordcount[word] = 1
            else:
                wordcount[word] += 1

        word_counter = collections.Counter(wordcount)
        self.most_used_word = dict(word_counter.most_common(3))

    def set_content_to_first_three_paragraphs(self):
        str1 = self.content.replace("\n\n", "\n")
        str = str1.split('\n')[:4]
        separator = '\n'
        self.content = separator.join(str)




