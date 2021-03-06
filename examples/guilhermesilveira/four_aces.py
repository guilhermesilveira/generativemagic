from examples.guilhermesilveira.spelling_designer import SpellingDesigner
from generativemagic.effects.four_aces import FourAces, parameter_space
from generativemagic.spelling import CachedLanguage, English


def main():
    language = CachedLanguage(English())
    example = SpellingDesigner(language)
    # example.run(basic_parameter_space(), effect_type = FourAces)
    # example.run(basic_parameter_space2(), effect_type = FourAces)
    example.run(parameter_space(), effect_type=FourAces)


if __name__ == '__main__':
    main()
