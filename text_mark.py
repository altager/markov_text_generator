from typing import Dict, AnyStr, List
import random


class Model:
    model_dict: Dict[str, Dict[str, int]] = {"__END__": {}}

    def calculate_model(self):
        with open('data/sample_corpus.txt', 'r', encoding='utf8') as f:
            for line in f:
                self.process_line(line)

    def process_line(self, line: str):
        splitted_line: List[str] = line.split(" ")
        prev: AnyStr = "__END__"
        for w in splitted_line:
            w = w.strip().lower()
            if w not in self.model_dict:
                self.model_dict[w] = {}
            if w in self.model_dict[prev]:
                self.model_dict[prev][w] += 1
            else:
                self.model_dict[prev][w] = 1
            prev = w

    @staticmethod
    def calculate_weights(data: dict):
        res: Dict[str, float] = {}
        for k, v in data.items():
            res[k] = v/sum(data.values())
        return res

    def generate_sentence(self, sentence_len=6):
        result: AnyStr = ""
        prev: AnyStr = "__END__"
        for i in range(0, sentence_len):
            calculated = Model.calculate_weights(self.model_dict[prev])
            result_word = random.choices(list(calculated.keys()), list(calculated.values()), k=1)[0]
            result += result_word + ' '
            prev = result_word
        return result


if __name__ == '__main__':
    m = Model()
    m.calculate_model()
    print(m.generate_sentence())









