## How to resize local LLM context window?

Easy!

Create a `Modelfile` pointing to your model of interest:
```Dockerfile
# Modelfile
FROM gemma3:27b
PARAMETER num_ctx 131072
```
(**it'll unlock full 128k potential of gemma**)


And trigger it:

`ollama create -f Modelfile gemma3:27b`

Host it:

`ollama serve`

### Tests

3090 24 gb vram + 80 gb ram

```bash
context size:
8192 -> default
24576 -> sweet spot
32768 -> takes some time to load
65536 -> danger zone
131072 -> too much (ram overflow)
```