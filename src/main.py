from random import randint

from seeds import kalev_1850


class TextGenerator:
    def __init__(self):
        self.seed = kalev_1850.KALEV
        self.seed_length = len(self.seed) - 1

    def choose_sentence(self):
        return self.seed[randint(0, self.seed_length)]

    def generate_paragraph(self, min_length=500, html=False, headline=False):
        paragraph = ""

        while len(paragraph) < min_length:
            paragraph += self.choose_sentence()

        if html:
            paragraph = f"<p>{paragraph}</p>"

        if headline:
            line = self.choose_sentence()
            if html:
                paragraph = f"<h2>{line}</h2>{paragraph}"

            else:
                paragraph = f"{line}\n\n{paragraph}"

        return paragraph

    def generate_text(self, paragraphs=10):
        text = ""
        counter = 0

        while counter < paragraphs:
            text = "\n\n".join([text, self.generate_paragraph()])
            counter += 1

        return text




a = TextGenerator()
print(a.generate_paragraph(html=True, headline=True))