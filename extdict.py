#!/usr/bin/env python

class AttributeDict(dict):
  def __getattr__(self, name):
    return self[name]

if __name__ == '__main__':
  q = AttributeDict({ 'Field1' : 3000, 'Field2' : 6000, 'RandomField' : 5000 })
  print q.Field1              
  print q.Field2              
  print q.RandomField
