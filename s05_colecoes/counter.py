"""
Módulo Collections - Counter (contador)

Collections -> High-performance Container Datetypes

Counter -> Recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter que é parecido com um
dicionário, contendo como chave o elemento da lista passada como parâmetro e como valor a quantidade de ocorrências
desse elemento.

- Exemplo de objeto criado: Counter({'igor': 3, 4: 2, 1: 1, 2: 1, 3: 1, 8: 1, None: 1})

"""

# Utilizando o Counter

# Exemplo 1
'''
from collections import Counter
lista = [1, 2, 3, 4, 4, 'igor', 'igor', 'igor', 8, None]  # Poderia ser qualquer iterável, aqui foi usado uma lista
contador = Counter(lista)
print(contador)
print(type(contador))
elemento = 'igor'
if elemento in lista:
    print(f"O elemento {elemento} aparece {dict(contador)[elemento]} vezes na lista")
else:
    print(f'O elemento {elemento} não está na lista')
'''


# Exemplo 2
from collections import Counter

texto = """ The origin of aerospace engineering can be traced back to the aviation pioneers around the late 19th to 
early 20th centuries, although the work of Sir George Cayley dates from the last decade of the 18th to mid-19th century. 
One of the most important people in the history of aeronautics,[7] Cayley was a pioneer in aeronautical engineering[8] 
and is credited as the first person to separate the forces of lift and drag, which are in effect on any flight vehicle.
[9]

Early knowledge of aeronautical engineering was largely empirical with some concepts and skills imported from other 
branches of engineering.[10] Scientists understood some key elements of aerospace engineering, like fluid dynamics, in 
the 18th century. Many years later after the successful flights by the Wright brothers, the 1910s saw the development 
of aeronautical engineering through the design of World War I military aircraft.

Between World Wars I and II, great leaps were made in aeronautical engineering. The advent of mainstream civil aviation 
greatly accelerated this process. Notable airplanes of this era include the Curtiss JN 4, the Farman F.60 Goliath, and 
Fokker trimotor. Notable military airplanes of this period include the Mitsubishi A6M Zero, the Supermarine Spitfire and 
the Messerschmitt Bf 109 from Japan, Great Britain, and Germany respectively. A significant development in aerospace 
engineering came with the first operational Jet engine-powered airplane, the Messerschmitt Me 262 which entered service 
in 1944 towards the end of the second World War.

The first definition of aerospace engineering appeared in February 1958.[4] The definition considered the Earth's 
atmosphere and the outer space as a single realm, thereby encompassing both aircraft (aero) and spacecraft (space) under 
a newly coined word aerospace. In response to the USSR launching the first satellite, Sputnik into space on October 4, 
1957, U.S. aerospace engineers launched the first American satellite on January 31, 1958. The National Aeronautics and 
Space Administration was founded in 1958 as a response to the Cold War. In 1969, Apollo 11, the first manned space 
mission to the moon took place. It saw three astronauts enter orbit around the Moon, with two, Neil Armstrong and Buzz 
Aldrin, visiting the lunar surface. The third astronaut, Michael Collins, stayed in orbit to rendezvous with Armstrong 
and Aldrin after their visit to the lunar surface. [11]

An important innovation came on January 30, 1970, when the Boeing 747 made its first commercial flight from New York to 
London. This aircraft made history and became known as the "Jumbo Jet" or "Whale"[12] due to its ability to hold up to 
480 passengers.[13]

Another significant development in aerospace engineering came in 1976, with the development of the first passenger 
supersonic aircraft, the Concorde. The development of this aircraft was agreed upon by the French and British on 
November 29, 1962.[14]

On October 25, 2007, the Airbus A380 made its maiden commercial flight from Singapore to Sydney, Australia. This 
aircraft was the first passenger plane to surpass the Boeing 747 in terms of passenger capacity, with a maximum of 853. 
Though development of this aircraft began in 1988 as a competitor to the 747, the A380 made its first test flight in 
April 2005.[15] """

contador = Counter(texto.split())
elemento = 'the'
if elemento in texto.split():
    print(f"A palavra '{elemento}' aparece {dict(contador)[elemento]} vezes no texto")
else:
    print(f"A palavra '{elemento}' não está no texto")

# As 3 palavras que mais ocorreram no texto
print(contador.most_common(3))
