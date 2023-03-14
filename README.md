<h1>Deterministic & Nondeterministic Finite Automata</h1>
<h2>A program to determine acceptance of a word</h2>
<img src='https://user-images.githubusercontent.com/65015373/225086828-b11a0344-777c-4062-a97b-a5476e154b13.png'>
<br>
<hr>
<h2>About it</h2>

<p>The purpose of this program is to determine whether a word is accepted by a given DFA or NFA.</p>

<br>
<hr>
<h2>How to use it</h2>

<p>It has builtin a CLI with 3 options: </p>
<ul>
    <li>Read a DFA</li>
    <li>Read a NFA</li>
    <p>- Both of them open a window to select a text file that contains the graph for the automata.</p>
    <li>Process a word - read from the STDIN a word and prints whether is it accepted or not.</li>
</ul>

<h3>The text format</h3>
<p>The automata expects the input to have this specific format: </p>
<code>node_number _ is_final _ next_node _ letter _ ... </code>

<br>
<p>Where: </p>
<ul>
    <li>the node number - represents a positive integer for that specific node</li>
    <b>Note that the <i>node 0</i> will be always consider the starting node!</b>
    <li>is_final - a boolean that marks if the node is a terminal one. This should be written as <code>f</code> for a final one and <code>n</code> for a non-terminal one. </li>
    <li>next_node - represents a positive integer for the next node adjacent</li>
    <li>letter - is the corresponding letter from the automata's alphabet(it could be also any symbol) that lies on the edge of the connection</li>
    <li>The three dots marks that we can have any number of nodes linked to this node.</li>
</ul>

<p>Every <b>node</b> along with its content should be written on a different line.</p>

<p>The program accepts non-completed automata, but must have all nodes declared at least.</p>


<h3>Example</h3>

<p>Suppose that we have this automata:</p>
<img src = 'https://user-images.githubusercontent.com/65015373/225073729-e3a79033-3df7-4738-9bc2-fc5f20fec8b2.png' style = "background:black;">

<p>The input file for this would be:</p>

<code >
0 n 0 1 1 0<br>
1 f 2 0 0 1<br>
2 n 3 2<br>
3 f
</code>

<p>But if we wanted a complete automata we would complete the edges with a <code>-1</code> node that coresponds for the <b>abort state</b>.</p>

<code>
0 n 0 1 1 0 -1 2<br>
1 f 2 0 0 1 -1 2<br>
2 n 3 2 -1 0 -1 1<br>
3 f -1 0 -1 1 -1 2
</code>


<br>
<hr>
<h2>How it works</h2>

<p>The program simulates an automata behavior, taking one letter at a time and decides the next node.</p>


<br>
<hr>
<h2>Tech specs</h2>

<p>It has implemented 2 main classes: </p>
<ul>
    <li>Node class - that represents a node in the automata's graph</li>
    <li>FA class(stands for Finate Automata) - storing the component nodes</li>
</ul>

<p>The DFA and NFA classes inherits from the FA and adds the main functionallity, <b>validate_word</b> method, which differs between them.</p>

<p>The word validation in a NFA is done by running a backtracking through all nondeterministic nodes, whereas in a DFA is a liniar lookup.</p>

<p>The adjacent nodes are stored as an array of indices that corresponds to the node.
<br>Example:<br>
0 coresponds to node 0, 1 to node 1, ...</p>


<p>The file selector is done using the <b>tkinter</b> module, the root windows is hidden.</p>

