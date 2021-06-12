from counter.characters import character_counter
from counter.words import word_counter
from counter.sentences import sentence_counter
import math

level = {0: "Kindergarten", 1: "1st Grade", 2: "2nd Grade", 3: "3rd Grade", 4: "4th Grade", 5: "5th Grade", 6: "6th Grade", 7: "7th Grade", 9: "9th Grade", 10: "10th Grade", 11: "11th Grade", 12: "12th Grade", 13: "College: Freshman", 14: "College: Sophomore", 15: "College: Junior", 16: "College: Senior", 17: "Graduate School"}

def index(text):
    characters = character_counter(text)
    words = word_counter(text)
    sentences = sentence_counter(text)

    #Coleman-liau Index
    index = 0.0588 * (100 * characters / words) - 0.296 * (100 * sentences / words) - 15.8

    if index < 1:
        index = 0
    if index > 16:
        index = 17

    return level[math.ceil(index)]


