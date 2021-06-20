import collections


class Article:
    def __init__(self, title, date, content, comments, id):
        self.title = title
        self.date = date
        self.content = content
        self.comments = comments
        self.id = id
        self.most_used_words = None

    # inits the most_used_words  field of the Article class with dictionary
    # with key(most used word) and value (count)
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
        self.most_used_words = dict(word_counter.most_common(3))

    def set_content_to_first_three_paragraphs(self):
        content_modified = self.content.replace("\n\n", "\n")
        content_modified = content_modified.split('\n')[:4]
        separator = '\n'
        self.content = separator.join(content_modified)
