Situation:

- The sales team faced inefficiencies in lead qualification, often spending excessive time on unqualified leads. 
- There was a need for a more precise targeting mechanism that aligned partner capabilities with customer needs to improve sales outcomes.

Task:
- The objective was to develop a data-driven solution that would enhance lead qualification accuracy by combining customer purchase trends and partner success metrics.
- This would help reduce time spent on unqualified leads and optimize partner alignment for higher sales success.

Action:
A predictive model was designed to assess both partner propensity to sell and customer propensity to buy:
- Random Forests were employed to analyze historical customer purchase patterns and partner success metrics, predicting likelihoods of successful matches.
-	Segmentation analysis was applied to categorize partners and customers into actionable groups based on potential fit.
-	Ensemble techniques were used to integrate insights from multiple data sources, improving overall targeting precision.

Result:
- The solution improved lead qualification accuracy, leading to a 25% reduction in time spent on unqualified leads.
- By aligning partner capabilities with customer needs more effectively, the model significantly enhanced targeting precision, driving productivity and better sales outcomes.
- This project demonstrated the value of integrating machine learning and segmentation for business optimization.


---

## Tech Stack
- Language: `Python`
- Libraries: `pandas`, `scikit-learn`, `numpy`, `seaborn`, `datetime`, `matplotlib`, `missingno`

---

## Approach
1. Import the required libraries and packages.
2. Read the CSV file.
3. Perform data preprocessing.
4. Conduct exploratory data analysis.
   - Univariate analysis
   - Multivariate analysis
1. Perform RFM Analysis.
2. Perform feature engineering.
3. Create modeling data.
4. Build the predictive model.
5. Make predictions.

---

## Code Structure
- `input`: Contains data and configuration files.
   - `config.yaml`: Configuration parameters.
   - `final_customer_data.xlsx`: Customer transaction data.
   - `final_customer_data_with_RFM_features.csv`: Merged dataset with RFM values.
   - `ecom_product_data.csv`: Transaction data for RFM modeling.
- `src`: Contains modularized code for different project steps.
   - `engine.py`: Main execution script.
   - `ml_pipeline`: Modular functions.
   - `requirements.txt`: List of required packages.
- `output`: Stores the trained model for future use.
- `lib`: Reference notebooks from the project.

---


