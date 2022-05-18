# [Django Charts via DRF](https://blog.appseed.us/django-charts-via-drf-and-charts-js/)

Simple project to showcase how to generate `real time data` with `Django`, `DRF` and  `Django Channels`, this data is then used to plot different charts with `Charts JS` in the `front-end`.
.



> Features:

- `Up-to-date dependencies`
- `Stack`: Django
- `API` via DRF
- `Webprotocol` Http & Websocket
- `Charts`: Chart.js
- `Styling`: BS5 (via CDN)

<br />


## ✨ How to use it

> 👉 **Clone Sources** (this repo)

```bash
$ git clone https://github.com/app-generator/sample-django-charts-js.git
$ cd sample-django-charts-js
```

<br />

> 👉 **Install Modules** using a Virtual Environment

```bash
$ virtualenv env
$ source env/bin/activate
$ pip3 install -r requirements.txt
```

Or for **Windows-based Systems**

```bash
$ virtualenv env
$ .\env\Scripts\activate
$
$ # Install modules - SQLite Database
$ pip3 install -r requirements.txt
```

👉 **Download redis**

Get the latest version of `redis` from https://redis.io/download and follow the installation guides, after installation run `redis-server` to start redis server.

Or for **Windows-based Systems**

On windows, you'll need to get redis cli, click to download latest reddit package, then doble click on the redis file and open in file explorer after to install, type `c:\program files\redis` on the explorer search bar and click on `redis-cli.exe` and your redis server is opened already.

<br />

> 👉 **Migrate Database**

```bash
$ python manage.py migrate
$ python manage.py runserver
```

<br />

> 👉 **Create Superuser**

```bash
$ python manage.py createsuperuser
```

<br />

> 👉 **Start the APP**

```bash
$ python manage.py runserver
```

<br />

> The bootstrap flow

- Access the `admin` section 
  - Load `data/users.csv` in users table (using import/export feature)
  - Load `data/products.csv` in users table (using import/export feature)
- Access the HOMEpage 
  - Charts should be displayed with data

<br />

> Navigations

 - Access all api at  `localhost:8000/all/`
 - Add new instance to the Product model at `localhost:8000/create/`
