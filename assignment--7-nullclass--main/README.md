# Task 7: Create a feature to translate the English word to Hindi and it should not translate if the English starts with vowels and other words it should convert . If we enter a English word starts with Vowels it should show an error message as This word starts with Vowels provide some other words and this model should be able to convert english word starts with vowels around 9 PM to 10 PM

## Overview
This task translates English words to Hindi, excluding words that start with vowels unless it is between 9 PM to 10 PM IST.

## Model
- The model uses a sequential architecture with constraints on vowels and time.

## Data
- Data consists of English-Hindi translation pairs.
- Sentences are preprocessed and tokenized.

## Files
- `task7.ipynb`: Contains the translation model with vowel-based constraints.
- `gui.py`: GUI script to interact with the model.

## Setup
1. Clone the repository:
   ```bash
   git clone <repo_url>
   cd <repo_name>
