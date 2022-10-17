# `UnionParser`
- Parsing libraries that separate programming language symbols from text, such as C++/Java/Python,  It is expected to integrate any programming language that can be text.
- It is a back-end program，Implemented using the most popular `IDE` integration protocol `JsonRPC`



## Schematic Diagram of Frame
- All calls are implemented through `JsonRPC` access
```mermaid
graph LR;
  P1[Java Frontend]--JsonRPC-->UP[Union Parser]
  P2[Python Frontend]--JsonRPC-->UP[Union Parser]
  P3[C/C++ Frontend]--JsonRPC-->UP[Union Parser]
  UP-->Ast((Ast files))
  Ast-->A1[Java Sources]
  Ast-->A2[Python Sources]
  Ast-->A3[C/C++ Sources]
```

- Parser source files from initialize

```mermaid
graph LR;
A[Frontend]--cmdline-->UP[Union Parser]-->J[JsonRPC]
subgraph Update Ast file
UP-->AST((Ast File))-->UP
end
```

- Watch source files changed

```mermaid
graph LR;
FW[File Watcher]-->UP[Union Parser]--JSONRPC-->A[Frontend]
subgraph Update Ast file
UP-->AST((Ast File))-->UP
end
```

- Parent Process watcher

```mermaid
graph TD;
A[Frontend]--cmdline-->UP[Union Parser]
UP-->Q{alive}--yes-->UP
Q--no-->exit
```

- Query language tokens

```mermaid
graph LR;
A[Frontend]--JsonRPC-->UP[Union Parser]-->J[JsonRPC]
subgraph Query Ast file
UP-->AST((Ast File))-->UP
end
```