# Ztoppuhr

No more uncertainty about how long it<sup>*</sup> took: use
[ZeroSeg](https://thepihut.com/products/zeroseg) as a Stopwatch!

_<sup>*</sup> - it = anything._

## Requirements

Ztoppuhr is a 21st-century Python app, and as such requires Python3.

## Setup / installation

On your Raspberry Pi:

    $ git clone https://github.com/rm-hull/ztoppuhr.git
    $ cd ztoppuhr
    $ sudo apt-get install python3-pip
    $ sudo pip3 install -r requirements.txt

## Running ZTOPPUHR

Just run it on the command-line, enter the following in the _ztopphur_
directory:

    $ ./ztoppuhr.py

Initially the stopwatch shows _0.000_ (0s 0ms). The **Ⓐ** button will
start and pause the stopwatch, while the **Ⓑ** button resets the counter
back to _0.000_... er, that's it.

## References

* https://thepihut.com/products/zeroseg

## License

### MIT License

Copyright (c) 2016 Richard Hull

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
