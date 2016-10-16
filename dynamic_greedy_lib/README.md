# Dynamic and Greedy Algorithms 

## Usage

Developed using Python 3.4.

To run a single test:

```
$ sh runner.sh <filename>
$ sh runner.sh greedy/tests/graph_coloring.py
```

To run all tests, pass no arguments:

```
$ sh runner.sh
```

Make sure you run the command from within the same folder as it is located.

## Development guidelines

Keep it simple. Only one public function, called `solve`, which takes an array as argument. 
Other functions should be prefixed with a single underscore.

Check `dynamic/edit_distance.py` for comment header template.

## Authors

### Dynamic Programming
|   Algorithm   	            |     Algorithm (pt-BR)     	|       File       	|  Author  	|
|:-------------:	            |:-------------------------:	|:----------------:	|:--------:	|
| Binomial Coefficient          |    Triângulo de Pascal    	| binomial_coefficient.py |  Jaelson 	|
| Coin Change                   |      Troco em moedas      	| coin_change.py   	| Fernando 	|
| Knapsack 	                    |      Mochila binária      	| knapsack.py       |  Jaelson 	|
|               	            |   Empilhamento de caixas  	|         -        	|     -    	|
| Floyd Warshall All Pairs Shortest Path | Caminho mais curto   | shortest_path.py 	| Fernando 	|
| Word Break      	            |     Quebra de palavras    	| word_break.py 	|  Jaelson 	|
|               	            |  Maior subsequência comum 	|                  	| Jorismar 	|
|               	            |    Soma de subconjunto    	|                  	| Jorismar 	|
|               	            | Multiplicação de matrizes 	|                  	| Jorismar 	|
| Edit Levenshtein Distance     |    Distância de edição    	| edit_distance.py 	| Fernando  |

## Greedy Programming
|   Algorithm   	            |     Algorithm (pt-BR)                            	|       File            |  Author  	|
|:-------------:	            |:----------------------------------------------:	|:-------------:        |:--------:	|
| Dijkstra’s Shortest Path      | Caminho mais curto (Algoritmo de Dijkstra) 	    | shortest_path.py      | Fernando 	|
|   	                        | Árvore geradora mínima (Algoritmo de Kruskal) 	|   	                | Jorismar 	|
|   	                        | Árvore geradora mínima (Algoritmo de Prim)    	| - 	                | -        	|
| Huffman Coding                | Compressão de dados (Código de Huffman)       	| huffman_coding.py     | Jaelson  	|
| Activity Selection            | Seleção de atividades                         	| activity_selection.py | Jaelson  	|
|   	                        | Mochila fracionária                           	|   	                | Jorismar 	|
| Graph Coloring                | Coloração de grafos                           	| graph_coloring.py     | Fernando 	|

## Credits

Most of the implementations are inspired on explanations and solutions from http://www.geeksforgeeks.org/.
