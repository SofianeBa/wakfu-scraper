import nltk
from typing import Tuple
from extractor import Extractor
from utils import operandAsMathOperator

class Interpreter:
    def __init__(self, localeSource: Tuple[str, list, int]):
        self.localeSource = localeSource

    def condition(self, token: str) -> str:
        return Extractor.condition(token, self.localeSource[1])

    def ternary(self, token: str, targetParam: int) -> str:
        resultTernary = Extractor.ternaryResult(token)
        comparison = Extractor.ternaryComparison(token)
        param = self.localeSource[1][targetParam]
        if comparison[0] == '>':
            return resultTernary if param > int(comparison[1]) else ''
        elif comparison[0] == '=':
            return resultTernary if param == int(comparison[1]) else ''
        else:
            return ''

    def param(self, token: str, shouldAddSpace: bool) -> Tuple[int, str]:
        regexpResults = nltk.re.match(r"\d", token)
        if regexpResults != None:
            current = int(regexpResults.group())
        else:
            current = 0
        interpretedParamValue = self.calc_param(current)
        return current, interpretedParamValue

    def computation(self, token: str) -> str:
        result = '[Computation]'
        regexpResults = nltk.re.match(r"\|\[#(\d*)(.)(\d*)](.)(.*?)\|", token)
        if regexpResults != None:
            targetParam = int(regexpResults.group(1))
            operand = regexpResults.group(4)
            operandNumber = regexpResults.group(5)
            paramValue = self.calc_param(targetParam, True)
            result = str(operandAsMathOperator[operand](paramValue, operandNumber))
        return result

    def calc_param(self, targetParam: int, precision: bool = False) -> str:
        if not precision:
            return str(
                int(self.localeSource[1][(targetParam - 1) * 2 + 1] * self.localeSource[2]) +
                self.localeSource[1][(targetParam - 1) * 2])
        else:
            return str(
                self.localeSource[1][(targetParam - 1) * 2 + 1] * self.localeSource[2] +
                self.localeSource[1][(targetParam - 1) * 2])
