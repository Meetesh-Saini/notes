# What is this?
A simple SSRF challenge.

# What participants will get?
All of the files with flask code to analyze the code.  
- api.py  
- app.py  
- models.py  
- server.py  
- requirements.txt  

# How to modify flag or database
Use `create.py` to modify flag or modify database.  
- Modify flag
    - change FLAG variable in `create.py` and call `write_flag` function.
- Modify datbase
    - change rows in `product.csv` or `sale.csv`, and call `update_product` or call `update_sale` in `create.py`.
