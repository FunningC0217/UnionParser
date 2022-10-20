# `unionparser`
- Parsing program that separate programming language symbols from text, such as C++/Java/Python,  It is expected to integrate any programming language that can be text.
- It is a back-end program，Implemented using the so easy `IDE` integration from file tree
- It will solve the problem of symbols in the strong workspace mode of the IDE. Because LSP services are usually used as the back-end in existing IDEs, and symbols can be synchronized only when documents are opened. You cannot get all the symbols when you open the workspace at the beginning.
- For the current program, try to keep the current program lightweight, and only support the symbols in the source file. If you need any symbols other than the source file, it is not supported. If you want to obtain relevant support, you can check the relevant usage of the document/symbol of the native LSP Server.


## Schematic Diagram of Frame
- display symbol file tree
```mermaid
graph LR;
  P1[Java Frontend]-->S((Symbol Tree))
  P2[Python Frontend]-->S((Symbol Tree))
  P3[C/C++ Frontend]-->S((Symbol Tree))
  S-->A1[Java Sources]
  S-->A2[Python Sources]
  S-->A3[C/C++ Sources]
```

- Parser source files from initialize

```mermaid
graph LR;
A[Frontend]--cmdline-->UP[unionparser]
subgraph Update File Tree
UP-->S((Symbol Tree))-->UP
end
```

- Watch source files changed

```mermaid
graph LR;
subgraph Update File Tree
FW[File Watcher]-->UP[unionparser]-->S((Symbol Tree))
end
S((Symbol Tree))-->A[Frontend]
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
A[Frontend]-->S((Symbol Tree))
```
