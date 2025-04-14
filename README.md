# 💤 Sleep Disorder Classification with Machine Learning

An end-to-end data science project that predicts **sleep disorders** using lifestyle, biometric, and psychological metrics.  
This project explores how stress, sleep quality, activity, and other factors weave together into a **self-reinforcing loop** — a behavioral echo chamber that affects sleep health.

---

## 🌙 Why This Project?

After periods of lifestyle disruption — like **Ramadan** or **Eid holidays** — many people experience irregular sleep patterns, often without realizing the long-term health impact.

This project investigates the predictors of **Insomnia**, **Sleep Apnea**, and **Healthy Sleep**, helping lay the groundwork for **early detection and lifestyle-based intervention**.

---

## 🧠 The Sleep Disruption Loop: A Behavioral Echo Chamber

Upon deeper analysis, a striking behavioral pattern emerged:  
The very factors that *disrupt* sleep are often the ones it *worsens in return* — forming a loop that feeds itself.

📌 Elevated **stress** reduces sleep duration.  
📌 **Poor sleep** amplifies stress responses.  
📌 **Low physical activity** diminishes sleep quality.  
📌 **Fatigue** undermines motivation to stay active.

Over time, these dynamics form a **closed loop** that makes sleep disorders **harder to detect and treat**.

> By recognizing this feedback system early, we can design **preventive interventions** that target *lifestyle behaviors* before the cycle cements into clinical symptoms.

---

## 🧪 Dataset Overview

Each entry contains lifestyle, health, and activity metrics:

- Gender, Age, Occupation  
- Sleep Duration & Quality  
- Stress Level  
- Physical Activity & Daily Steps  
- Heart Rate & Blood Pressure  

**Target classes**:
- `Insomnia`
- `Sleep Apnea`
- `None` (Healthy)

---

## 🧰 Project Workflow

1. **Preprocessing**  
   - Handled missing values  
   - Encoded categorical features  
   - Scaled numerical data  
2. **Exploratory Data Analysis**  
   - Value counts, heatmaps, distributions  
3. **Statistical Testing**  
   - ANOVA (numerical) & Chi-Square (categorical)  
4. **Model Building**  
   - Compared multiple classifiers  
   - Tuned XGBoost with Grid Search  

---

## 📊 Model Comparison

| Model                    | Train Accuracy | Test Accuracy |
|-------------------------|----------------|---------------|
| Logistic Regression     | 89.00%         | 94.00%        |
| Random Forest           | 96.00%         | 95.00%        |
| Support Vector Classifier | 94.00%       | 95.00%        |
| **XGBoost (Tuned)**     | 91.64%         | **96.00%** ✅ |

---

## 🔍 Key Insights

- **High Stress = Higher Risk**  
  Sleep apnea patients showed consistently high stress scores.

- **Poor Sleep Duration**  
  Short sleep durations were linked to insomnia and apnea.

- **Sleep Quality Matters**  
  Clear inverse relation between sleep quality and disorder status.

- **Activity Creates a Protective Buffer**  
  Those with higher physical activity were mostly in the “no disorder” group.

- **BMI, Occupation, Gender**  
  Statistically significant predictors in classification.

> These aren’t just features. They are **flags** — behavioral signals we can act on.

---

## 📝 Final Thought

Sleep is not a luxury.  
It’s *infrastructure*.

When stress becomes chronic and sleep is ignored, the body revolts. This project highlights how everyday habits can accumulate into full-blown disorders.

If you’re still reading this past midnight:  
🪥 Close the laptop.  
🛏️ Fix your infrastructure.# Sleep-Health-and-Lifestyle
