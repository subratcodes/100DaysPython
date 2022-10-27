def runs():
  try:
    a=[1,2,3]
    print(a[3])
  except (IndexError,ValueError) as err:
    print(err)