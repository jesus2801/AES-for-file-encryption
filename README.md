# AES algorithm for files encryption and decryption
This repository is a Python executable to create a basic manager for utf-8 files encryption and decryption via CLI.

## Get Started
**⚠️You should have Python installed.⚠️**  
**⚠️This tutorial works on Linux⚠️**  
If you are not on Linux, try to look for the equivalences in your OS.

Set up virtual enviroment:
```
python -m venv env
source env/bin/activate
```

Install dependencies:
```
pip install -r requirements.txt
```

## Run executable
Make the file executable:
```
sudo chmod +x ./AES
```

Run the example (with tests/index.html):
```
./AES cipher -p secret --salt salt --size 128 -i tests/index.html -o tests/index.html
./AES decipher -p secret --salt salt --size 128 -i tests/index.html.enc -o tests/index.html
```

## Environment Variables

To run this project, you will need to add the following environment variable to your .env file: `IV=`. You can generate a random value with:
```
python scripts/iv.py
```

The reason why the IV is stored is because it should be the same when encrypting and decrypting (exactly like the key)

## Tips
If you want to leave your virtual enviroment:
```
deactivate
```

## Authors
- [@jesus2801](https://github.com/jesus2801)


## License
[MIT](https://choosealicense.com/licenses/mit/)