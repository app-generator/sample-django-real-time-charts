# [Django Charts via DRF](https://blog.appseed.us/django-charts-via-drf-and-charts-js/)

Simple sample project to showcase  `real time data` generation with `Django` and `DRF` using  `Django Channels`, this data is then used to plot different real time charts with `Charts JS` and `bootstrap` in the `front-end`. The charts include `Bar chart`, `Pie Chart` and `Line chart`.
.



> Features:

- `Up-to-date dependencies`
- `Stack`: Django
- `API` via DRF
- `Webprotocol` Http & Websocket
- `Charts`: Chart.js
- `Styling`: BS5 (via CDN)

<br />
> 👉 **Image** 

![charts1](https://user-images.githubusercontent.com/68183305/169057898-cd0148a8-047d-46cf-a586-b378199238d7.png)

<br />


## ✨ How to use it

> 👉 **Clone Sources** (this repo)

```bash
$ git clone https://github.com/app-generator/sample-django-real-time-charts/
$ cd sample-django-real-time-charts
```

```CMD
>> git clone https://github.com/app-generator/sample-django-real-time-charts/
>> cd sample-django-real-time-charts
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

<br />
> 👉 **Image** 

![charts2](https://user-images.githubusercontent.com/68183305/169059259-286f9507-6317-422e-a697-bc56d73b2070.png)


<br />
👉 **Download redis**

Get the latest version of `redis` from https://redis.io/download and follow the installation guides, after installation run `redis-server` to start redis server.

Or for **Windows-based Systems**

On windows, you'll need to get latest redis cli from [https://github.com/tporadowski/redis](https://github.com/tporadowski/redis/releases/), click to download latest reddit package, then doble click on the redis file and open in file explorer after to install, type `c:\program files\redis` on the explorer search bar and click on `redis-cli.exe` and your redis server is opened already.

<br />

> 👉 **Migrate Database**

```bash
$ python manage.py makemigrations
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
