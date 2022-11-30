def fix_command(text : str, words : list):
    # Принимает слово -> Возвращает слово с исправленной орфографией
    import numpy as np
    array = np.array(words)

    from pyxdameraulevenshtein import damerau_levenshtein_distance_seqs, normalized_damerau_levenshtein_distance_seqs
    result = list(zip(words, list(normalized_damerau_levenshtein_distance_seqs(text, array))))

    command, rate = min(result, key=lambda x: x[1])
    if rate > 0.40:
        return

    return command



def text_ru_clear(text : str) -> str:
    # Принимает текстовую строку -> Возвращает строку состоящую только из символов кириллицы
    for letter in text:
        x = ord(letter)
        if (x >= 1072 and x <= 1103) or (x >= 1040 and x <= 1071) or x == 1105 or x == 1025 or x == 32:
            continue
        else:
            text = text.replace(letter, ' ')
            
    while '  ' in text:
        text = text.replace('  ', ' ')
    if text[len(text)-1] == ' ':
        text = text[:len(text)-1]
            
    return text



def text_preprocessing(text : str, words : list) -> list:
  # Принимает текст и словарь -> Возвращает форматированный текст
  text = text_ru_clear(text)
  text = text.split(' ')
    
  for i in range(len(text)):
    text[i] = fix_command(text[i], words)
  
  output = ''
  for word in text:
    if word != None:
      output = output + str(word) + ' '
  output = output[:len(output) - 1]
  return output 



def tokenization(text : str) -> list:
    # Принимает форматированный текст -> Возвращает список слов
    L = text.split(' ')
    return L