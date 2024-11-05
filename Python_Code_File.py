import streamlit as st
import pickle
import numpy as np

# Selling Price Prediction
def predict_selling_price(customer,country,status,item_type,application,width,product_ref,quantity_tons_log,
                          thickness_log):    
    with open("model1.pkl","rb") as ft:
        ml = pickle.load(ft)
    user_data= np.array([[customer,country,status,item_type,application,width,product_ref,quantity_tons_log,
                          thickness_log]])
    y_pred = ml.predict(user_data)

    return np.exp(y_pred[0])

# Status Prediction
def predict_status(customer,country,selling_price_log,item_type,application,width,product_ref,
                   quantity_tons_log, thickness_log):    
    with open("model2.pkl","rb") as ft:
        ml = pickle.load(ft)
    user_data= np.array([[customer,country,selling_price_log,item_type,application,width,product_ref,
                          quantity_tons_log, thickness_log]])
    y_pred = ml.predict(user_data)

    return y_pred

# Straemlit Part
st.set_page_config(layout= "wide")

st.title(":orange[**INDUSTRIAL COPPER MODELING**]")
st.write("This application allows you to predict either the **Selling Price** for a product (using a regression model) "
         "or the **Status** (WON or LOST) of a transaction (using a classification model).")
page = st.selectbox(":violet[**Select the Operation**]", 
                            ["Predict the Selling Price 💰", "Predict the Status 🔍"])

if page == "Predict the Selling Price 💰":
    status_options = {'Won': 1, 'Lost': 0, 'Draft': 2, 'To be approved': 3, 'Not lost for AM': 4,
                     'Wonderful': 5, 'Revised': 6, 'Offered': 7, 'Offerable': 8}
    product_ref_options = [1670798778, 1668701718, 628377, 640665, 611993, 1668701376, 164141591, 1671863738, 
                            1332077137, 640405, 1693867550, 1665572374, 1282007633, 1668701698, 628117, 
                            1690738206, 628112, 640400, 1671876026, 164336407, 164337175, 1668701725, 
                            1665572032, 611728, 1721130331, 1693867563, 611733, 1690738219, 1722207579,  
                            929423819, 1665584320, 1665584662, 1665584642]
    country_options = [28, 25, 30, 32, 38, 78, 27, 77, 113, 79, 26, 39, 40, 84, 80, 107, 89]
    application_options = [10, 41, 28, 59, 15,  4, 38, 56, 42, 26, 27, 19, 20, 66, 29, 22, 40, 25, 67, 79, 3,
                            87.5, 2, 5, 39, 69, 70, 65, 58, 68]
    item_type_options = {'W': 1, 'WI': 0, 'S': 2, 'Others': 3, 'PL': 4, 'IPL': 5, 'SLAWR': 6}

    col1,col2,col3= st.columns(3)
    with col1:    
        customer = st.number_input(label=":blue[**Enter the Value for Customer**]", min_value=12458.0, 
                                   max_value=30408185.0, value=12458.0, step=1.0, format="%.1f", 
                                   key='One')
        item_type_selection =  st.selectbox(":blue[**Select the Item Type**]",
                                            sorted(item_type_options.keys()),key='Two') 
        item_type = item_type_options[item_type_selection]

        product_ref= st.selectbox(":blue[**Select the Product Ref**]",sorted(product_ref_options),
                                  key='Three') 
        
    with col2:
        country= st.selectbox(":blue[**Select the Country**]",sorted(country_options), key='Four') 
        application= st.selectbox(":blue[**Select the Application**]",sorted(application_options),
                                  key='Five') 
        quantity_tons_log = st.number_input(label=":blue[**Enter the Value for Quantity Tons (Log Value)**]",
                                            min_value=-0.322, max_value=6.924, value=0.000, step=0.01,
                                            format="%.3f", key='Six')

    with col3:       
        status_selection = st.selectbox(":blue[**Select the Status**]",sorted(status_options.keys()),
                                  key='Seven') 
        status = status_options[status_selection]
        width = st.number_input(label="**:blue[Enter the Value for Width]**", min_value=700.0, 
                                max_value=1980.0, value=700.0, step=0.1, format="%.1f", key='Eight')
        thickness_log = np.log(st.number_input(label=":blue[**Enter the Value for Thickness**]", 
                                               min_value=0.18, max_value=2500.0, value=0.18, step=0.01, 
                                               format="%.2f", key='Nine'))

    button= st.button(":red[***PREDICT THE SELLING PRICE***]",use_container_width=True)
    if button:
        price= predict_selling_price(customer,country,status,item_type,application,width,product_ref,
                                     quantity_tons_log,thickness_log)               
        st.write("## :green[**The Selling Price is :**]",price)

elif page == "Predict the Status 🔍":
    product_ref_options = [1670798778, 1668701718, 628377, 640665, 611993, 1668701376, 164141591, 
                           1671863738, 1332077137, 640405, 1693867550, 1665572374, 1282007633, 1668701698, 
                           628117, 1690738206, 628112, 640400, 1671876026, 164336407, 1665572032,164337175,     
                           611728, 1721130331, 1693867563, 611733, 1690738219, 1722207579, 929423819, 
                           1668701725, 1665584320, 1665584642]
    country_options = [28, 25, 30, 32, 38, 78, 27, 77, 113, 79, 26, 39, 40, 84, 80, 107, 89]
    application_options = [10, 41, 28, 59, 15,  4, 38, 56, 42, 26, 27, 19, 20, 66, 29, 22, 40, 25, 67, 79, 3,
                            87.5, 2, 5, 39, 69, 70, 65, 58, 68]
    item_type_options = {'W': 1, 'WI': 0, 'S': 2, 'Others': 3, 'PL': 4, 'IPL': 5, 'SLAWR': 6}

    col1,col2,col3= st.columns(3)
    with col1:    
        customer = st.number_input(label=":blue[**Enter the Value for Customer**]", min_value=12458.0, 
                                   max_value=30408185.0, value=12458.0, step=1.0, format="%.1f", 
                                   key='One')
        item_type_selection =  st.selectbox(":blue[**Select the Item Type**]",
                                            sorted(item_type_options.keys()),key='Two') 
        item_type = item_type_options[item_type_selection]
        product_ref= st.selectbox(":blue[**Select the Product Ref**]",sorted(product_ref_options),
                                  key='Three')  
            
    with col2:
        country= st.selectbox(":blue[**Select the Country**]",sorted(country_options),
                                  key='Four') 
        application= st.selectbox(":blue[**Select the Application**]",sorted(application_options),
                                  key='Five') 
        quantity_tons_log = st.number_input(label=":blue[**Enter the Value for Quantity Tons (Log Value)**]",
                                            min_value=-0.322, max_value=6.924, value=0.000, step=0.01,
                                            format="%.3f", key='Six')

    with col3:       
        selling_price_log = st.number_input(label=":blue[**Enter the Value for Selling Price (Log Value)**]",
                                            min_value=5.975, max_value=7.390, value=5.975, step=0.01,
                                            format="%.3f", key='Seven')
        width = st.number_input(label=":blue[**Enter the Value for Width**]", min_value=700.0, 
                                max_value=1980.0, value=700.0, step=0.1, format="%.1f", key='Eight')
        thickness_log = np.log(st.number_input(label=":blue[**Enter the Value for Thickness**]", 
                                               min_value=0.18, max_value=2500.0, value=0.18, step=0.01, 
                                               format="%.2f", key='Nine'))

    button= st.button(":red[***PREDICT THE STATUS***]",use_container_width=True)
    if button:
        status = predict_status(customer,country,selling_price_log,item_type,application,width,product_ref,
                                     quantity_tons_log,thickness_log)               
        if status == 1:
            st.write("## :green[**The Status is WON**]")
        else:
            st.write("## :red[**The Status is LOST**]")
    