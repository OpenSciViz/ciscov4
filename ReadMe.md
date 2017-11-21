This Readme content create by: python -c 'import euclid ; help(euclid)'

chkSys> 2.7
completed system check ... python version: 2.7
ok this is a 64 bit OS or better, with python version: 2.7
Help on module euclid:

NAME
    euclid

FILE
    /home/hon/2017/apr2017/cisco/euclid.py

DESCRIPTION
    Cisco challenge v4 unit and end-2-end tests
    First test is with a list of random points.
    Second test is with a list of points parsed fron the json file.
    
    The json sample point data file was extracted from the docx download via soffice
    i.e. Linux Libre Office, exported/saved-as to a text file and then this bash egrep:
    
    egrep '\{|\[|\]' CiscoChallengeCodingAssignmentv4.txt > coords.json

CLASSES
    __builtin__.dict(__builtin__.object)
        XYPoint
    
    class XYPoint(__builtin__.dict)
     |  Comparison class for Euclidian distance (from the origin) of 2 point objects ... 
     |  (cut-n-paste-n-edited from): http://portingguide.readthedocs.io/en/latest/comparisons.html
     |  The so-called dunderscore (double underscore) methods of the xy point class
     |  define comparison symantics by evaluating the point's absolute magnitue 
     |  distance from the origin of the Euclidian plane (flat space-time: the metric
     |  is unity everywhere!)
     |  
     |  Method resolution order:
     |      XYPoint
     |      __builtin__.dict
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __eq__(self, other)
     |  
     |  __ge__(self, other)
     |  
     |  __getattr__(self, name)
     |  
     |  __gt__(self, other)
     |  
     |  __init__(self, x=0, y=0, name='origin')
     |  
     |  __le__(self, other)
     |  
     |  __lt__(self, other)
     |  
     |  __ne__(self, other)
     |  
     |  __repr__(self)
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from __builtin__.dict:
     |  
     |  __cmp__(...)
     |      x.__cmp__(y) <==> cmp(x,y)
     |  
     |  __contains__(...)
     |      D.__contains__(k) -> True if D has a key k, else False
     |  
     |  __delitem__(...)
     |      x.__delitem__(y) <==> del x[y]
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __getitem__(...)
     |      x.__getitem__(y) <==> x[y]
     |  
     |  __iter__(...)
     |      x.__iter__() <==> iter(x)
     |  
     |  __len__(...)
     |      x.__len__() <==> len(x)
     |  
     |  __setitem__(...)
     |      x.__setitem__(i, y) <==> x[i]=y
     |  
     |  __sizeof__(...)
     |      D.__sizeof__() -> size of D in memory, in bytes
     |  
     |  clear(...)
     |      D.clear() -> None.  Remove all items from D.
     |  
     |  copy(...)
     |      D.copy() -> a shallow copy of D
     |  
     |  fromkeys(...)
     |      dict.fromkeys(S[,v]) -> New dict with keys from S and values equal to v.
     |      v defaults to None.
     |  
     |  get(...)
     |      D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
     |  
     |  has_key(...)
     |      D.has_key(k) -> True if D has a key k, else False
     |  
     |  items(...)
     |      D.items() -> list of D's (key, value) pairs, as 2-tuples
     |  
     |  iteritems(...)
     |      D.iteritems() -> an iterator over the (key, value) items of D
     |  
     |  iterkeys(...)
     |      D.iterkeys() -> an iterator over the keys of D
     |  
     |  itervalues(...)
     |      D.itervalues() -> an iterator over the values of D
     |  
     |  keys(...)
     |      D.keys() -> list of D's keys
     |  
     |  pop(...)
     |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
     |      If key is not found, d is returned if given, otherwise KeyError is raised
     |  
     |  popitem(...)
     |      D.popitem() -> (k, v), remove and return some (key, value) pair as a
     |      2-tuple; but raise KeyError if D is empty.
     |  
     |  setdefault(...)
     |      D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
     |  
     |  update(...)
     |      D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
     |      If E present and has a .keys() method, does:     for k in E: D[k] = E[k]
     |      If E present and lacks .keys() method, does:     for (k, v) in E: D[k] = v
     |      In either case, this is followed by: for k in F: D[k] = F[k]
     |  
     |  values(...)
     |      D.values() -> list of D's values
     |  
     |  viewitems(...)
     |      D.viewitems() -> a set-like object providing a view on D's items
     |  
     |  viewkeys(...)
     |      D.viewkeys() -> a set-like object providing a view on D's keys
     |  
     |  viewvalues(...)
     |      D.viewvalues() -> an object providing a view on D's values
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from __builtin__.dict:
     |  
     |  __hash__ = None
     |  
     |  __new__ = <built-in method __new__ of type object>
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T

FUNCTIONS
    chkSys()
        fun with exceptions -- check the runtime system for expected support
    
    jsonXYPoints(filename='coords.json', points=[])
        Read list of unsorted points from json text file and return list of XYPoint objs
        Assumes format: [{"id":"a","value":"31,49"}, ...]
    
    printPoints(u=[], s=[], o={'name': 'origin', 'x': 0, 'y': 0})
        Formatted print of 2 XYPoints lists
    
    randSample(list=[], names=['a', 'b', 'c', 'd', 'e', 'f', 'g'])
    
    sortByDistance(origin, unsorted_list=[], sorted_list=[])
        Rely on XYPoint comparison dunderscore method python magic for distance sort
    
    testOptns()
    
    transAll(origin={'x': 0, 'y': 0}, origpnts=[], trnspnts=[])
        Translate all points in list according to the indicated origin

DATA
    print_function = _Feature((2, 6, 0, 'alpha', 2), (3, 0, 0, 'alpha', 0)...

02may2017

