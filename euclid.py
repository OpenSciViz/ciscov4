#!/usr/bin/env python
'''
Cisco challenge v4 unit and end-2-end tests
First test is with a list of random points.
Second test is with a list of points parsed fron the json file.

The json sample point data file was extracted from the docx download via soffice
i.e. Linux Libre Office, exported/saved-as to a text file and then this bash egrep:

egrep '\{|\[|\]' CiscoChallengeCodingAssignmentv4.txt > coords.json
'''

from __future__ import print_function
import os, string, sys
if sys.version_info.major < 3: import six # allows python3 syntax in python2

def chkSys():
  '''fun with exceptions -- check the runtime system for expected support'''
  pyver = str(sys.version_info.major) + '.' + str(sys.version_info.minor)
  try:
    pyver = float(pyver) ; print('chkSys>', pyver) 
  except Exception as e:
    print(e) ; sys.stderr.write('float exception ... \n')
    sys.exit()
  else:
    if( pyver < 2.7 ):
      sys.stderr.write('sorry, only python 2.7 and beyond supported!\n')
      sys.exit()
    bits64 = sys.maxsize > 2**32 # ; print(bits64)
    if( not bits64 ):
      sys.stderr.write('sorry, only 64bit OS and beyond supported!\n')
      sys.exit()
  finally:
    sys.stdout.write('completed system check ... python version: ' + str(pyver) + '\n')

  sys.stdout.write('ok this is a 64 bit OS or better, with python version: ' + str(pyver) + '\n')
# end chkSys

# when used as a module, perform chkSys on import:
chkSys()

# proceed if ok ...
# for potential future use:
# import datetime, errno, logging, os, string, signal, socket
import getopt, json, random, time, zipfile

class XYPoint(dict):
  '''
  Comparison class for Euclidian distance (from the origin) of 2 point objects ... 
  (cut-n-paste-n-edited from): http://portingguide.readthedocs.io/en/latest/comparisons.html
  The so-called dunderscore (double underscore) methods of the xy point class
  define comparison symantics by evaluating the point's absolute magnitue 
  distance from the origin of the Euclidian plane (flat space-time: the metric
  is unity everywhere!) 
  '''
  def __getattr__(self, name):
    return self[name]

  def __init__(self, x=0, y=0, name='origin'):
    self.x = x
    self.y = y
    self.name = name

  def __eq__(self, other):
    return ((self.x, self.y) == (other.x, other.y))

  def __ne__(self, other):
    return ((self.x, self.y) != (other.x, other.y))

  def __lt__(self, other):
    smag = self.x*self.x + self.y*self.y
    omag = other.x*other.x + other.y*other.y
    return (smag < omag)

  def __le__(self, other):
    smag = self.x*self.x + self.y*self.y
    omag = other.x*other.x + other.y*other.y
    return (smag <= omag)

  def __gt__(self, other):
    smag = self.x*self.x + self.y*self.y
    omag = other.x*other.x + other.y*other.y
    return (smag > omag)

  def __ge__(self, other):
    smag = self.x*self.x + self.y*self.y
    omag = other.x*other.x + other.y*other.y
    return (smag >= omag)

  def __repr__(self):
    xy = "%s, %s" % (self.x, self.y)
    return self.name+': ('+xy+')'
# end XYPoint

def printPoints(u=[], s=[], o={'x':0, 'y':0, 'name':'origin'}):
  '''Formatted print of 2 XYPoints lists'''
  print(o, 'unsorted list:')
  for p in u:
    print(p)
  print('------------------------------------------------------------')

  print(o, 'sorted list:')
  for p in s:
    print(p)
  print('------------------------------------------------------------')
# end printPoints

def transAll(origin={'x': 0, 'y': 0}, origpnts=[], trnspnts=[]):
  '''Translate all points in list according to the indicated origin'''
  for p in origpnts:
    tp = XYPoint(p.x - origin.x, p.y - origin.y, 'tr:'+p.name)
    trnspnts.append(tp)
    print('transAll> ', p, tp) 
  return len(trnspnts)
# end transAll

def sortByDistance(origin, unsorted_list=[], sorted_list=[]):
  '''Rely on XYPoint comparison dunderscore method python magic for distance sort'''
  print('sortByDistance> list size: ', len(unsorted_list), origin)
  transAll(origin, unsorted_list, sorted_list)
  sorted_list.sort() 
  return len(sorted_list)   
# end sortByDistance

def randSample(list=[], names=['a', 'b', 'c', 'd', 'e', 'f', 'g']):
  for nam in names:
    rx = random.randrange(-10,10)
    ry = random.randrange(-10,10)
    p = XYPoint(rx, ry, nam)
    list.append(p)

  return len(list)
# end randSample

def jsonXYPoints(filename='coords.json', points=[]):
  '''
  Read list of unsorted points from json text file and return list of XYPoint objs
  Assumes format: [{"id":"a","value":"31,49"}, ...]
  '''
  xylist = {}
  try:
    with open(filename) as pointfile:    
      xylist = json.load(pointfile) # ; print('jsonXYPoints> ', xylist)
  except:
    print('jsonXYPoints> failed to load: ', filename)
    points = None
    return 0

  try:
    for p in xylist:
      # print(p) ; print(p['id'], p['value'])
      x, y = p['value'].split(',') # ; print(x, y)
      points.append(XYPoint(int(x), int(y), p['id']))
  except Exception as e:
    print(e) ; sys.stderr.write('sorry, failed to parse json coords ...\n')
    points = None
    return 0
  
  print('jsonXYPoints> ', points)
  return len(points)
# end jsonXYPoints

def testOptns():
  jsonfile = './coords.json'
  if(len(sys.argv) > 1): jsonfile = sys.argv[1] 
  if(len(jsonfile) <= 0):
    sys.stderr.write('sorry, no valid jsonfile found\n')
    sys.exit()

  return jsonfile
# end testOpt

if __name__ == '__main__':
  # random origin:
  ox = random.randrange(-10, 10)
  oy = random.randrange(-10, 10)
  o = XYPoint(ox, oy)

  rpnts = []
  rcnt = randSample(rpnts)
  rpnts.append(o)
  print('sort random sample with random origin as the last element in the unsorted list.')
  print('the origin point should become the first in the resulting sorted list ... ')
  sorted_pnts = []
  cnt = sortByDistance(o, rpnts, sorted_pnts)
  printPoints(rpnts, sorted_pnts, o)

  jsonfile = testOptns()
  jpnts = []
  jcnt = jsonXYPoints(jsonfile, jpnts)
  if( jcnt <= 0 ):
    sys.stderr.write('sorry, no valid json data\n')
    sys.exit()

  # another random origin:
  ox = random.randrange(-10, 10)
  oy = random.randrange(-10, 10)
  o = XYPoint(ox, oy)
  jpnts.append(o)
  sorted_pnts = []
  print('sort JSON sample with random origin as the last element in the unsorted list.')
  print('the origin point should become the first in the resulting sorted list ... ')
  cnt = sortByDistance(o, jpnts, sorted_pnts)
  printPoints(jpnts, sorted_pnts, o)

