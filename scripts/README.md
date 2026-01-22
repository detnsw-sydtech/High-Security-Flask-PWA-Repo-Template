# #Useful tips
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


## 🧭 Step 3 — Create your virtual environment
Your script is correct: it expects ```.venv``` to exist.




