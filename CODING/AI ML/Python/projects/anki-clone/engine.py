import json
import csv


# Read definitions.json
def load_vocab_from_json(file_path):
    '''Load vocab data froma JSON file'''
    with open(file_path, 'r') as f:
        data = json.load(f)
# TODO: Come back and finish this later
    return data

class VocabCard:
    '''Represents a single vocab card'''
    def __init__(self):
        return

