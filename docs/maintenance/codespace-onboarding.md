# Getting Started in Your Codespace

This project is designed to **set itself up for you**.  
Most of the time, you just open the Codespace and start coding.

## What happens automatically

When your Codespace is created:

1. **uv is installed**  
2. **A virtual environment (`.venv`) is created**  
3. **All dependencies are installed**  
4. **Basic checks run** to make sure Python and uv are correct  

When your Codespace starts:

1. **Old VM cache is cleaned** (to keep things fast and stable)  
2. **Diagnostics run** (so staff can help if something breaks)  
3. **The Flask app starts** on port `5000`  

You’ll usually see a prompt telling you the app is running and a link to open it in the browser.

---

## Common commands you might use

**From the terminal in the Codespace:**

- **Check environment health**
```bash
bash .devcontainer/scripts/diagnostics.sh
```
This will show:
- Python version
- uv version
- virtual environment status
- installed packages
- whether Flask is running
- whether port 5000 is active

If something feels “off”, run this first.

- **Rebuild the virtual environment (if something feels “off”)**
```bash
bash .devcontainer/scripts/rebuild-venv.sh
```
Use this if:
- dependencies seem broken
- you see weird import errors
- you’ve been told to “reset your environment”
This will:
- Delete .venv
- Create a fresh virtual environment
- Reinstall all dependencies with uv sync

- **Run the app again (if you stopped it)**
Start the Flask app (if it’s not running)
Normally the app starts automatically when the Codespace starts.
If you’ve stopped it or something crashed, you can run:
```bash
bash .devcontainer/startup.sh
```
This will:
- activate ```.venv```
- run ```uv sync```
- start Flask on port ```5000```


## When to ask for help
If you see errors about:
- Python version mismatch
- uv not installed
-.venv missing

**When something looks wrong**
If you see errors about:
- **Python version mismatch**
- **uv not installed**
- **.venv missing**
Do this:
1. Run diagnostics:
```bash
bash .devcontainer/scripts/diagnostics.sh
```
2. If it still looks broken, try a full reset:
```bash
bash .devcontainer/scripts/rebuild-venv.sh
```
3. If it’s still not right, copy the diagnostics output and share it with your teacher.


Then copy the output and share it with your teacher.
This gives enough information to fix your environment quickly.
You are not expected to debug everything yourself.
The scripts are there to give clear signals about what’s wrong.


## Golden rule
If you’re not sure what to do:
1. Run diagnostics
2. Read the messages
3. Ask for help with the output

You don’t need to be a DevOps engineer to use this project — the container is doing the heavy lifting for you.
---
