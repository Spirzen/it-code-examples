
import std/httpclient

proc fetchPreview(url: string; maxLen = 200): string =
  let client = newHttpClient()
  defer: client.close()
  client.timeout = 10_000
  let body = client.getContent(url)
  if body.len <= maxLen:
    body
  else:
    body[0 ..< maxLen] & "..."

when isMainModule:
  echo fetchPreview("https://example.com")
