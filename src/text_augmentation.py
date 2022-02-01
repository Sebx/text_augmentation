#!/usr/bin/env python
# TextAugment: EDA
#
# Copyright (C) 2022
# Author: Sebx
#
# URL: <https://github.com/Sebx/text_augmentation/>
# For license information, see LICENSE
#
"""
This module is an implementation of some basics text augmentation algorithms.
"""
import random


class TextAugmentation:
    """
    This class is an implementation of some basics text augmentation algorithms.

    Example usage: ::
        >>> from text_augmentation import TextAugmentation
        >>> TextAugmentation.random_deletion("Jose is good")
        >>> TextAugmentation.random_swap("Also Juan is good")
        >>> TextAugmentation.random_insertion("But Pedro is bad")
    """

    def __init__(self, stop_words=None, random_state=1):
        pass


    def _create_synonyms():
        pass


    @staticmethod
    def random_deletion(sentence):
        """Randomly delete words from the sentence.

        :param sentence: Sentence

        :return: Augmented sentence.
        """
        words = sentence.split()

        if len(words) == 1:
            return words
       
        new_words = list()
        
        for word in words:
            r = random.uniform(0, 1)
            if r > 0.2:
                new_words.append(word)

        if len(new_words) == 0:
            return random.choice(words)

        return " ".join(new_words)


    @staticmethod
    def random_swap(sentence, n=1):
        """Randomly swap two words in the sentence n times.

        :param sentence: Sentence.
        :param n: Number of repetitions to swap.

        :return: Augmented sentence.
        """
        def swap_word(new_words):
            random_idx_1 = random.randint(0, len(new_words) - 1)
            random_idx_2 = random_idx_1
            counter = 0
            while random_idx_2 == random_idx_1:
                random_idx_2 = random.randint(0, len(new_words) - 1)
                counter += 1
                if counter > 3:
                    return new_words
            new_words[random_idx_1], new_words[random_idx_2] = new_words[random_idx_2], new_words[random_idx_1]
            return new_words

        words = sentence.split()
        new_words = words.copy()
        for _ in range(n):
            new_words = swap_word(new_words)
        return " ".join(new_words)


    @staticmethod
    def random_insertion(sentence, n=1):
        """Randomly insert n words into the sentence

        :param sentence: Sentence.
        :param n: Number of words to insert.

        :return: Augmented sentence.
        """

        def create_synonyms(word):
            # No time to implement this.
            return f"{word}-Word-Synonyms"

        def add_word(new_words):
            synonyms = list()
            counter = 0
            stopwords = ["stopword1", "stopword12", "stopword3"]
            while len(synonyms) < 1:
                random_word_list = list([word for word in new_words if word not in stopwords])
                random_word = random_word_list[random.randint(0, len(random_word_list) - 1)]
                synonyms = create_synonyms(random_word)
                counter += 1
                if counter >= 10:
                    return new_words 
            random_synonym = synonyms[0]
            random_idx = random.randint(0, len(new_words) - 1)
            new_words.insert(random_idx, random_synonym)
            return new_words

        n = n
        sentence = sentence
        words = sentence.split()
        new_words = words.copy()
        
        for _ in range(n):
            new_words = add_word(new_words)
        
        return " ".join(new_words)
