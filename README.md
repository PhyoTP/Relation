# Relation
a python module for making relationships between classes
## how to use
download relation.py to your project and import it:
```py
import relation as r
```
to define a new relator (a custom class), use `class insert_name_here(r.Relator):`  
to add a relation to a relator, multiply them  
to add a child to a relator, use `parent+child`  
to check if an object is a relator use `is_relator` or `type_is_relator` for type  
to access a relator's relationships as a list of strings, use `.[insert relationship]_names`  
see example.py for more usage
## roadmap
- [x] Python File
- [ ] Upload to PyPi to able to be pip installed
- [ ] more features
- [ ] Swift Package?

