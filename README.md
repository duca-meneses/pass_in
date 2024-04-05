<h1 align="center" style="font-weight: bold;">Pass.In Api Rest 💻</h1>

<div align="center">

![python][PYTHON__BADGE]
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
	![SQLite](https://img.shields.io/badge/SQLite-000?style=for-the-badge&logo=sqlite&logoColor=07405E)

</div>

<p align="center">
 <a href="#started">Getting Started</a> •
 <a href="#routes">API Endpoints</a> •
 <a href="#author">Author</a> •
</p>

<p align="center">
  <b>Creating a pass.in api rest with flask</b>
</p>

<h2 id="started">🚀 Getting started</h2>

To get started, follow the steps below

<h3>Prerequisites</h3>

- [python](https://pyhton.org)
- [poetry](https://https://python-poetry.org/docs/)

<h3> Tech Stack </h3>

- python = 3.12
- sqlalchemy
- flask
- flask-cors
- sqlite

<h3>Cloning</h3>

How to clone your project

```bash
git clone https://github.com/duca-meneses/tracks-api.git
```

After cloning the project

```bash
poetry install
```

if you don't use poetry

creating a virtual environment

```bash
python -m venv .venv
```

Activate venv on windows

```bash
.venv/Scripts/activate
```

Active venv on linux/mac

```bash
source .venv/bin/activate
```

Now do the command to install the project dependencies

```bash
pip install -r requirements.txt
```

<h3>Starting</h3>

To start up the flask server

```bash
python app.py
```

<h2 id="routes">📍 API Endpoints</h2>

Here you can list the main routes of your API, and what are their expected request bodies.

| event route             |     description             |
| ----------------------- | :------------------:        |
| GET /events/eventId     |   Get event by eventId      |
| POST /events            |    Create an event          |

| attendees route               |     description       |
| ---------------------------   | :------------------:  |
| GET /events/eventId/attendees | Get event attendees   |
| POSt /events/eventId/register | Register an attendee  |
| GET /attendees/attendeesId/badge | Get an attendee badge |

| check-ins routes |                description            |
| ---------------  | :---------------------------------:   |
| POST /attendees/attendeesId/check-in | Check-in attendee |

<h2 id="author">Author</h2>

<table
  >
  <tr>
    <td align="center">
      <a href="#">
        <img src="https://avatars.githubusercontent.com/u/53846394?v=4" width="100px;" alt="Carlos Eduardo Profile Picture"/><br>
        <sub>
          <b>Carlos Eduardo</b>
        </sub>
      </a>
    </td>
  </tr>
</table>


[PYTHON__BADGE]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54

