### Important Notes: 
In the descriptions below of the metrics, there are references to ‘positive’ and ‘negative’ labels. These are general terms to describe a binary classification outcome that we want to examine in relation to ‘sex’ in this case. An example of such a binary classification would be if we were looking at a dataset to train a cancer detection diagnostic model. The model either outputs ‘yes’ if cancer is detected, or ‘no’ if it is not, and these would be the ‘positive’ and ‘negative’ labels respectively. These metrics help us to understand the breakdown of our dataset in terms of the ‘sex’ variable and the ‘has cancer’ variable.

In addition, we are not always striving for the values that signify exact equality between male and female counts and percentages. For example, consider an AI tool used to diagnose autoimmune diseases. 80% of autoimmune diseases are suffered by females, therefore even if our dataset was 50% male samples and 50% female samples, we would and should expect that the value for Positive Label Imbalance is closer to -1 than 0, meaning that a higher percentage of the female samples are ‘positive’ compared to male samples. This examples highlights the fact that the ‘optimal’ or ‘unbiased’ values for these metrics that we are striving for can be highly contextual, depending on the problem that the AI tools is addressing.

These metrics were taken from: https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-detect-data-bias.html

# Training Dataset Challenge

## Submission Requirements
Below are the requirements that your submitted dataset must follow in order to work properly with the benchmarking workflow:

1. A column with the label ‘ID’ that is of the type ‘string’
2. A colum with the label ‘Sexo’ that is of the type ‘string’
3. All values in the ‘Sexo’ column must be either the string ‘male’ or ‘female’
4. A colum with the label ‘AF’ that is of type ‘string’
5. All values in the ‘AF’ column must be either the string ‘Yes’ or ‘No’
6. The file must be a .csv

## Metrics

### Class Imbalance

**Definition:** What proportion of the data set is one class vs the other 

**Equation:** (male_count - female_count) / (male_count + female_count)

**How to interpret:** If the value is 0.5, the dataset is perfectly balanced, having the same number of male samples as female samples. As the value trends toward 1, the data set has more male samples, and toward 0, the data set has more female samples.

### Female Positive Label Percentage

**Definition:** What percentage of all 'positive' labels are from females 

**Equation:** f_positive / overall_positive

**How to interpret:** If the value is 0.5, this means that of all the samples with a ‘positive’ label, there are the same number of male samples as there are female. As the value trends toward 1, more female samples have a ‘positive’ label than male, and toward 0, more male samples have a ‘positive’ label than female.

### Female Negative Label Percentage

**Definition:** What percentage of all 'negative' labels are from males

**Equation:** f_negative / overall_negative

**How to interpret:** If the value is 0.5, this means that of all the samples with a ‘negative’ label, there are the same number of male samples as there are female. As the value trends toward 1, more female samples have a ‘negative’ label than male, and toward 0, more male samples have a ‘negative’ label than female.

### Positive Label Imbalance

**Definition:** What percentage of 'positive' labels are male/female

**Equation:** (m_positive / male_count) - (f_positive / female_count)

**How to interpret:** If the value is 0, this means that the same percentage of female samples are ‘positive’ as male samples are ‘positive’. As the value trends toward 1, this means that the percentage of male samples that are ‘positive’ is greater than the percentage of female samples that are ‘positive’, and vice versea as the value trends toward -1.

### Negative Label Imbalance

**Definition:** What percentage of 'negative' labels are male/female

**Equation:** (m_negative / male_count) - (f_negative / female_count)

**How to interpret:** If the value is 0, this means that the same percentage of female samples are ‘negative’ as male samples are ‘negative’. As the value trends toward 1, this means that the percentage of male samples that are ‘negative’ is greater than the percentage of female samples that are ‘negative’, and vice versea as the value trends toward -1.

### Female Conditional Demographic Disparity

**Definition:** Determines whether females have a larger proportion of negative predictions in the data set than of the positive predictions

**Equation:** (f_negative / (m_negative + f_negative)) - (f_positive / (m_positive + f_positive))

**How to interpret:** A value of 0 indicates females represent equal proportions of ‘negative’ and ‘positive’ outcomes. As the value trends toward 1, this means that females have a greater proportion of ‘negative’ outcomes than ‘positive’ outcomes in the dataset. As the value trends toward -1, this means that females have a greater proportion of ‘positive’ outcomes than ‘negative’ outcomes in the dataset. 
 
### Male Conditional Demographic Disparity

**Definition:** Determines whether males have a larger proportion of negative predictions in the data set than of the positive predictions 

**Equation:** (m_negative / (m_negative + f_negative)) - (m_positive / (m_positive + f_positive))

**How to interpret:** A value of 0 indicates males represent equal proportions of ‘negative’ and ‘positive’ outcomes. As the value trends toward 1, this means that males have a greater proportion of ‘negative’ outcomes than ‘positive’ outcomes in the dataset. As the value trends toward -1, this means that males have a greater proportion of ‘positive’ outcomes than ‘negative’ outcomes in the dataset. 

# Model Output Challenge

## Submission Requirements

Below are the requirements that your submitted dataset must follow in order to work properly with the benchmarking workflow:

1. A column with the label ‘ID’ that is of the type ‘string’
2. A colum with the label ‘output’ that is of the type ‘string’
3. All values in the ‘output’ column must be either the string ‘Yes’ or ‘No’
4. The file must be a .csv

## Metrics

#### For definition purposes:
TP - True positives, model predicted positive and true value is positive (count)
TN - True negatives, model predicted negative and true value is negative (count)
FP - False positives, model predicted positive but true value is negative (count)
FN - False negatives, model predicted negative but true value is positive (count)

Overall accuracy - Equal accuracy (correct predictions) for each subgroup (TP + TN) / (total count)
Statistical Parity - Fractions of assigned positive labels are the same in subgroups, or align with known percentage distributions (TP + FP) / (total count)
Equal Opportunity - True positive rates are equal for subgroups TP / (TP + FN)
Predictive Equality -  False positive rates are equal for subgroups FP / (FP + TN)
False Negative Rate - False negative rates are equal for subgroups FN / (FN + TP)

### Overall Accuracy 

**Definition:**  Percentage of model predictions that are correct

**Equation:** (TP + TN) / (total count)

**How to interpret:**  

### Statistical Parity

**Definition:**  Percentage of the outputs that the model predicted as positive

**Equation:** (TP + FP) / (total count)

**How to interpret:**  

### Equal Opportunity

**Definition:**  Percentage of positive outcomes that the model predicted correctly

**Equation:** TP / (TP + FN)

**How to interpret:**  

### Predictive Equality

**Definition:**  Percentage of the negative outcomes that the model predicted correctly

**Equation:** FP / (FP + TN)

**How to interpret:**  

### False Negative Rate

**Definition:**  Percentage of positive outcomes that the model did not predict correctly

**Equation:** FN / (FN + TP)

**How to interpret:**  



#### Updates to be made
The above metrics need to be updated and added to in order to analyze these metrics throught the lens of sex. To do this, we can measure each metric for males and females separately, and then subtract the two values from each other. Therefore, if the metric is 0, it is the same for both sexes, if it trends toward 1 or toward -1, it is biased toward one sex.