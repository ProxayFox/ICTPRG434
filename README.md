# Tafe Assignment
# How to Install and Run
## Prerequisites
### Software Requirements
 - Python 3.12
 - PIPx
 - Poetry
### Libraries
  - Psutil-6.1.0
  - Libraries included with Python 3.12
### Tools
 - CLI Access

## Installation Instructions
### Nixos or with NixPKG Manager
1. Create the nix env
    ```bash
    nix-shell
    ```
2. Build Poetry Environment and dependencies
    ```bash
    poetry install
    ```
3. Run the Script and get the resulting data
    ```bash
    poetry run main
    ```

### Linux :: [Ensure Git is installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git#_installing_on_linux)
1. Install the Nix Package Manager
    ```bash
    sh <(curl -L https://nixos.org/nix/install) --daemon
    ```
2. Download Repo
    ```bash
    git clone https://github.com/ProxayFox/ICTPRG434
    ```
2. Build the nix environment
    ```bash
    nix-shell
    ```
3. Build Poetry Environment and dependencies
    ```bash
    poetry install
    ```
4. Run the Script and get the resulting data
    ```bash
    poetry run main
    ```
    Results will show in a file called hostData.csv
### Windows
1. Install python 3.12 and git
    ```powershell
    winget install -e --id Python.Python.3.12
    winget install git.git
    ```
2. Install Poetry <br>
    `you may need to open and close the terminal to get environment veriables reset`    
    ```powershell
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
    scoop install pipx
    pipx ensurepath
    pipx install poetry
    ```
3. Build Poetry Environment and dependencies
    ```bash
    pipx run poetry install
    ```
4. Run the Script and get the resulting data
    ```bash
    pipx run poetry run main
    ```
    Results will show in a file called hostData.csv

### Unable to get Poetry working
1. Ensure Python 3.12 is installed
2. Open and edit `ictprg434/main.py`
3. Go to the very bottom of the script and uncomment the `print(start())`
    From 
    ```python
    # print(start())
    ```
    to
    ```python
    print(start())
    ```
4. Install psutils
    ```bash
    py -m pip install psutils
    ```
5. Run the script
    then run 
    ```bash
    py ./ictprg434/main.py
    ```
## Usage Instructions:
This is outlined in the README.md of the code’s directory
### Linux:
```bash
poetry run main
```
### Windows:
```bash
pipx run poetry run main
```
### Without Poetry:
```bash
py ./ictprg434/main.py
```
