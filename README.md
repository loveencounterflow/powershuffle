Well I couldn't leave it alone there must be a faster way....

I have one, read a few lines of the file and get an avarage bits per line and the total file size.
Now move the file pointer between bit 0 and the estimated last bit and read a line.

## Usage

Run this tool from the cli like any other python script.

```
$ ./powershuf.py --help                             
usage: powershuf.py [-h] --file FILE -n N [--min-len MINLEN] [--max-len MAXLEN]

Returns random lines from text files, as fast as possible.

optional arguments:
  -h, --help        show this help message and exit
  --file FILE       the file to parse
  -n N              amount of lines you want to return
  --min-len MINLEN  minimum line length, defaults to 0
  --max-len MAXLEN  maximum line length, defaults to ∞
```


## Results:

```txt
# svanbroekhoven @ lynx in ~/git/shuf on git:master x [0:41:59] 
$ time shuf -n 10 lines_tester.txt > /dev/null
shuf -n 10 lines_tester.txt > /dev/null  1.73s user 0.04s system 99% cpu 1.774 total

# svanbroekhoven @ lynx in ~/git/shuf on git:master x [0:44:24] 
$ time ./powershuf.py -n 10 --file lines_tester.txt > /dev/null 
./powershuf.py -n 10 --file lines_tester.txt > /dev/null  0.02s user 0.00s system 98% cpu 0.024 total

# svanbroekhoven @ lynx in ~/git/shuf on git:master x [0:44:50] 
$ time ./powershuf.py -n 10 --file lines_78000000000.txt > /dev/null 
./powershuf.py -n 10 --file lines_78000000000.txt > /dev/null  0.02s user 0.01s system 80% cpu 0.047 total

# svanbroekhoven @ lynx in ~/git/shuf on git:master x [0:46:11] 
$ time ./powershuf.py -n 10 --file actual_dataset.csv > /dev/null 
./powershuf.py -n 10 --file actual_dataset.csv > /dev/null  0.16s user 0.02s system 99% cpu 0.179 total

# svanbroekhoven @ lynx in ~/git/shuf on git:master x [0:46:20] 
$ time shuf -n 10 actual_dataset.csv > /dev/null
shuf -n 10 actual_dataset.csv > /dev/null  8.27s user 1.81s system 99% cpu 10.149 total
```

## Output warning

The `-n` parameter will set the desired output to exactly the amount of lines you've asked for even if the input file has less lines and will create duplicates in the results if set above the actual line total.


![Hits](https://hitcounter.pythonanywhere.com/count/tag.svg?url=https%3A%2F%2Fgitlab.com%2Faapjeisbaas%2Fshuf)
![Google Analytics](https://www.google-analytics.com/collect?v=1&tid=UA-48206675-1&cid=555&aip=1&t=event&ec=repo&ea=view&dp=gitlab%2Fshuf%2FREADME.md&dt=shuf)