a libre front-end for mozilla firefox addons site
---

# how to run

## using docker

```bash
docker build --tag mozilfun .
docker run mozilfun
```

## classic way

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirments.txt
python3 mozilfun.py
```