#!/usr/bin/env python
# coding: utf-8

# In[46]:


from flask import Flask, request, render_template
import joblib


# In[47]:


app = Flask(__name__)


# In[48]:


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST": 
        income = request.form.get("Income")
        print(income)
        model1 = joblib.load("FOOD_REG")
        pred1 = model1.predict([[income]])
        str1 = f"The prediction for your Food Expenditure based on your income using Regression is : {pred1[0][0]:.2f}"
        return(render_template("index.html", result1=str1))
    else:
        return(render_template("index.html", result1="Your result will be shown here"))


# In[ ]:


if __name__ == "__main__": 
    app.run()


# In[ ]:




