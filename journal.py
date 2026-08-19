from storage import Storage
from entry import Entry
import json

class Journal:

  def get_next_id(self):
    data = Storage.load_data()

    if not data:
      return 1
    else:
      return max(entry['id'] for entry in data) + 1


  def add_entry(self):
    data = Storage.load_data()
    print(f'{'='*15}Add Entry{'='*15}\nTitle')
    while True:
      title = input('::…::').strip()
      if not title:
        print('Title can not be Empty!')
      elif title == 'end':
        break
      else:
        lines = []
        while True:
          line = input('-_- ')
          if line == 'end':
            break
          else:
            lines.append(line)
        content = '\n'.join(lines)

        entry = Entry(self.get_next_id(),title,content)

        data.append(entry.to_dict())
    
        with open(Storage.path,'w') as f:
          json.dump(data,f,indent=4)
        print(f'Entry saved sucsesfully with id {self.get_next_id()-1}')

  
  def edit_entry(self):
    data = Storage.load_data()
    if not data:
      print('No entries available.')
      return
    else:
      while True:
        print()
        choice = input('=== Edit Entry ===\n1. Replace text\n2. Continue writing\n3. rewrite content/title\n4.Cancel\nEnter Your Choice:').strip().lower()
        if not choice:
          print('Choice couldn\'t be EMPTY!')
        elif choice == 'end':
          break
        elif choice == '1':
          while True:
            id = input('Enter Id: ').lower().strip()
            if not id:
              print('id can not be Empty!')
            elif id == 'end':
              break
            else:
              try:
                id = int(id)
              except ValueError:
                print('integer only')
                continue
              if not any(i['id'] == id for i in data):
                print('Entry not found.')
              else:
                while True:
                  old_word = input('Enter Old word you want to replace::: ')
                  if not old_word:
                    print('Word can not be Empty!')
                  elif old_word == 'end':
                    break
                  else:
                    for d in data:
                      if d['id'] == id:
                        splited = d['content'].split()
                        if old_word in splited:
                          old_word_index = splited.index(old_word)
                          new_word = input('Enter New Word:::')
                          splited[old_word_index] = new_word
                          d['content'] = '\n'.join(splited)
                          Storage.save(data)
                          print(f'Old Word "{old_word}" replaced by "{new_word}"')
                        else:
                          print('Old Word Not Found')
              
        elif choice == '2':
            while True:
              id = input('Id\'s of your content:').strip().lower()
              if not id:
                print('id can not be EMPTY')
              elif id == 'end':
                break
              else:
                try:
                  id = int(id)
                except ValueError:
                  print('integer Only')
                  continue
                if not any(i['id'] == id for i in data):
                  print(f'No item matching for {id}!')
                else:
                  for d in data:
                    if d['id'] == id:
                      continue_writting = input(f'{d['content']} ')
                      d['content'] = d['content'] + f' {continue_writting}'
                      Storage.save(data)

        elif choice == '3':
          while True:
            rewrite_menu = input('1. title\n2 content\n3.Cancel.__').strip().lower()
            if not rewrite_menu:
              print(f'Menu can not be Empty')
            elif rewrite_menu == 'end':
              break
            else:
              if rewrite_menu == '1':
                while True:
                  id = input('Id of your contents title!').lower().strip()
                  if not id:
                    print('Id can not be Empty')
                  elif id == 'end':
                    break
                  else:
                    try:
                      id = int(id)
                    except ValueError:
                      print('Integer Only')
                      continue
                    stopped = False
                    while not stopped:
                      if not any(i['id'] == id for i in data):
                        print(f'No id matching for {id}!')
                      else:
                        old_title = input('Old Title:  ')
                        
                        if not old_title:
                          print('Old Title Can Not Be Empty!')
                          
                        elif old_title == 'end':
                          stopped = True
                        
                        elif not any(t['title'] == old_title for t in data):
                          print(f'Not found a title with "{old_title[:8]}.."')
                          
                        else:
                          while True:
                            new_title = input('New Title:  ')
                            if not new_title:
                              print('New title can not be empty!')
                            elif new_title == 'end':
                              break
                            else:
                              for o in data:
                                if o['id']==id:
                                  if o['title'] == old_title:
                                    o['title'] = new_title
                                    Storage.save(data)
                              stopped = True
                              break


              elif rewrite_menu == '2':
                date = Storage.load_data()
                while True:
                  id = input('Id of your contents title!').lower().strip()
                  if not id:
                    print('Id can not be Empty')
                  elif id == 'end':
                    break
                  else:
                    try:
                      id = int(id)
                    except ValueError:
                      print('Intger Only')
                      continue
                    if not any(i['id'] == id for i in data):
                      print(f'No id matching for {id}!')
                    else:
                      new_content = input('New content:  ')
                      for o in data:
                        if o['id'] == id:
                          o['content'] = new_content
                          Storage.save(data)

              elif rewrite_menu == '3':
                break
              else:
                print('Invalid choice!')
                
        elif choice == '4':
          break
        else:
          print('Invalid choice')
  

  def delete_entry(self):
    data = Storage.load_data()
    if not data:
      print('No entries available!')
      return
    else:
      while True:
        id = input('Enter id to Be Deleted:').lower().strip()
        if not id:
          print('Id can\'t be Empty!')
        elif id == 'end':
          break 
        else:
          try:
            id = int(id)
          except ValueError:
            print('Intger Only')
            continue
          if not any(i['id'] == id for i in data):
            print(f'no matching id for {id}')
          else:
            for d in data:
                if d['id'] == id:
                  filtered = [c for c in data if not c['id'] == id]
                  data = filtered
                  Storage.save(data)
                  print(f'id {id} deleted sucsesfully!')
                  break


  def view_entry(self):
    data = Storage.load_data()
    if not data:
      print('No Entries Avaulable')
      return
    else:
      print('====== View entries======')
      print(f'Entries ==> {len(data)} ')
      while True:
        entry_id = input('Read entry id?').lower().strip()
        if not entry_id:
          print('Entry id can\'t be Empty')
        elif entry_id == 'end':
          break
        else:
          try:
            id = int(entry_id)
          except ValueError:
            print('Inger only')
            continue
          if not any(i['id'] == id for i in data):
            print('Item not Found!')
          else:
            for d in data:
              if d['id'] == id:
                print(
                  f'Title = {d["title"]}\n'
                  f"Content{'_'*40}\n{d['content']}\n"
                  f"Id = {d['id']}\n"
                  f"{'…'*40}\n"
                  f"                    {d['date']} "
                )
        
        
  def search_entry(self):
    data = Storage.load_data()
    if not data:
      print('No Entry Vailable!')
    else:
      while True:
        id = input('id🔗').lower().strip()
        if not id:
          print('Id can\'t be Empty')
        elif id == 'end':
          break
        else:
          try:
            id = int(id)
          except ValueError:
            print('integer Only')
            continue
          found = False
          for d in data:
            if d['id'] == id:
              found = True
              print(
                f'Title = {d["title"]}\n'
                f"Content{'_'*40}\n{d['content']}\n"
                f"Id = {d['id']}\n"
                f"{'…'*40}\n"
                f"                    {d['date']} "
              )
          if not found:
            print('Item Not Found')
  
  def tag_entry(self):
    data = Storage.load_data()
    if not data:
      print('No entry Available!')
    else:
      while True:
        id = input('id_@').lower().strip()
        if not id:
          print('Id can\'t be Empty')
        elif id == 'end':
          break
        else:
          try:
            id = int(id)
          except ValueError:
            print('Somthing Went Wrong')
            print('May you acidentally entered invalid integer')
            continue
          if not any(i['id'] == id for i in data):
            print(f'Entry not found matching to {id}')
          else:
            for d in data:
              if d['id'] == id:
                tag = input('Tag:  ').strip()
                if not tag:
                  print('Tag can not be empty!')
                elif tag == 'end':
                  break
                else:
                  d.setdefault('tag',[]).append(tag)
                  Storage.save(data)
                  break
                  

  def list_all_entries(self):
    data = Storage.load_data()
    if not data:
      print('No entry available!')
    else:
      for i,e in enumerate(data,1):
        print(f'___________({i})_________')
        print(
          f'Id = {e['id']}\n'
          f"Title = {e['title']}\n"
          f"Content:-\n{'_'*40}\n{e['content']}\n"
          f" {'…'*40}\n"
          f"{' '*28}{e['date']}\n"
        )
        if e.get('favorite'):
          print(f'{' '*30}Entry in favorite 🧡')
        else:
          print(f'{' '*18} You can put it in favorites! 💌')
        print()


  def favorite_entry(self):
    data = Storage.load_data()
    if not data:
      print('No entries available')
    else:
      while True:
        id = input("Enter id: ").lower().strip()
        if not id:
          print('Id can\'t be Empty')
        elif id == 'end':
          break
        else:
          try:
            id = int(id)
          except ValueError:
            print('Invalid input\nInger only')
            continue
          for entry in data:
            if entry["id"] == id:
              entry['favorite'] = not entry.get('favorite',False)
              Storage.save(data)

              if entry['favorite']:
                print('Added to favorite sucsesfully!')
              else:
                print('Removed from favorite!')
              break


  def clear_all_data(self):
    data = Storage.load_data()

    data.clear()

    Storage.save(data)


if __name__=='__main__':
  app = Journal()
  app.clear_all_data()
