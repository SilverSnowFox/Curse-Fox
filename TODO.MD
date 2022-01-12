List of things to remake of the bot

- [ ] Help Command
- [ ] Main file
- [ ] List curses
- [ ] Create curses
- [ ] Server settings
- [ ] Curse someone 
- [ ] Cure someone
- [ ] Bot info
- [ ] Multiple language support
- [ ] Update the README.md

## Notes
- Use objects instead of SQL for curses
- Save server settings in SQL
- Save default settings and curses in json
- Check for ways to store objects
- Save languages in json
- Add modules to requirements.txt

## Commands
### Help

- Create an embed
- Retrieve server language
- Display help information main, list for the individual

### Info
Display the server stuff

- Retrieve language
- Display server name
- Display server icon
- Display server member count
- Display curse count
- Display server settings
- Display available languages available for the bot

### List Curses

- Retrieve server language
- Retrieve list of server curses
- Display curses

### Create Curse

- Check perms
- Get the argument
- Character check to make sure no problem
- Character limit to make sure no problem
- Check that curse doesn't already exist
- Add curse
- Save object

### Delete Curse

- Check that curse exists
- Check perms
- Delete curse
- Go through each user and remove if cursed with it
- Save object

### Curse someone

- Check perms
- Display list of curses, dropdown list
- Add curse to user
- Save object

### Cure someone

- Check that target is cursed
- Check that user has perms
- Remove user from cursed
- Save object

### Server settings

- Retreive server language 
- Display server settings
- Use buttons to turn off if on, same vice versa if user has permission
- Update settings
- Save in SQL

### Owner commands

- Cure everyone
- Reset curses (removes all then re-add default curses)
- Reset settings 

### List Curses

- Retrieve server language
- Display list of server curses
- Save object

### Bot info

- Retrieve server language
- Display bot information
  - Ping
  - Language
  - Developer
  - Python version

### on_message

- Check if user is cursed in server
- Retrieve curse, if is
- Create webhook
- Delete message
- Send message
- Send attachments
- Delete webhook