Notes:

Attention is a communication mechanism. Can be seen as nodes in a directed graph looking at each other and aggregating information with a weighted sum of all nodes that poitn to them, with data dependant weights.

There is no notion of space. Attention simpy acts over a set of vectors. This is why we need to positionally encode tokens.

Each example across batch dimension is ofcourse processed completely independant and never talk to each other

"self-attention" means that the keys and values produced in the same pool of nodes.
"cross-attention" refers to a separate pool of nodes for the keys and a separate pool for the values.