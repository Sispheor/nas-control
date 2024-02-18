# NAS control

## Install

```
git clone https://github.com/Sispheor/nas-control.git
cd nas-control
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirments.txt
```

## Token

Generate a token
```python
import secrets
secrets.token_hex(16)
'29717e76xxxxxxxxx855b'
```

Place the token in the `secrets.sh` file

## Allow user to execute restart of kodi

Run `visudo` and add following:
```
nico ALL=NOPASSWD: /bin/systemctl restart kodi
```

## RUN

Run
```
source secret.sh 
source .venv/bin/activate
flask --app main run --host=0.0.0.0
```

## Usage

Test with curl

Export the token
```
export TOKEN=29717e76xxxxxxxxx855b
```

Access index page
```
curl --insecure -i -X GET --header "x-access-tokens: $TOKEN"  https://localhost:5000/
```

Restart Kodi
```
curl --insecure -i -X POST --header "x-access-tokens: $TOKEN"  https://localhost:5000/kodi/restart/
```

## Auto start

Update the working dir from the `nas-control.service` file.

Install the systemd service
```
cp nas-control.service /etc/systemd/system/nas-control.service
systemctl daemon-reload
systemctl start nas-control
systemctl enable nas-control
```
