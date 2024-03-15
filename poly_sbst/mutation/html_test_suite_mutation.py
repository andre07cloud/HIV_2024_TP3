from poly_sbst.mutation.abstract_mutation import AbstractMutation
import numpy as np
import random
from urllib.parse import urlparse, urlunparse
from html.parser import HTMLParser
from random import choice
from bs4 import BeautifulSoup  # Import BeautifulSoup for element selection

class HtmlTestSuiteMutation(AbstractMutation):

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
            self._insert_random_character,
            self._replace_random_character
        ]
        mutator = np.random.choice(possible_mutations)
        #mutator = random.choice(self.mutators)
        return mutator(x)
    
    def _delete_random_character(self, x):
        """Returns x with a random character deleted"""
        
        html_updated = []
        j = 0
        for html_string in x:
            # Parse the HTML string into a BeautifulSoup object
            soup = BeautifulSoup(html_string, 'html.parser')

            # Find all suitable elements (excluding script and style tags)
            replaceable_elements = soup.find_all(lambda tag: tag.name not in ['script', 'style'])

            # Check if there are any replaceable elements
            if not replaceable_elements:
                html_updated[j] = html_string

            # Choose a random element to delete
            random_element = choice(replaceable_elements)

            # Extract the element and remove it from the soup object
            random_element.extract()
            html_updated.append(str(soup))
            j += 1

        return html_updated

    def _insert_random_character(self, x):
        """Returns x with a random character inserted"""
        elements = ["<img src='random_image.jpg' alt='Random Image'>", "<b>Bold text</b>", "<i>Italic text</i>"]
        html_updated = []
        j = 0
        for html_string in x:
            # Choose a random element to insert
            random_element = choice(elements)

            # Find a random position to insert (avoiding tags)
            valid_positions = []
            for i in range(len(html_string)):
                if html_string[i] not in "<>":
                    valid_positions.append(i)

            if not valid_positions:
                html_updated[j] = html_string  # No valid positions to insert

            insert_position = choice(valid_positions)

            # Insert the random element at the chosen position
            inserted = html_string[:insert_position] + random_element + html_string[insert_position:]
            html_updated.append(inserted)
            j += 1

        return html_updated


    def _replace_random_character(self, x):
        """Returns x with a random character replaced"""
        html_replaced = []
        i = 0
        elements = ["<i>Italic text</i>", "<span style='color:red'>Red text</span>"]
        for html_string in x:
            
            # Parse the HTML string into a BeautifulSoup object
            soup = BeautifulSoup(html_string, 'html.parser')

            # Find all suitable elements (excluding script and style tags)
            replaceable_elements = soup.find_all(lambda tag: tag.name not in ['script', 'style'])

            # Check if there are any replaceable elements
            if not replaceable_elements:
                html_replaced[i] = html_string

            # Choose a random element to replace
            random_element = choice(replaceable_elements)

            # Choose a random element from the provided list for replacement
            replacement_element = choice(elements)

            # Replace the random element with the chosen element
            random_element.replace_with(BeautifulSoup(replacement_element, 'html.parser'))
            updated = str(soup)
            html_replaced.append(updated) 
            i += 1

        return html_replaced