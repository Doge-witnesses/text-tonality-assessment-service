def fix_command(text : str, words : list):
    import numpy as np
    array = np.array(words)

    from pyxdameraulevenshtein import damerau_levenshtein_distance_seqs, normalized_damerau_levenshtein_distance_seqs
    result = list(zip(words, list(normalized_damerau_levenshtein_distance_seqs(text, array))))

    command, rate = min(result, key=lambda x: x[1])
    if rate > 0.40:
        return

    return command
 
def text_ru_clear(text : str, words : list) -> list:
  for letter in text:
    x = ord(letter)
    if (x >= 1072 and x <= 1103) or (x >= 1040 and x <= 1071) or x == 1105 or x == 1025 or x == 32:
      continue
    else:
      text = text.replace(letter, ' ')
      
  while '  ' in text:
    text = text.replace('  ', ' ')
    
  text = text.lower()
  text = text.split(' ')
  
  if text[len(text)-1] == '':
    text.pop(len(text)-1)
    
  for i in range(len(text)):
    text[i] = fix_command(text[i], words)
    
  return text 
