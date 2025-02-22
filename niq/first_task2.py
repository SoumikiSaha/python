import re

def parse_nutritional_values(text):
    nutrition_dict = {}
    
    patterns = [
        r"([\wÀ-ÿ\s\-]+)\s*:\s*([\d,\.]+\s*[a-zA-Z%µ]*)", 
        r"([\wÀ-ÿ\s\-]+)\s*\(([\w,]+)\)\s*:\s*([\d,\.]+\s*[a-zA-Z%µ]*)"
    ]
    
    for pattern in patterns:
        matches = re.findall(pattern, text)
        for match in matches:
            if len(match) == 3:
                name = f"{match[0]} ({match[1]})"
                value = match[2].strip()
            else:
                name, value = match
                name = name.strip()
                value = value.strip()
            nutrition_dict[name] = value
    
    return nutrition_dict

text = """Additifs nutritionnels : Vitamine C-D3 : 160 UI, Fer (3b103) : 4mg, Iode (3b202) : 0,28 mg, Cuivre (3b405, 3b406) : 2,2 mg,Manganèse (3b502, 3b503, 3b504) : 1,1 mg, Zinc (3b603,3b605, 3b606) : 11 mg –Clinoptilolited’origine sédimentaire : 2 g. Protéine : 11,0 % - Teneur en matières grasses : 4,5 % - Cendres brutes : 1,7 % - Cellulose brute : 0,5 % - Humidité : 80,0 %."""
print(parse_nutritional_values(text))