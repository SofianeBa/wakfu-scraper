import nltk
from typing import Tuple

class Extractor:
    @staticmethod
    def condition(token: str, params: list) -> str:
        resultCondition = ''
        paramsNumber = ''
        regexpResults = nltk.re.match(r"{\[(~)(\d)]\?(.*?):(.*?)}$", token)
        if regexpResults != None:
            paramsNumber = regexpResults.group(2)
            resultCondition = regexpResults.group(3) if len(params) < int(paramsNumber) else regexpResults.group(4)
        return resultCondition

    @staticmethod
    def ternaryResult(token: str) -> str:
        resultTernary = ''
        regexpResults = nltk.re.match(r"\?(.*?):", token)
        if regexpResults != None:
            resultTernary = regexpResults.group(1)
        return resultTernary

    @staticmethod
    def ternaryComparison(token: str) -> Tuple[str, str]:
        defaultComparisonSymbol = '>'
        defaultComparisonValue = '1'
        regexpMatch = nltk.re.match(r"\[(\D)(.*?)]", token)
        if regexpMatch != None:
            defaultComparisonSymbol = regexpMatch.group(1)
            defaultComparisonValue = regexpMatch.group(2)
        return defaultComparisonSymbol, defaultComparisonValue
