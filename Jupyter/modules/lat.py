kyrlat = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'h', 
          'ґ': 'g', 'д': 'd', 'е': 'e', 'є': 'je', 
          'ж': 'ź', 'з': 'z', 'и': 'y', 'i': 'i', 
          'ї': 'ji', 'й': 'j', 'к': 'k', 'л': 'l', 
          'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 
          'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 
          'ф': 'f', 'х': 'ch', 'ц': 'c', 'ч': 'ć', 
          'ш': 'ś', 'щ': 'ść', 'ь': 'j', 'ю': 'ju', 
          'я': 'ja',
          'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'H',
          'Ґ': 'G', 'Д': 'D', 'Е': 'E', 'Є': 'Je',
          'Ж': 'Ź', 'З': 'Z', 'И': 'Y', 'I': 'I', 
          'Ї': 'Ji', 'Й': 'J', 'К': 'K', 'Л': 'L', 
          'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 
          'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 
          'Ф': 'F', 'Х': 'Ch', 'Ц': 'C', 'Ч': 'Ć', 
          'Ш': 'Ś', 'Щ': 'Ść', 'Ь': 'J', 'Ю': 'Ju', 
          'Я': 'Ja'}

kacap = ['Ё', 'ё', 
         'Ъ', 'ъ',
         'Ы', 'ы',
         'Э', 'э']

anglia = ['A', 'a',
          'B', 'b',
          'C', 'c',
          'D', 'd',
          'E', 'e',
          'F', 'f',
          'G', 'g',
          'H', 'h',
          'I', 'i',
          'J', 'j',
          'K', 'k',
          'L', 'l',
          'M', 'm',
          'N', 'n',
          'O', 'o',
          'P', 'p',
          'Q', 'q',
          'R', 'r',
          'S', 's',
          'T', 't',
          'U', 'u',
          'V', 'v',
          'W', 'w',
          'X', 'x',
          'Y', 'y',
          'Z', 'z']


def perekladacz(text) -> str: 
    
    """
        Cja funkcija perekladaje tekst na latynsjku abetku

    Args:
        text (str): ukrajinsjkyj tekst

    Returns:
        str: latynsjkyj tekst
    """
    
    new_text = text
    
    for letter in text: 
        if letter in kacap: 
            return 'Ruzzkij vajennyj karablj, idi nachuj'
        if letter in anglia:
            return 'Oh, you are from Anglia?'
    
    for key, value in kyrlat.items():
        new_text = new_text.replace(key, value)
    
    return new_text


if __name__ == "__main__":
    vasztekst = str(input('vaś tekst: ')) 
    
    print('')
    print(perekladacz(vasztekst))
    print('')

