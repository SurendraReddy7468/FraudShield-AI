<div align="center" style="border: 2px solid #ccc; padding: 20px; border-radius: 12px; width: 80%; margin: auto; box-shadow: 0 0 10px rgba(0,0,0,0.15);">
    <img
        width="180"
        height="220"
        alt="Logo - SURE ProEd"
        src="https://github.com/user-attachments/assets/88fa5098-24b1-4ece-87df-95eb920ea721"
        style="border-radius: 10px;"
    />

  <h1 align="center" style="font-family: Arial; font-weight: 600; margin-top: 15px;">SURE ProEd (formerly SURE Trust) 
      </h1>
<h2 style="color: #2b6cb0; font-family: Arial;">Skill Upgradation for Rural youth Empowerment Trust</h2>
</div>

<hr style="border: 0; border-top: 1px solid #ccc; width: 80%;" />

<div style="padding: 20px; border: 2px solid #ddd; border-radius: 12px; width: 90%; margin: auto; background: #fafafa; font-family: Arial;">

<h2 style = "color:#333;"> Student Details </h2>
<div align = "left" style ="margin: 20px; font-size: 16px;">
    <p><strong>Name:</strong> Surendra Reddy </p>
    <p><strong>Email ID:</strong> surendrareddyg40aiml@gmail.com </p>
    <p><strong>College Name:</strong> Central Institute of Technology Kokrajhar </p>
    <p><strong>Branch/Specialization :</strong> Computer Science &amp; Engineering </p>
    <p><strong>College ID:</strong> 202302023119 </p>
</div>

<hr style="border: 0; border-top: 1px solid #ccc; width: 80%;" />

<h2 style="color:#333;"> Course Details </h2>
<div align="left" style="margin: 20px; font-size: 16px;">
    <p><strong>Course Opted:</strong> G40 AI&amp;ML </p>
    <p><strong>Instructor Name:</strong> Prof. Radhakumari </p>
</div>
<div align="left" style="margin: 20px; font-size: 16px;">
    <p><strong>Duration:</strong> 6 months </p>
</div>

<hr style="border: 0; border-top: 1px solid #ccc; width: 80%;" />

<h2 style="color:#333;"> Trainer Details </h2>
<div align="left" style="margin: 20px; font-size: 16px;">

<p><strong>Trainer Name:</strong> Ms. Akshara A</p>
<p><strong>Trainer Email ID:</strong> Not available</p>
<p><strong>Trainer Designation:</strong> FSD &amp; AI/ML Trainer &amp; Volunteer @ Sure Trust | SDE-2 @ Propel Technology</p>
</div>

<hr style="border: 0; border-top: 1px solid #ccc; width: 80%;" />

## **Table of Contents**
- [Overall Learning](#overall-learning)
- [Projects Completed](#projects-completed)
- [Project Introduction](#project-introduction)
- [Technologies Used](#technologies-used)
- [Roles and Responsibilities](#roles-and-responsibilities)
- [Project Report](#project-report)
- [References](#references)
- [Learnings from LST & SST](#learnings-from-lst-and-sst)
- [Community Services](#community-services)
- [Certificate](#certificate)
- [Acknowledgments](#acknowledgments)

<hr style="border: 0; border-top: 1px solid #ccc; width: 80%;" />


## Overall Learning 

During my 6-month internship, I learned the fundamentals of Python programming, data analysis and machine learning, and applied them in a real-world capstone project.
I gained hands-on experience with Pandas, NumPy, Scikit-learn, XGBoost, SHAP and Streamlit. I learned how to handle highly imbalanced data, judge models with the right metrics instead of accuracy, explain individual predictions, and deliver a trained model as an interactive web application.
Beyond technical skills, the Life Skill and Soft Skill sessions improved my communication, confidence and professionalism, and I strengthened my habits of problem-solving, documentation and version control with Git and GitHub.


<h2 style="color:#333;" id="projects-completed"> Projects Completed </h2>
<div align="left" style="margin: 20px; font-size: 16px;">

<p><strong><a href="#project1">Project 1:</a></strong> FraudShield AI – Explainable credit card fraud detection and risk scoring</p>

</div>

<!-- Project 1 -->
<h3 id="project1">Project 1: FraudShield AI – Explainable credit card fraud detection and risk scoring</h3>
<p>
  FraudShield AI is a machine learning system that detects credit card fraud and explains every decision. Fraud is very rare (only 0.17% of 284,807 transactions in the dataset), so a model that always says "legit" is 99.83% accurate while catching no fraud. I therefore judged models by precision, recall and PR-AUC instead of accuracy. I compared Logistic Regression, Random Forest and XGBoost using SMOTE and class weights, and found that XGBoost with class weights worked best.
  On 56,962 unseen test transactions it caught 83 of 98 frauds with only 10 false alarms (precision 0.893, recall 0.847, F1-score 0.869, PR-AUC 0.885).
  The model's output becomes a 0–100 risk score with three bands (Low: approve, Medium: review, High: block), and SHAP shows the top five reasons behind each score. Everything runs in an interactive Streamlit dashboard on real transactions the model never trained on.
</p>
<p>
  <a href="https://github.com/sure-trust/REDDY-SURENDRA-g40-ai-ml/blob/main/Final%20capstone%20project/FraudShield_Project_Report.pdf" target="_blank"><strong>→ View Full Project Report</strong></a>
</p>
<p>
  <a href="https://github.com/SurendraReddy7468/FraudShield-AI" target="_blank"><strong>→ View Project Source Code on GitHub</strong></a>
</p>

### **Project Introduction**

Credit card fraud causes direct financial loss and weakens trust in digital payments, yet it is very hard to detect because fraud is only a tiny share of all transactions. FraudShield AI was built to catch as much fraud as possible without blocking genuine customers, and to explain why each transaction was flagged so that a human reviewer can trust the result.

### **Technologies Used**

- **Language:** Python
- **Data:** Pandas, NumPy
- **Modelling:** Scikit-learn, XGBoost, imbalanced-learn (SMOTE)
- **Explainability:** SHAP
- **Visualisation:** Matplotlib, Seaborn
- **Web app:** Streamlit
- **Tools:** Google Colab, VS Code, Git and GitHub
- **Dataset:** [Credit Card Fraud Detection (Kaggle, ULB Machine Learning Group)](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)

### **Roles and Responsibilities**

I completed this project individually, end to end:

- Explored the data and studied how fraud differs from legitimate transactions.
- Split and scaled the data without leakage, and compared SMOTE, class weights and no handling.
- Trained and evaluated Logistic Regression, Random Forest and XGBoost on precision, recall, F1-score and PR-AUC.
- Built the 0–100 risk score, the risk bands and the SHAP explanations.
- Developed the Streamlit dashboard and published the code on GitHub.
- Wrote the project report and presented the results to my mentor.

### **Project Report**

- [Full project report (PDF)](https://github.com/sure-trust/REDDY-SURENDRA-g40-ai-ml/blob/main/Final%20capstone%20project/FraudShield_Project_Report.pdf)
- [Project files in the SURE Trust repository](https://github.com/sure-trust/REDDY-SURENDRA-g40-ai-ml/tree/main/Final%20capstone%20project)
- [Source code on my personal GitHub](https://github.com/SurendraReddy7468/FraudShield-AI)

<hr style="height:1px; border-top:1px solid #ccc; width:80%;" />


## **References**

- [Credit Card Fraud Detection dataset – Kaggle](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- [XGBoost: A Scalable Tree Boosting System](https://arxiv.org/abs/1603.02754)
- [SMOTE: Synthetic Minority Over-sampling Technique](https://doi.org/10.1613/jair.953)
- [A Unified Approach to Interpreting Model Predictions (SHAP)](https://arxiv.org/abs/1705.07874)
- [Streamlit documentation](https://docs.streamlit.io)
---


## **Learnings from LST and SST**

**Life Skill Training (LST)** sessions were held every Sunday. Each week an experienced person shared lessons about life, building a career, learning new things, behaving well and overcoming fears and problems. We also joined meet calls with students from all the batches in one place, where we could clear our doubts and build good interaction with mentors and guest speakers. These sessions gave me direction, confidence and a better understanding of how to grow into a successful professional.

**Soft Skills Training (SST)** taught us how to talk and behave in a professional way. It improved my communication, my manner while speaking with others, and my overall professionalism, which helped me present my project clearly and confidently.
---

## **Community Services**

During my internship period, I took part in community-oriented activities and gave some help from my side to people and to the environment.

### **Activities Involved**
- **Tree Plantation Drive** – Participated by planting trees and contributing to environmental improvement.

- **Helping Elder Citizens** – Served and assisted elder citizens with simple daily tasks and provided support where needed.

### **Impact / Contribution**

- Actively participated in promoting a greener and cleaner surrounding.
- Offered personal assistance to elder citizens, strengthening community bonds.
- Improved skills in communication, coordination, and social responsibility.

<!--
### **Photos**
Add your own community service photos here, then remove the comment markers.

<div align="center">
<img src="YOUR-PHOTO-URL-1" alt="Community Service Photo 1" width="30%">
<img src="YOUR-PHOTO-URL-2" alt="Community Service Photo 2" width="30%">
</div>
-->

---

## **Certificate**

The internship certificate serves as an official acknowledgment of the successful completion of my training period. It will be issued by the organization upon fulfilling all required tasks and meeting the performance expectations of the program. The certificate validates the skills, experience, and contributions made during the internship.

<!--
Add your own certificate image after it is issued, then remove the comment markers.
<p align="center">
<img src="YOUR-CERTIFICATE-IMAGE-URL" alt="Internship Certificate" width="80%">
</p>
-->

---

## **Acknowledgments**

- [Prof. Radhakumari Challa](https://www.linkedin.com/in/prof-radhakumari-challa-a3850219b) , Executive Director and Founder - [SURE Trust](https://www.suretrustforruralyouth.com/)
- Ms. Akshara A , FSD & AI/ML Trainer & Volunteer @ Sure Trust | SDE-2 @ Propel Technology – for guiding me through the training and the capstone project.
- Central Institute of Technology Kokrajhar – for supporting my learning.

</div>

