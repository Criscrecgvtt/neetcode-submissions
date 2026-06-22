from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Creamos el diccionario invertido para agrupar las palabras
        anagramas = defaultdict(list)
        
        for palabra in strs:
            # Ordenamos las letras para que todos los anagramas generen la misma clave
            clave = "".join(sorted(palabra))
            
            # Hacemos append directamente al grupo correspondiente
            anagramas[clave].append(palabra)
            
        # Retornamos únicamente las sublistas con las palabras agrupadas
        return list(anagramas.values())
