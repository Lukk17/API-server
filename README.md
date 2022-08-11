1. Install Python3
https://www.python.org/downloads/release/python-3106/
   * check checkbox "Add Python X.XX to PATH"
   * customize installation and check all checkboxes  
  

2. If not installed previously install python PIP  
a) Windows command prompt:  
`curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`  
b) Linux:  
`sudo apt-get install python3-pip`


3. Install Flask framework in terminal (Windows or Linux):  
   a) Windows   
   `python -m pip install flask`   
   b) Linux  
   `python3 -m pip install flask`
   

5. In terminal (starting from main app folder):  
   `cd server`  
   `flask run`  
Should print in terminal:  
   ``` 
   * Debug mode: off
   WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
   * Running on http://127.0.0.1:5000
   Press CTRL+C to quit
   ```

6. You can check GET balance in the browser at address:  
   http://127.0.0.1:5000/balance
   
For POST (and GET too) request use Postman or curl.  
Collection for Postman are exported into "postman" folder - you can import it in app.