from examples.guilhermesilveira.spelling_designer import SpellingDesigner
from generativemagic.movements.riffle import basic_parameter_space, RiffleShuffle, parameter_space
from generativemagic.spelling import CachedLanguage, English


def main():
    language = CachedLanguage(English())
    example = SpellingDesigner(language)
    # example.run(basic_parameter_space(), effect_type=RiffleShuffle)
    example.run(parameter_space(), effect_type=RiffleShuffle)


if __name__ == '__main__':
    main()
