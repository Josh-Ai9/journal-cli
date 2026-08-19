import journal

class Menu:
  def __init__(self):
    self.journal = journal.Journal()
  def show_menu_request(self):
    while True:
      try:
        print(
          f'1. Add Entry\n'
          f'2. Edit Entry\n'
          f'3. delete Entry\n'
          f'4. view Entry\n'
          f'5. search Entry\n'
          f'6. tag Entry\n'
          f'7. favorite Entry\n'
          f'8. List All Entries\n'
          f'9. Clear All Datas\n'
        )
        main_menu = input(':…:').strip().lower()
        
        if main_menu == '1':
          self.journal.add_entry()
        elif main_menu == '2':
          self.journal.edit_entry()
        elif main_menu == '3':
          self.journal.delete_entry()
        elif main_menu == '4':
          self.journal.view_entry()
        elif main_menu == '5':
          self.journal.search_entry()
        elif main_menu == '6':
          self.journal.tag_entry()
        elif main_menu == '7':
          self.journal.favorite_entry()
        elif main_menu == '8':
          self.journal.list_all_entries()
        elif main_menu == '9':
          print('Press Enter or choose y to confirm')
          confirm = input('Confirm You Want To Delet All of your Datas -y').lower().strip()
          if not confirm or confirm == 'y':  self.journal.clear_all_data()
          else:  print('You stopped it from deleting all your datas!')
        elif main_menu == 'end':
          break
        elif not main_menu:
          print('Main menu shouldn\'t be Empty')
        else:
          print('Invalid Choice!')
      except Exception as e:
        print(e)



if __name__=='__main__':
  user1 = Menu()
  user1.show_menu_request()
  
  