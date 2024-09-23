import pandas as pd 
import numpy as np 

df = pd.read_csv("data_cleaning_example.csv")
df.drop_duplicates(inplace = True)
df['Ville'].fillna(df['Ville'].mode()[0], inplace=True)
df['Nom'].fillna(df['Nom'].mode()[0], inplace=True)
df['Score'].fillna(df['Score'].mean().astype(int), inplace = True)


median_salary = df['Salaire'].median()
mean_age_above_median = df.loc[df['Salaire'] > median_salary, 'Age'].mean()
mean_age_below_median = df.loc[df['Salaire'] <= median_salary, 'Age'].mean()

df['Age'] = np.where(
        (df['Age'].isnull()) & (df['Salaire'] > median_salary), 
        int(mean_age_above_median),                                  
    
    np.where(
        (df['Age'].isnull()) & (df['Salaire'] <= median_salary),  
        int(mean_age_below_median),                                  
        
        df['Age']  
    )
)

median_age = df['Age'].median()
mean_salary_above_median = df.loc[df['Age']>median_age, 'Salaire'].mean()
mean_salary_below_median = df.loc[df['Age']<= median_age, 'Salaire'].mean()


df['Salaire'] = np.where(
        (df['Salaire'].isnull()) & (df['Age']>median_age), 
        int(mean_salary_above_median),
    
    np.where(
        (df['Salaire'].isnull()) & (df['Age']<= median_age), 
        int(mean_salary_below_median),
    
        df['Salaire']
    )
)
