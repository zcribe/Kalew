from random import randint

from seeds import kalev_1850


class TextGenerator:
    def __init__(self):
        self.seed = kalev_1850.KALEV
        self.seed_length = len(self.seed) - 1

    def choose_pseudo_random_sentence(self):
        return self.seed[randint(0, self.seed_length)]

    def generate_paragraph(self, min_length=500):
        paragraph = ""

        while len(paragraph) < min_length:
            paragraph += self.choose_pseudo_random_sentence()

        return paragraph

    def generate_text(self, nr_paragraphs=10):
        text = ""
        counter = 0

        while counter < nr_paragraphs:
            text += self.generate_paragraph()
            text += "\n"
            counter += 1

        return text

a = TextGenerator()
print(a.generate_text())