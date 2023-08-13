import pandas as pd
import plotly.express as px
import streamlit as st

dogs_df = pd.read_csv('dog_intelligence.csv', encoding='ISO-8859-1')

dogs_df = dogs_df.dropna()
dogs_df.columns = dogs_df.columns.str.lower()
dogs_df.info()

st.title('Pup Smarts')
st.header("Dog Intelligence Comparison Based on Size")

# Create a dictionary mapping breed to intelligence score range
breed_intelligence_scores = {}

for _, row in dogs_df.iterrows():
    breed = row['breed']
    min_score = row['reps_lower']
    max_score = row['reps_upper']
    breed_intelligence_scores[breed] = (min_score, max_score)

def predict_intelligence(breed):
    # Check if the breed is in the dictionary
    if breed in breed_intelligence_scores:
        min_score, max_score = breed_intelligence_scores[breed]
        # Calculate the average intelligence score
        predicted_intelligence = (min_score + max_score) / 2
        return predicted_intelligence
    else:
        # If breed is not found in the dictionary, return a message indicating that
        return f"Intelligence score prediction not available for {breed}"

def main():
    st.title('Dog Intelligence Predictor')
    
    # Dropdown list to select breed
    breed_options = sorted(dogs_df['breed'].unique())
    selected_breed = st.selectbox('Select the breed of the dog:', breed_options)
    
    if st.button('Predict Intelligence'):
        # Call the predict_intelligence function and get the predicted intelligence
        predicted_intelligence = predict_intelligence(selected_breed)
        
        # Display the predicted intelligence
        if isinstance(predicted_intelligence, float):
            st.write(f'Predicted Intelligence Score: {predicted_intelligence:.2f}')
        else:
            st.write(predicted_intelligence)



def size_category(row):
    if row['height_low_inches'] <= 12 and row['weight_low_lbs'] <= 10:
        return 'Small'
    elif row['height_low_inches'] <= 18 and row['weight_low_lbs'] <= 25:
        return 'Medium'
    else:
        return 'Large'

# Apply the size_category function to create a new column
dogs_df['Size Category'] = dogs_df.apply(size_category, axis=1)

# Melt the dataframe to include reps_lower and reps_upper as a single column
melted_df = pd.melt(dogs_df, id_vars=["Size Category"], value_vars=["reps_lower", "reps_upper"],
                    var_name="Repetitions", value_name="Value")

# Create a histogram of reps_lower and reps_upper with size category on the x-axis
histogram = px.histogram(melted_df, x="Value", color="Repetitions", facet_col="Size Category",
                         facet_col_spacing=0.02,  # Adjust this spacing as needed
                         title="Distribution of Repetitions for Understanding Commands by Size Category",
                         labels={"Value": "Repetitions", "Repetitions": "Type of Repetitions"},
                         category_orders={"Repetitions": ["reps_lower", "reps_upper"]})

# Display the histogram using Streamlit
st.plotly_chart(histogram)


# Create a scatterplot of height vs. weight with number of repetitions as color
scatterplot = px.scatter(dogs_df, x="height_low_inches", y="weight_low_lbs", color="reps_lower",
                         title="Scatterplot of Low Height vs. Weight with Number of Repetitions",
                         labels={"height_low_inches": "Height (inches)", "weight_low_lbs": "Weight (lbs)"},
                         color_continuous_scale="Viridis",
                         hover_name="breed")

# Display the scatterplot using Streamlit
st.plotly_chart(scatterplot)

# Add a checkbox to show/hide the scatter plot
show_scatterplot = st.checkbox("Show Scatter Plot", value=True)
if not show_scatterplot:
    st.plotly_chart(scatterplot, use_container_width=True)

if __name__ == "__main__":
    main()
