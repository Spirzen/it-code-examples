
import std/[strutils, tables, sequtils]

proc wordCount(text: string): Table[string, int] =
  result = initCountTable[string]()
  for w in text.splitWhitespace():
    let key = w.toLowerAscii()
    if key.len > 0:
      result.inc(key)

when isMainModule:
  let sample = "Nim Nim nim — быстрый Nim"
  let counts = wordCount(sample)
  for word, n in counts.pairs:
    echo word, ": ", n
