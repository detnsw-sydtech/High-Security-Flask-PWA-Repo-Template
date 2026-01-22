# Codespace Procedures -- starting Python, uv, venv, installing dependencies

## Step 0 -- This will make your flask app run (but do this after the other steps)
In codespace, the following command will fire up a link that you click on to see your flask app front page.

```bash
uv run flask run --host=0.0.0.0 --port=5000
```


## 🧭 Step 1 — Install Python (Codespaces base image doesn’t include it)
Run
```bash
sudo apt-get update
sudo apt-get install -y python3 python3-venv python3-pip
```
Then confirm:
```bash
python3 --version
```
You should see something like:
```code
Python 3.12.x
```


## 🧭 Step 2 — Install uv (fresh Codespaces never includes it)
Install uv:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
Reload your shell so PATH updates:
```bash
source ~/.profile
```
Confirm:
```bash
uv --version
```
If that prints a version, uv is ready.



## 🧭 Step 3 — Create your virtual environment
Your script is correct: it expects ```.venv``` to exist.
Create it:
```bash
uv venv
```
Then activate it:
```bash
source .venv/bin/activate
```
Confirm:
```bash
python --version
which python
```
You should see ```.venv/bin/python```.



## 🧭 Step 4 — Sync dependencies
Now install everything from your ```pyproject.toml```:
```bash
uv sync
```
This installs Flask, SQLAlchemy, your extensions, everything.



## 🧭 Step 5 — Run your dev-start script again
```bash
./scripts/dev-start.sh
```

## Remember
A fresh Codespace:

- does not include Python
- does not include uv
- does not include your .venv
- does not preserve executable bits on scripts

Your workflow is correct — the environment just needed to be rebuilt.


