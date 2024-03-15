import numpy as np 
import random
from poly_sbst.generators.random_generator import RandomGenerator
from poly_sbst.generators.abstract_generator import AbstractGenerator
from poly_sbst.common.abstract_grammar import AbstractGrammar
#abstract_generator import AbstractGenerator
class UrlTestSuiteGenerator(AbstractGenerator):

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
        
        gram_url_dict =  {
        "<start>":
            ["<url>"],
        "<url>":
            ["<scheme>://<authority><path><query>"],
        "<scheme>":
            ["http", "https", "ftp", "ftps"],
        "<authority>":
            ["<host>", "<host>:<port>", "<userinfo>@<host>", "<userinfo>@<host>:<port>"],
        "<host>":
            ["yahoo.com", "www.google.com", "bing.com", "opera.com", "safari.com"],
        "<port>":
            ["80", "8080", "<nat>"],
        "<nat>":
            ["<digit>", "<digit><digit>"],
        "<digit>":
            ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
        "<userinfo>":
            ["user:password"],
        "<path>":
            ["", "/", "/<id>"],
        "<id>":
            ["abc", "def", "x<digit><digit>"],
        "<query>":
            ["", "?<params>"],
        "<params>":
            ["<param>", "<param>&<params>"],
        "<param>":
            ["<id>=<id>", "<id>=<nat>"],
        }
        grammar = AbstractGrammar(gram_url_dict)
        n = random.randint(self.min_length, self.max_length)
        test_suite = []
        for i in range(n):
            test_suite.append(grammar.generate_input())
        #test_suite.append(grammar.generate_input())
        #print(test_suite)
        #inputs = grammar.generate_input()
        #print(test_suite)
        return np.array(test_suite)


