# cmake-to-dot

As if cmake 3.17 the result of cmake --graphviz is incomplete, in the sense that it does not export all dependencies.
Specifically, if A -> B -> A (project A depends on project B, and project B depends on project A) only one direction of the relationship is written.
Contrary, if A -> B -> C -> A then those relations _are_ correctly written.

cmake_to_dot.py is a hack to transform CMake's 'target_link_libraries' into a graphviz .dot files.

To be able to specifically find these cyclic dependencies, try:

```cat `find . -name CMakeLists.txt` | ./cmake_to_dot.py | ./dot_find_cycles.py```


