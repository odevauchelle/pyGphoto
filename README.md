# pyGphoto

Yet another convenience python wrapper for [gphoto2](http://www.gphoto.org/). Compare with [this](https://github.com/jcarnu/pygphotoshot) and [this](https://github.com/Soreine/pygphoto).

Tested only with an EOS 600D Canon Digital Camera.

## Simple example

```python
import pyGphoto as pgp

print( pgp.get_picture( filename = 'test.jpg' ).stdout.decode() )
```

## Tips

To stream a liveview:
```
gphoto2 --capture-movie --stdout | vlc -
```
