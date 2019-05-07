# N Queens Puzzle

## Coding Challenge

Here's the programming problem: https://en.wikipedia.org/wiki/Eight_queens_puzzle

These are the different aspect of the project you can work on (in order):

1. Determine all possible solutions for a given N where N ≥ 8 (within 10 mins on a laptop).

**Note:** Bonus points for a higher N where N is the size of the board / number of queens.

2. Iterate over N and store the solutions in Postgres using SQLAlchemy.

3. Write basic tests that at least verify the number of solutions for a given N match what's online.

**Note:** I recommend using pytest.

4. Docker-ize the solution, so that I can run the code and tests without any assumption of my local setup.

**Note:** Including running a Postgres instance in docker-compose.

5. Setup Travis CI (or similar) for your public GitHub repo to run the tests automatically.

## Solution

### Requirements/Dependencies

+ git version 2.7.4

Installation: https://git-scm.com/downloads

+ Docker version 18.09.0

Installation: https://docs.docker.com/install/#server

+ docker-compose version 1.23.2

Installation: https://docs.docker.com/compose/install/#prerequisites

### Clone Repository and Build the Application

+ Clone the solution repository.

+ Access the solution directory with the following command:

```bash
cd SOLUTION_DIRECTORY
```

+ Build the application, running the following command:

```bash
sudo docker-compose build
```

### Run for first time the Application

+ To start for first time the application, please run the following command:

```bash
sudo docker-compose up -d
```

+ The final step is create the local settings file.

Please, create a new file called "local_settings.py" in "n-queens-puzzle/core/config".

Copy the information from the file "local_settings_template.py" into it.

Change the information corresponding to the configuration that you did before.

### Run the Application

You have two ways to run the application.

First way, please run the following commands:

```bash
sudo docker-compose exec web bash
python main.py
```

Second way, please run the following command:

```bash
sudo docker-compose exec web bash -c 'python main.py'
```

### Run the Unit Tests

Ypu have two ways to run the unit tests.

First way, please run the following commands:

```bash
sudo docker-compose exec web bash
python -m pytest tests.py
```

Second way, please run the following command:

```bash
sudo docker-compose exec web bash -c 'python -m pytest tests.py'
```
