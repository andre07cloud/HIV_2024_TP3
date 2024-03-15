from poly_sbst.mutation.abstract_mutation import AbstractMutation
import numpy as np
import random
from urllib.parse import urlparse, urlunparse

class UrlTestSuiteMutation(AbstractMutation):

    def __init__(self, mut_rate: float = 0.4, min_mutations: int = 1,
        max_mutations: int = 10, generator=None):
        super().__init__(mut_rate, generator)
        self.mut_rate = mut_rate
        self.generator = generator
        self.min_mutations = min_mutations
        self.max_mutations = max_mutations
        #self.mutators = [self._delete_random_character, self._replace_random_character]
    

    def _do_mutation(self, x) -> np.ndarray:
        """
        Perform mutation on an individual.

        Args:
            x: The individual to mutate.

        Returns:
            The mutated individual.

        """
        """Return x with a random mutation applied"""
        possible_mutations = [
            self._delete_random_character,
            #self._insert_random_character,
            self._replace_random_character
        ]
        mutator = np.random.choice(possible_mutations)
        #mutator = random.choice(self.mutators)
        return mutator(x)
    
    def _delete_random_character(self, x):
        """Returns x with a random character deleted"""
        
        url_parsed = []
        for url in x:
            url_parsed.append(urlparse(url))
        #print("************************************************")
        #print(url_parsed[0])
        #print("************************************************")
        i = 0
        for url in url_parsed:

            elements = [url.scheme, url.netloc, url.path, url.params, url.query, url.fragment]
            random_element_index = random.randrange(len(elements))  # Choose a random element index

            # Skip deleting essential elements: scheme and netloc
            while url.scheme == url.netloc == '' and random_element_index < 2:
                random_element_index = random.randrange(len(elements))  # Reselect if scheme or netloc is empty

            elements[random_element_index] = ''  # Delete the chosen element by setting it to an empty string

            modified_url = urlunparse(elements)  # Reconstruct the URL with the deleted element
            url_parsed[i] = modified_url
            i += 1
        #print(url_parsed[0])
        return url_parsed

    def _insert_random_character(self, x):
        """Returns x with a random character inserted"""
        pos = random.randint(0, len(x))
        random_character = chr(random.randrange(32, 127))
        return x[:pos] + random_character + x[pos:]

    def _replace_random_character(self, x):
        """Returns x with a random character replaced"""
        url_parsed = []
        for url in x:
            url_parsed.append(urlparse(url))
        #print("************************************************")
        #print(url_parsed[0])
        #print("************************************************")
        #parsed_url = x  # Parse the URL into its components
        i = 0
        for url in url_parsed:

            elements = [url.scheme, url.netloc, url.path, url.params, url.query, url.fragment]
            random_element_index = random.randrange(len(elements))  # Choose a random element index

            # Generate a replacement string with random uppercase and lowercase letters
            replacement = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(4))

            elements[random_element_index] = replacement  # Replace the chosen element

            modified_url = urlunparse(elements)  # Reconstruct the URL with the modified element
            url_parsed[i] = modified_url
            i += 1
        return url_parsed