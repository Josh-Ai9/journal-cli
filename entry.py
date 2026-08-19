import datetime

class Entry:
  def __init__(self,id,title,content,date=None):
    self.id = id
    self.title = title
    self.content = content
    self.date = date or datetime.datetime.now().strftime('%b %d_%m_%y - %H:%M:%S')


  def to_dict(self):
    return {
      'id':self.id,
      'title':self.title,
      'content':self.content,
      'date':self.date
    }


  def from_dict(cls,data):
    return cls(
      data['id'],
      data['title'],
      data['content'],
      data['date'],
    )