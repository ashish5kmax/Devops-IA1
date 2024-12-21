def factorial(n):
  if(n==0) return 1
  fact = 1
  for i in range(1,n+1):
    fact*=i
  
  return fact

def test_factorial():
  assert factorial(5) == 120
  assert factorial(4) == 24
