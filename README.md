1. Clone this repository and create a virtual-env in the same directory

```sh
cd django-docx-import
python3 -m venv venv
```
2. Activate your virtual-env:

Windows:

```sh
venv\Scripts\activate
```
if it doesent work powershell:
```sh
Set-ExecutionPolicy -ExecutionPolicy AllSigned
```
#terminal
```sh
venv\Scripts\activate
```
```sh
Set-ExecutionPolicy -ExecutionPolicy Restricted
```


Linux:

```sh
source venv/bin/activate
```

3. Install required Python modules

```sh
pip3 install -r requirements.txt
```

4. Finally run your server

```sh
python3 manage.py runserver
```