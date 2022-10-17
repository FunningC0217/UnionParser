# `unionparser`
- Parsing libraries that separate programming language symbols from text, such as C++/Java/Python,  It is expected to integrate any programming language that can be text.
- It is a back-end program，Implemented using the most popular `IDE` integration protocol `JsonRPC`



## Schematic Diagram of Frame
- All calls are implemented through `JsonRPC` access
```mermaid
graph LR;
  P1[Java Frontend]--JsonRPC-->UP[unionparser]
  P2[Python Frontend]--JsonRPC-->UP[unionparser]
  P3[C/C++ Frontend]--JsonRPC-->UP[unionparser]
  UP-->Ast((Ast files))
  Ast-->A1[Java Sources]
  Ast-->A2[Python Sources]
  Ast-->A3[C/C++ Sources]
```

- Parser source files from initialize

```mermaid
graph LR;
A[Frontend]--cmdline-->UP[unionparser]-->J[JsonRPC]
subgraph Update Ast file
UP-->AST((Ast File))-->UP
end
```

- Watch source files changed

```mermaid
graph LR;
FW[File Watcher]-->UP[unionparser]--JSONRPC-->A[Frontend]
subgraph Update Ast file
UP-->AST((Ast File))-->UP
end
```

- Parent Process watcher

```mermaid
graph LR;
A[Frontend]--cmdline-->UP[unionparser]
UP-->Q{alive}--yes-->UP
Q--no-->exit
```

- Query language tokens

```mermaid
graph LR;
A[Frontend]--JsonRPC-->UP[unionparser]
subgraph Query Ast file
UP-->AST((Ast File))-->UP
end
```