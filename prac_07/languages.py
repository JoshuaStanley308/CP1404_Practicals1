

from prac_07.programming_language import ProgrammingLanguage


def main():

    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("visual_basic", "Static", True, 1995)

    ruby.__str__()
    python.__str__()
    visual_basic.__str__()
