def factorial(n):
  if(n==0):
    return 1
  return n*factorial(n-1)

def test_factorial():
  # for testing
  assert factorial(5) == 120
  assert factorial(4) == 24
  assert factorial(0) == 1
