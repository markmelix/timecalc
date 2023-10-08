# timecalc

Simple time calculator supporting arithmetic priority.

## Installation

``` sh
git clone https://github.com/markmelix/timecalc.git
cd timecalc
chmod +x timecalc.py
poetry install
poetry shell
```

## Examples

``` sh
./timecalc.py "19:00 - 8:00" # stdout: 11:00
./timecalc.py "5:29 - 4:24" # stdout: 01:05
./timecalc.py "1:05 + (5:25 - 6:30)" # stdout: 00:00
```
