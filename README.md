# `unionparser`
- Parsing program that separate programming language symbols from text, such as C++/Java/Python,  It is expected to integrate any programming language that can be text.
- It is a back-end program，Implemented using the so easy `IDE` integration from file tree



## Schematic Diagram of Frame
- display symbol file tree
```mermaid
graph LR;
  P1[Java Frontend]-->T((File Tree))
  P2[Python Frontend]-->T((File Tree))
  P3[C/C++ Frontend]-->T((File Tree))
  T-->A1[Java Sources]
  T-->A2[Python Sources]
  T-->A3[C/C++ Sources]
```

- Parser source files from initialize

```mermaid
graph LR;
A[Frontend]--cmdline-->UP[unionparser]
subgraph Update File Tree
UP-->T((File Tree))-->UP
end
```

- Watch source files changed

```mermaid
graph LR;
subgraph Update File Tree
FW[File Watcher]-->UP[unionparser]-->T((File Tree))
end
T((File Tree))-->A[Frontend]
```

- Parent process watcher

```mermaid
graph LR;
A[Frontend]--cmdline-->UP[unionparser]
UP-->Q{alive}--yes-->UP
Q--no-->exit
```

- Query language tokens

```mermaid
graph LR;
A[Frontend]-->T((File Tree))
```
