# Execution Engines

| Engine             | Main Use Case                   | JIT?    | Optimizing Compiler  | Special Note                 |
| ------------------ | ------------------------------- | ------- | -------------------- | ---------------------------- |
| **V8**             | Chrome, Node.js, Deno           | ✅       | TurboFan             | Fastest in most benchmarks   |
| **SpiderMonkey**   | Firefox, Thunderbird            | ✅       | IonMonkey + Warp     | First JS engine ever         |
| **JavaScriptCore** | Safari, iOS, React Native (iOS) | ✅       | FTL JIT (LLVM-based) | Low memory footprint         |
| **Chakra**         | Legacy Edge                     | ✅       | FullJIT              | Dead after Edge Chromium     |
| **Hermes**         | React Native (mobile)           | ❌ (AOT) | None (AOT only)      | Best for mobile startup time |
| **GraalJS**        | GraalVM, server-side polyglot   | ✅       | Graal Compiler       | Polyglot support             |


---
