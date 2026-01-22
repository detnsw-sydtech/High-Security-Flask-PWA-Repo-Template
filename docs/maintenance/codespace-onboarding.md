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
- **Rebuild the virtual environment (if something feels “off”)**
```bash
bash .devcontainer/scripts/rebuild-venv.sh
```

- **Run the app again (if you stopped it)**
```bash
bash .devcontainer/startup.sh
```

## When to ask for help
If you see errors about:
- Python version mismatch
- uv not installed
-.venv missing

Run:
```bash
bash .devcontainer/scripts/diagnostics.sh
```
Then copy the output and share it with your teacher.
This gives enough information to fix your environment quickly.


## Golden rule
If you’re not sure what to do:
1. Run diagnostics
2. Read the messages
3. Ask for help with the output

You don’t need to be a DevOps engineer to use this project — the container is doing the heavy lifting for you.

---


---

### “Reset environment” VS Code task

Create (or extend) `.vscode/tasks.json`:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Reset environment (uv + venv)",
      "type": "shell",
      "command": "bash .devcontainer/scripts/install-uv.sh && bash .devcontainer/scripts/rebuild-venv.sh",
      "problemMatcher": [],
      "presentation": {
        "reveal": "always",
        "panel": "dedicated"
      }
    },
    {
      "label": "Run diagnostics",
      "type": "shell",
      "command": "bash .devcontainer/scripts/diagnostics.sh",
      "problemMatcher": [],
      "presentation": {
        "reveal": "always",
        "panel": "shared"
      }
    }
  ]
}
```

You can then:
- open the Command Palette → “Run Task”
- choose “Reset environment (uv + venv)” when things are broken
- choose “Run diagnostics” when they need to show you what’s happening
- 
