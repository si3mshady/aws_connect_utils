import streamlit as st
import boto3

# Function to check if the phone number exists in DynamoDB
def check_phone_number(phone_number):
    dynamodb = boto3.client('dynamodb', region_name='us-east-1')
    table_name = 'phonedb'
    
    response = dynamodb.get_item(
        TableName=table_name,
        Key={
            'PhoneNumber': {'S': phone_number}
        }
    )
    
    if 'Item' in response:
        return True
    else:
        # If the phone number doesn't exist, add it to the DynamoDB table
        dynamodb.put_item(
            TableName=table_name,
            Item={
                'PhoneNumber': {'S': phone_number}
            }
        )
        return False

# Streamlit app layout
st.title("Phone Number Verification App")
user_input = st.text_input("Enter a Phone Number:")

if st.button("Verify"):
    if check_phone_number(user_input):
        st.image("https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGt4NzRrdXdkeHNlZmF2eGExMzhsNWVnaGpoaTluNGxoODFyeWhzaSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l1J9urAfGd3grKV6E/giphy.gif")
        st.write("Welcome back!")
    else:
        st.image("https://images.squarespace-cdn.com/content/v1/5a01bfa1bce17651a5f3334d/1517178866947-LB4K5PIHUK2T3FM774LU/CombinationLock.gif")
        st.write("The number was stored in the database.")

st.info("Note: Please enter a phone number to check.")
