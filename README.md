# Relation
a python module for making relationships between classes
## how to use
download relation.py to your project and import it:
```py
from relation import Relator
```
- to define a new relator (a custom class), use `class insert_name_here(Relator):`  
- to add a relation to a relator, multiply them
- to add a child to a relator, use `parent+child`
  - New: you can do `parent+[child1,child2,child3...]` now
- to access a relator's relationships as a list of strings, use `.[insert relationship]_names`  
see examples for more usage
## roadmap
- [x] Python File
- [ ] More examples and features
- [ ] Upload to PyPi to able to be pip installed
- [ ] Swift Package?

