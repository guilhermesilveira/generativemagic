from examples.guilhermesilveira.spelling_designer import SpellingDesigner
from generativemagic.movements.riffle import basic_parameter_space, RiffleShuffle, parameter_space
from generativemagic.spelling import CachedLanguage, English


def main():
    language = CachedLanguage(English())
    example = SpellingDesigner(language)
    # example.run(basic_parameter_space(), effect_type=RiffleShuffle, threads=8)
    example.run(parameter_space(), effect_type=RiffleShuffle, threads=8)


if __name__ == '__main__':
    main()
