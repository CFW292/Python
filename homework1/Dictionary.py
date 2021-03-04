from homework1.Letter import Letter
class Dictionary:
  def __init__(self):
    self.start_letter = Letter(False, {})

  # imagine adding the word 'cat'
  def add_word(self, word):
    
    # adds 'CAT' to the dictionary
    new_letter = self._add_character('c', self.start_letter)
    new_letter = self._add_character('a', new_letter)
    new_letter = self._add_character('t', new_letter)
    new_letter.is_word = True

    add_letter = self._add_character('a',self.add_letter)

    '''
    staring at self.start_letter
    for every letter in the word:
        if the letter already exists:
          follow it
        else:
          add it and then follow it
    at the end of the word:
      mark that letter as is_word=True
    '''
    
    
  
  def contains_word(self, add):
    # this code has not stared yet.
    pass

  def _add_character(self, character, letter_object):
    new_letter = Letter(False, {})
    letter_object.next_letters[character] = new_letter
    return new_letter
    