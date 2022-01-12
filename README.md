# Curse Fox (Old)
A Discord bot that adds a little something to those misbehaving or interested users by adding 'curses' to their messages!

For example, if the user is cursed with 'woof', their messages will be replaced with 'message woof'

## Commands

### Help
```!!Help```

Send the user a DM with a list of commands and server information such as if everyone can curse or cure.

### Curing Users
#### ```!!Cure <user>```

Cures the mentioned user from the curse. This command is enabled for everyone by default to all users. It can be changed to only admins by using `!!EveryoneCure false`. It will still be enabled for users with administrator perms.
Ex: `!!Cure @User`

#### ```!!MassCure```

Similar to `!!Curse <user>` but cures the whole guild. This is an admin only command.


### Cursing Users
```!!Curse <user> <curse>```

Curses a mentioned user with an existing curse in the server.
Ex: `!!Curse @User nya`

### List Information
```!!Curses```

Displays a list of the guild's curses in the user's DM.

### Creating and Deleting curses
```!!Create <curse>```

Creates and adds a curse to the server that everyone can use. Limited to 20 characters at most.
Ex: `!!Create nya`

```!!Delete <curse>```

Deletes a curse from the server.
Ex: `!!Delete nya`

These two commands are administrator only commands.

## Default settings
```!!EveryoneCure <true/false>```

Toggles everyone's permission to cure others. If set to false, only people without curse and administrators can cure others.

```!!EveryoneCurse```

Toggles everyone's permission to curse others. If set to false, only administrators can curse others.

By default, EveryoneCure and EveryoneCurse are set to `true`