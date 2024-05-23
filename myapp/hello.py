import fire

def hello(name="World"):
  return "#2 Test - Hello %s!" % name

if __name__ == '__main__':
  fire.Fire(hello)
