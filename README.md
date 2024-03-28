# kiu_test

## Challenge

Dado el siguiente Sistema:

Una compañía Aérea se dedica al negocio de transporte de cargas aéreas entre diferentes orígenes y destinos.

La compañía solo puede transportar paquetes de Clientes.

Por cada paquete transportado la compañía aérea cobra 10$

Debe existir un método que genere un reporte con el total de paquetes transportados y el total recaudado para un día determinado.

Se pide:

* Programar en Python las clases y responsabilidades del sistema, crear los testeos unitarios que consideren necesarios.
* No utilizar ningún framework ni base de datos en la solución (mantener una solución sencilla).

## Usage

All the project is developed using Python built-in libraries. So no instalations or virtual environment is needed.

There is a small HTTP server embedded within the main program to get the daily package report. This report lists:
 * The request date to report
 * Total packages
 * Total money collected
 * And a list of all the packages with some detail about them

 ### Run Server

 To run the server from your console execute

 ```bash
cd .../kiu_test
python main.py
 ```

 This will populate the date base with some dummy data for testing purposes and run the server:

 ```
 $ python main.py 
 Data base populated with dummy data, existing dates:
        * 2024-01-08
        * 2024-02-15
        * 2024-03-17


Server started http://localhost:8080
 ``` 

The dates displayed are the ones prepolulated in the database that may queried.

### Get the daily packages report

After running executing main, you can GET the report from your browser with the link [http://localhost:8080](http://localhost:8080).
This will show you the report for the current day (today).

For checking other date's reports you may add querys to the url with the year, month and day:

[http://localhost:8080/?year=2024&month=02&day=15](http://localhost:8080/?year=2024&month=02&day=15)

### Add entries to the database

Using POST requests to the models endpoints it is posible add entries to the database.
Example using curl program:

```bash
# Adding a Client
curl -d '{ "name": "Lolo" }' localhost:8080/client

# Adding two Airports
curl -d '{ "name": "Aeroparque" }' localhost:8080/airport
curl -d '{ "name": "Ezeiza" }' localhost:8080/airport

# Adding a Travel
curl -d '{"destination":"Aeroparque", "origin":"Ezeiza", "date":"2024-06-16"}' localhost:8080/travel

# Adding a Package
curl -d '{ "travel": 4, "client": "Lolo" }' localhost:8080/package
```

After executing above comments, if going to [http://localhost:8080/?year=2024&month=02&day=15](http://localhost:8080/?year=2024&month=06&day=16)
will at least bring up the package just added.

## Modules

The main modules of the poject are
 
 ### database

A simple In Memory Database was created to be able to store and fetch data.
The class `InMemDB` is implemented with a Singleton pattern desing to be able to instanciate the same object from all the project.
It has three simplified methods:
 * `add()` To add entries
 * `select()` To select entries with filter option
 * `exist()` To check if an item exists in the DB

 ### kiu

Kiu module is where the system logic should be placed. Responses to requests, etc.

 ### models

Definition of all models used in the system. Every module shall inherit `BaseModule` class, define fields if it has and redifine the `validators` method if any input needs validation.

 ### tests

 System tests suite. Implemented with `unittest`

## Run tests

From console run:

```bash
cd .../kiu_test
python -m unittest tests
```