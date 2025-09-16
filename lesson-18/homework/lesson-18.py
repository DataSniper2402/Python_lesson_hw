
# homework--1
# 1
import pandas as pd 
ta = pd.read_csv('tackoverflow_qa.csv')
q1 = ta[ta['creationdate'] < '2014-01-01']
# 2

q2 = ta[ta['quest_rep'] > 50]

# 3

q3 = ta[(ta['quest_rep'] >= 50) & (ta['quest_rep'] <= 100)]
# 4
import pandas as pd
titanic = pd.read_csv('titanic.csv')
q4 = questions.merge(titanic[titanic['Name'] == 'Scott Boston'],
                     left_on='Id', right_on='QuestionId')

# 5
PassengerId = ['User1', 'User2', 'User3', 'User4', 'User5']
q5 = questions.merge(titanic[titanic['Name'].isin(PassengerId)],
                     left_on='Id', right_on='PassengerId')
# 6
q6 = titanic.merge(titanic[titanic['Name'] == 'Unutbu'],
                     left_on='Id', right_on='PassengerId')
q6 = q6[(q6['creationdate'] >= '2014-03-01') &
        (q6['creationdate'] <= '2014-10-31') &
        (q6['quest_rep'] < 5)]
# 7

q7 = ta[(ta['quest_rep'].between(5, 10)) | (ta['viewcount'] > 10000)]

# 8
answered_by_scott = titanic[titanic['Name'] == 'Scott Boston']['PassengerId']
q8 = ta[ta['Id'].isin(answered_by_scott)]


# homework-3
# 1
import pandas as pd 
df = pd.read_csv("titanic.csv")
print(df.head(5))
# 2

print("Shape:", df.shape)
print(df.info())
print(df.describe(include='all'))

# 3
import matplotlib.pyplot as plt

# Survived bo‘yicha grafik
df['Survived'].value_counts().plot(kind='bar', title="Survival count")
plt.show()

# Pclass bo‘yicha taqsimot
df['Pclass'].value_counts().plot(kind='bar', title="Pclass distribution")
plt.show()

# homework-4
# 1
female_class1_20_30 = df[(df['Sex'] == 'female') &
                         (df['Pclass'] == 1) &
                         (df['Age'].between(20, 30))]

# 2
fare_gt_100 = df[df['Fare'] > 100]

# 3
survived_alone = df[(df['Survived'] == 1) &
                    (df['SibSp'] == 0) &
                    (df['Parch'] == 0)]

# 4
embarked_c_gt_50 = df[(df['Embarked'] == 'C') &
                      (df['Fare'] > 50)]
# 5
with_family = df[(df['SibSp'] > 0) & (df['Parch'] > 0)]
# 6
                           (df['Survived'] == 0)]
# 7

cabin_and_fare_gt_200 = df[df['Cabin'].notna() & (df['Fare'] > 200)]
# 8

odd_passenger_id = df[df['PassengerId'] % 2 == 1]

# 9

unique_ticket = df[df['Ticket'].map(df['Ticket'].value_counts()) == 1]

# 10

miss_class1 = df[(df['Name'].str.contains('Miss')) &
                 (df['Pclass'] == 1) &
                 (df['Sex'] == 'female')]



