# YandexImageLoader
Loads all images from Yandex image search html file. 
To get this file open your browser, type query and scroll down to see all
the results. Than save the page as html file.

# Installation
pip install yil

# Usage
yil [--help] [--w=<number>] [--out_dir=<output dir>] -f=<html file name> [--pb]

--help - print usage message, <br />
--w=<number> - number of workers for parallel loading, 1 by default, <br />
--pb -show progress bar,  <br />
--f=\<html file name> -html file with search results, <br />
--out_dir=<dir_name> - where store images, ./downloads by default, <br />
in this dir will be saved errors.txt (messages about downloading errors)
and indexes.txt (correspondence between numeric names in out_dir and names in 
the html file)

