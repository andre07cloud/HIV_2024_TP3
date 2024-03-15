import numpy as np 
import random
from poly_sbst.generators.random_generator import RandomGenerator
from poly_sbst.generators.abstract_generator import AbstractGenerator
from poly_sbst.common.abstract_grammar import AbstractGrammar
from collections import namedtuple
#abstract_generator import AbstractGenerator
class HtmlTestSuiteGenerator(AbstractGenerator):

    def __init__(self):
        super().__init__()
        self._name = "RandomGenerator"
        self.test_gen = RandomGenerator()
        self.max_length = 15
        self.min_length = 10
    
    def cmp_func(self, x: np.ndarray, y: np.ndarray) -> float:
        """
        Compare two test cases and return a similarity score.

        Args:
            x (np.ndarray): The first test case.
            y (np.ndarray): The second test case.

        Returns:
            float: The similarity score between the two test cases.
        """
        return 0.0
    

    def generate_random_test(self) -> str:
        
        # Define a namedtuple for HTML element information
        HTMLElement = namedtuple("HTMLElement", ["name", "opening_tag", "closing_tag", "attrs", "content_model"])

        gram_html_dict =  {
            "<start>": ["<html>"],
            "<html>": ["<head><body>"],
            "<head>": ["<title><meta>"],
            "<title>": ["<title-tag>"],
            "<title-tag>": ["<title-content>"],
            "<title-content>": ["Hello World"],
            "<meta>": ['<meta-tag>'],
            "<meta-tag>": ['<meta-content>'],
            "<meta-content>": ['<meta-charset>'],
            "<meta-charset>": ['utf-8'],
            "<body>": ["<header><main><footer>"],
            "<header>": ["<header-tag>"],
            "<header-tag>": ["<header-content>"],
            "<header-content>": ["<h1>Welcome</h1>"],
            "<main>": ["<main-tag>"],
            "<main-tag>": ["<main-content>"],
            "<main-content>": ["<p>This is the main content</p>"],
            "<footer>": ["<footer-tag>"],
            "<footer-tag>": ["<footer-content>"],
            "<footer-content>": ["<p>Footer content goes here</p>"]
            }
        grammar = AbstractGrammar(gram_html_dict)
        n = random.randint(self.min_length, self.max_length)
        test_suite = []
        for i in range(n):
            test_suite.append(grammar.generate_input())
        #test_suite.append(gram_html_dict.generate_input())
        #print(test_suite)
        #inputs = gram_html_dict.generate_input()
        print(test_suite)
        return np.array(test_suite)


