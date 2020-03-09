![CI](https://github.com/uwenergynetwork/energyhacks-backend/workflows/CI/badge.svg)
Instructions to connect to DB
* Run `./cloud_sql_proxy -instances=uwenca:us-central1:energyhacks-2020=tcp:3306`
* If the above command doesn't work in Google Cloud SDK Shell, use: `"cloud_sql_proxy.exe" -instances=uwenca:us-central1:energyhacks-2020=tcp:3306`
* On your prefered SQL Studio, connect to localhost:3306 and use password.
* `https://dbeaver.io/` is good.


Run tests
* `python -m pytest` 
* (Running tests not working on GitHub, please run locally!)
