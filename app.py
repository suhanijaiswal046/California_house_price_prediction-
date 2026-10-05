import streamlit as st
import pandas as pd
import joblib

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="California House Price Predictor",
    page_icon="🏡",
    layout="wide"
)

# ==========================================
# LOAD MODEL
# ==========================================

obj = joblib.load("california_1.joblib")

model = obj["model"]
columns = list(obj["columns"])

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

.main{
    background:#f5f7fb;
}

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}

div[data-testid="stMetric"]{
    background:white;
    padding:20px;
    border-radius:15px;
    border:1px solid #e5e7eb;
    box-shadow:0 3px 12px rgba(0,0,0,.08);
    color: #000000 !important;
}

/* Ensure metric value and all text inside the metric are black*/
div[data-testid="stMetric"] * {
    color: #000000 !important;
}    

.stButton>button{

    width:100%;
    height:55px;

    border:none;

    border-radius:10px;

    background:#2563eb;

    color:white;

    font-size:18px;

    font-weight:600;

}

.stButton>button:hover{

    background:#1d4ed8;

}

</style>
""", unsafe_allow_html=True)

# ==========================================
# HEADER
# ==========================================

st.title("🏡 California House Price Predictor")

st.write("""
Estimate the market value of a California house using Machine Learning.

Fill in the details below and click **Predict House Price**.
""")

st.info("""
👋 **New to house price prediction?**

Don't worry! Hover over the **ⓘ icon** beside each field to see a simple explanation and example values.
If you're unsure, use the default values to explore how the model works.
""")

st.divider()



# ===================================================
# HELP SECTION
# ===================================================

with st.expander("ℹ️ Don't know what these values mean? Click here"):

    st.markdown("""
## 🏡 How to Fill the Form

Don't worry if these terms look technical.
Below is a simple explanation of every field.

---

### 💰 Neighborhood Median Income

This represents the average income of families living nearby.

**Typical Range**

- 🔴 1–3 → Lower-income area
- 🟡 4–6 → Average-income area
- 🟢 7–15 → High-income area

**Example**

`5.2`

---

### 🏠 House Age

Average age of houses.

Example:

- New House → 5 years
- Medium → 20 years
- Old → 45 years

---

### 🚪 Average Rooms

Average rooms in nearby houses.

Typical values

- 4
- 5
- 6
- 7
- 8

---

### 👨‍👩‍👧 Population

Total people living nearby.

Typical values

500 – 5000

---

### 🏡 Average Occupancy

Average people living in one house.

Typical values

2–5

---

### 📍 Longitude

Location of the property.

Example

-122.23

Don't worry if you don't know this.
You can use the sample value.
""")

    

# ==========================================
# INPUTS
# ==========================================

left, right = st.columns(2)

with left:

    medinc = st.number_input(
    "💰 Neighborhood Median Income",
    min_value=0.0,
    value=5.0,
    step=0.1,
    help="""
    Average income of families in the neighborhood.

    Typical Range:
    • 1–3 = Lower income
    • 4–6 = Average income
    • 7–15 = High income

    Example:
    5.2
    """
    )

    st.caption("💡 Example: 5.2")

    houseage = st.number_input(
    "🏠 House Age (Years)",
    min_value=1,
    max_value=60,
    value=20,
    help="""
    How old is the house?

    Typical values

    5 = New House

    20 = Medium

    45 = Old House
    """
    )

    st.caption("💡 Example: 20 Years")

    averooms = st.number_input(
    "🚪 Average Rooms",
    min_value=1.0,
    value=6.0,
    step=0.1,
    help="""
    Average number of rooms.

    Typical Range

    4 = Small House

    6 = Medium House

    8 = Large House
    """
    )

    st.caption("💡 Example: 6 Rooms")

with right:

    population = st.number_input(
    "👨‍👩‍👧 Neighborhood Population",
    min_value=1,
    value=1000,
    help="""
    Approximate population living nearby.

    Typical Range

    500–5000
    """
    )

    st.caption("💡 Example: 1200")

    aveoccup = st.number_input(
    "🏡 Average People Per House",
    min_value=1.0,
    value=3.0,
    step=0.1,
    help="""
    Average number of people living in one house.

    Typical Range

    2–5
    """
    )

    st.caption("💡 Example: 3")

    longitude = st.number_input(
    "📍 Longitude",
    value=-122.23,
    format="%.2f",
    help="""
    Location coordinate.

    Typical California values

    -114 to -124

    Example

    -122.23
    """
    )

    st.caption("💡 Example: -122.23")

st.divider()

# ==========================================
# BUTTONS
# ==========================================

col1, col2 = st.columns(2)

with col1:
    predict = st.button(
        "🏡 Predict House Price",
        use_container_width=True
    )

with col2:
    reset = st.button(
        "🔄 Reset",
        use_container_width=True
    )

if reset:

    # Remove all widget values
    for key in list(st.session_state.keys()):
        del st.session_state[key]

    st.rerun()

# ==========================================
# PREDICTION
# ==========================================

if predict:

    input_df = pd.DataFrame(
        [[
            medinc,
            houseage,
            averooms,
            population,
            aveoccup,
            longitude
        ]],
        columns=columns
    )

    with st.spinner("🤖 AI is predicting..."):

        prediction = model.predict(input_df)[0]

    st.success("Prediction completed successfully!")

    prediction = float(model.predict(input_df)[0])

    estimated_price = prediction * 100000


    st.subheader("🤖 AI Prediction Result")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            label="📊 Model Prediction",
            value=f"{prediction:.3f}"
        )

    with col2:
        st.metric(
            label="💰 Estimated House Price",
            value=f"${estimated_price:,.0f}"
        )

    if estimated_price < 150000:
        category = "🟢 Budget"

    elif estimated_price < 300000:
        category = "🔵 Affordable"

    elif estimated_price < 600000:
        category = "🟡 Premium"

    else:
        category = "🔴 Luxury"


    st.info("""
        ### 📘 What do these values mean?

        **📊 Model Prediction**
        - This is the raw output generated by the Machine Learning model.
        - In the California Housing dataset, the target value is measured in units of **$100,000**.

        **💰 Estimated House Price**
        - This is the converted house price shown in US dollars.
        - Formula used:

        **Estimated Price = Model Prediction × $100,000**
        """)
    
    st.divider()

    st.subheader("📋 Input Summary")

    st.dataframe(
        input_df,
        use_container_width=True
    )

    st.divider()

    st.subheader("🤖 AI Insight")

    if prediction >= 3:

        st.success("""
The model predicts this property has a relatively **high market value**.

Possible reasons:

- High median income

- Good house condition

- Attractive location

- Strong neighborhood characteristics
""")

    elif prediction >= 2:

        st.info("""
The predicted price is **moderate**.

The property's value is influenced by a balanced combination of income, house age, and location.
""")

    else:

        st.warning("""
The estimated price is comparatively **lower**.

This may be due to lower neighborhood income, smaller houses, or location characteristics.
""")

st.divider()

st.caption("❤️ Built with Streamlit • Scikit-learn • Machine Learning")