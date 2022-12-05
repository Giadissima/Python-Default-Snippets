class EnvMissing(Exception):
  def __init__(self, var):
    self.message = f'{var} missing in environment'
    super().__init__(self.message)