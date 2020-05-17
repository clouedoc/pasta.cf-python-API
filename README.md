# Pasta.cf python API

It's a simple API for [pasta.cf](https://pasta.cf) written in python.
It can:
  - create pasta of all types ( except url shortener )
  - remove pasta
  - edit and existing pasta
  - read a pasta
  
Built with Cmd+Alt+I on Chromium, on pasta.cf. ( Devel. console )

Brought to you by <censored due to google finding this account>, because I'm a top level narcissic.

# Installation

___You need to have ```requests``` installed on your system, for your specific version of python.___


<censored due to google finding this file; basically, git clone and pip install>

Now move pastacfapi.py to the root file of your project ( or somewhere in your $PYTHONPATH )

# Usage

### To import: ( pastacfapi.py need to be in the same folder of the root file.)

```py
import pastacfapi
```

### To create a new paste:

```py
pastacfapi.create(paste_title, paste_text, paste_type)
```

# Exemples:

```py
import pastacfapi

paste = pastacfapi.create("PASTA-CF-API", "Wow, this API is really great, thanks to <censored due to google>, <3", pastacfapi.SELF_BURNING)

print("Paste url is: " + paste.url)
```

# Documentations

## Functions:

- create(title, text, type)

Return a [pasta_object](#pasta_object)

- remove(pasta-token, password)

Remove a pasta. Return nothing

- edit(pasta-token, password, title, text)

Edit an already created pasta. Only work with editable pasta. Return nothing

- read(pasta-token)

Return a string containing the text of the pasta specified.

## Constants:

### Paste type:

- ```SELF_BURNING```
- ```EDITABLE```
- ```STANDARD```

Side note: URL_SHORTENER is not supported yet.

## Classes

### pasta_object

- pasta['token']

The token of your pasta e.g: ```papa-sampling-random```

- pasta['view']

It's the standard user GUI url to see the pasta you just created.

- pasta['raw']

It's the raw GUI of your pasta, without fireworks.

- pasta['password']

It's the password of the paste you just created, if it's type is ```EDITABLE```

- pasta['type']

It's the type of the paste you just created (again!), if you forgot what is was.


# TODO:
##### Any ortographic help is welcome. I'm french. I speak english like an albinos unicorn.
##### Implement error handling. Please, someone, do that for me, because I don't know how to do it, really :(
##### Add commentaries (?) to the source code, because I'm bit lazy tonight.
##### Format this ugly README.md, I would accept every commit about that

# Contributors:

- <censored due to google finding this file>
- You ?

# LICENSE

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Licence Creative Commons" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br /><a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"></a>
For further informations see ```LICENSE``` file
