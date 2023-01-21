import nltk
nltk.download('punkt')
from interpreter import Interpreter
from models.LocaleSource import LocaleSource

class Core:
    def __init__(self):
        self.interpreter = None

    def parse(self, locale_source: LocaleSource):
        self.interpreter = Interpreter(locale_source)
        tokenized = nltk.word_tokenize(locale_source.locale)
        return self.analyze(tokenized)

    def analyze(self, tokenized):
        should_recurse = False
        recursive_string = ''
        current_param = 1
        parsed_tokens = []
        should_add_space_next = False

        for token in tokenized:
            if token in ["[", "#", "]"]:
                continue
            if token[0] == "{" and "?:" in token:
                recursive_string = self.interpreter.condition(token)
                should_recurse = True
                should_add_space_next = False
            elif token[0] == "|" and token[-1] == "|":
                computed_token = self.interpreter.computation(token)
                parsed_tokens.append(self.add_space(computed_token, should_add_space_next))
                should_add_space_next = False
            elif token[0] == "#":
                param = self.interpreter.param(token, should_add_space_next)
                parsed_tokens.append(self.add_space(param.interpreted_param_value, should_add_space_next))
                current_param = param.current
                should_add_space_next = True
            elif token[0] == "[" and token[-1] == "]":
                parsed_tokens.append(self.interpreter.ternary(token, current_param))
                should_add_space_next = True
            else:
                parsed_tokens.append(self.add_space(token, should_add_space_next))
                should_add_space_next = False

            if should_recurse:
                return self.analyze(nltk.word_tokenize(recursive_string))

        return "".join(parsed_tokens)

    def add_space(self, interpreted_token, should_add_space):
        return " " + interpreted_token if should_add_space else interpreted_token
