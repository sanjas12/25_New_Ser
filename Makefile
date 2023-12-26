.PHONY: run

build:
    python setup.py build

run:
    make -f Makefile.win run
    python -m dotenv bot.py