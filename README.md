## saucelab-api-client ##

saucelab-api-client - is a client for provide integration with SauceLab

General information about [SauceLab Api](https://docs.saucelabs.com/dev/api/)

**Requirements**
- requests

**Installation**
```shell
pip install saucelab-api-client
```

**Configuration**
```shell
from saucelab_api_client.saucelab_api_client import SauceLab
saucelab = SauceLab('your_host', 'your_username', 'your_token')
```
**Features in version: 0.1**
- Supported api:
  - accounts
  - jobs
  - platform
  - real devices
  - storage
- Powerful device filter - saucelab.devices.filter_devices()

**TODO**
- Add support:
  - sauce connect
  - insights
  - performance

**Usage examples**
```shell
teams = saucelab.accounts.account_team.teams()
devices = saucelab.devices.filter_devices(min_os_version='14.4.1', max_os_version='14.9')
apps = saucelab.storage.files()
```
