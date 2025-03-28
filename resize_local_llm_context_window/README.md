## How to resize local LLM context window?

Easy!

Create a `Modelfile` pointing to your model of interest:
```
# Modelfile
FROM gemma3:27b
PARAMETER num_ctx 131072
```
(it'll unlock full 128k potential of gemma)


And trigger it:

`ollama create -f Modelfile gemma3:27b`

Host it:

`ollama serve`