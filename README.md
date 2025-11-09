# Customer_Profitability_Analysis_Project

📊 **Telecom Customer Profitability Dashboard** (Power BI + Python + MySQL).


---

````md

---

## 🧩 Project Overview
This project delivers a **Customer Profitability Analysis Dashboard** built in **Power BI**, designed for executive decision-making.  
It goes beyond simple revenue tracking to measure **Customer Lifetime Value (CLV)**, **Return on Investment (ROI)**, and **Segment Profitability**, helping telecom companies optimize marketing and retention strategies.

---

## 🧠 Key Insights Delivered
- 📈 **Customer Lifetime Value (CLV)** per customer  
- 💸 **Profit Margin** & **ROI** by customer segment  
- 🕒 **Monthly Revenue Trends**  
- 🌍 **Geographical Revenue Distribution**  
- 👥 **Customer Retention and Churn Analysis**

---

## ⚙️ System Workflow

```mermaid
flowchart TD
    A[📂 Data Collection] --> B[🧹 Data Cleaning (Python)]
    B --> C[(💾 MySQL Database)]
    C --> D[📊 Power BI Visualization]
    D --> E[🧠 Decision Making]
````

**Explanation:**

1. **Data Collection:** Raw telecom data imported from CSV and databases
2. **Data Cleaning:** Processed using Python (Pandas & NumPy)
3. **Database:** Cleaned data stored in MySQL
4. **Visualization:** Power BI connected via DirectQuery
5. **Decision Support:** Executives use insights to optimize profitability

---

## 🧮 KPI Formulas

| Metric                            | Formula                                                                               | Description                                                |
| --------------------------------- | ------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| **CLV (Customer Lifetime Value)** | `(Average Revenue per Customer × Gross Margin %) × Average Customer Lifespan (years)` | Predicts total revenue from a customer over their lifetime |
| **ROI (Return on Investment)**    | `(Total Profit ÷ Total Cost) × 100`                                                   | Measures investment efficiency                             |
| **Profit Margin**                 | `(Revenue - Cost) ÷ Revenue × 100`                                                    | Shows overall profitability                                |

> 💡 In Power BI, CLV was computed for **each customer** using DAX measures on aggregated data.

---

## 🗂️ Folder Structure

```
Telecom_Customer_Profitability/
│
├── dataset/
│   └── customer_profitability.csv
│
├── data_cleaning_script/
│   └── Cleaning.py
│
├── reports/
│   └── Telecom_Dashboard.pbix
│
├── testing/
│   └── test_data_quality.py
│
├── requirements.txt
└── README.md
```

---

## 🧰 Tech Stack

| Layer                   | Technology             | Description                                   |
| ----------------------- | ---------------------- | --------------------------------------------- |
| **Data Layer**          | MySQL                  | Stores cleaned and processed customer data    |
| **Processing Layer**    | Python (Pandas, NumPy) | Performs preprocessing and metric computation |
| **Visualization Layer** | Power BI               | Builds interactive dashboards and reports     |

---

## 📊 Dashboard Highlights

✨ **Interactive Power BI Features:**

* Dynamic slicers for **Customer Segment**, **Region**, and **Plan Type**
* Time-series visualizations with **Month & Year filters**
* KPI cards for **CLV**, **ROI**, and **Profit**
* Drill-downs for detailed profitability at the customer level
* Live database connection using **DirectQuery**

📷 *Example Preview (Dashboard Screenshot Placeholder)*

> *(Insert your Power BI dashboard screenshot here)*

---

## 🧠 Insights from the Dashboard

* 📊 Top 10 customers generate **68% of total profits**
* 🚀 ROI highest in **Premium Plan** category
* 💰 CLV indicates strong **retention value in urban regions**
* 🔄 Identified **loss-making customers** with negative ROI

---

## 🧱 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/telecom-profitability-dashboard.git
cd telecom-profitability-dashboard
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Data Cleaning Script

```bash
python data_cleaning_script/Cleaning.py
```

### 4️⃣ Connect Power BI to MySQL

1. Open `Telecom_Dashboard.pbix`
2. Set MySQL connection credentials
3. Refresh data → Dashboard auto-updates

---

## 📚 References

1. [Power BI Documentation](https://learn.microsoft.com/en-us/power-bi/)
2. [Pandas Library](https://pandas.pydata.org/)
3. [NumPy Library](https://numpy.org/doc/)
4. [MySQL Documentation](https://dev.mysql.com/doc/)
5. [Power BI DirectQuery](https://learn.microsoft.com/en-us/power-bi/connect-data/)

---

## 🧑‍💻 Author

**👤 Sahithi thalluri**
📧 [[sahithi382004@gmail.com]]
💼 Data Analyst | Power BI Developer | Python Enthusiast

---

## ⭐ Show Your Support

If you found this project useful, don’t forget to ⭐ **star this repository** and share it!

---

## 🏗️ Future Enhancements

* Integration with AI-based profitability forecasting
* Predictive churn modeling
* Automated alert system for revenue dips

---

### 🎉 Built with ❤️ using Power BI, Python, and MySQL

```

---

Would you like me to:
✅ add an **interactive table of contents**,  
✅ auto-generate commit badges (stars, forks, issues),  
and  
✅ include a **Power BI preview image layout**?


```
