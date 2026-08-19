import json,os

class Storage:
  
  path = 'A_Diary_data.json'

  @classmethod
  def load_data(cls):
    if os.path.exists(cls.path):
      with open(cls.path,'r') as f:

        try:
          return json.load(f)
        except json.JSONDecodeError:
          return []
    else:
      return []

  @classmethod
  def save(cls,file):
    with open(cls.path,'w') as f:
      json.dump(file,f,indent=4)