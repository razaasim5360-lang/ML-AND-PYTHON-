ml(Machine Learning with Python)
Internship
Day 1

Basic Functions - Group of block -

Data Type Required:- Array

Need to Improve - Loops, types of loops , Nested Loop ,Function, Type of Functions , Array , recursive functions

------------_----

Day2 ---

{• what is recursive functions • -> recursive functions call it self unit the given condition is true }

formula :- fact(n)=n*fact(n-1) fact(0)=1

example:- fact(5)=?

n=5 fact(5)=5fact(5-1) fact(5)=5fact(4) fact(4)=5*fact(3) . . . n times until value met✅

fact54321*1 = ?

recurcive

fact(n)=nfact(n-1) n=5 fact(5)=5fact(5-1)

fact(5)=5fact(4) fact(4)=4fact(3) fact(5)=5fact(2) fact(5)=5fact(1) fact(5)=5*fact(0)

back tracking -- return back function -> fun Def. -> Code of Block -> Activation record(Memory Address)

facto(5)=54321

loop - cycle - loop( k= 5 to 1)

result= result*k

!.. (function , loop and Nested loop or array , Recursion .)

 Day 3
def Fact(n): if n== 0: return 1 else: return n * Fact(n-1)

Stack -> LIFO--500,99,77
Day 4
we install Pandas or install Django or Sir nee nahi padhyai

fact. ke hi program hai.....................

def add(n): if n == 0: return 0 else: return n+add(n-1)

n = int(input("enter a number: ")) z = add(n)

print(z)

iska output n number ko n+n+n+n...+0 tak

ML
What is Machine Learning
-> ML is the process in which a computer analyes data,learn patternfrom it,and make predicatoin or desicions automatically.

What is Learnig
-> Learnig is the process of gaining knowledge or improving performance by using experience by using experience, practice, or data.

Day 5
Knowledge = information prodessing

infomation = raw data processing

raw data = from the surrounding

Day 6
Moduels

first mak a main file

and made anoter file called exe_mod import Main file ame and another metod from Main file ame import * (" this can imoprt all fun. from Main file ame ")

dir("pandas")

we have to learn algebra, Static , Calculas , probelity

Duler Theorm

NumPy Provides Two Fundamental Object

N-dimensional Array Object
A Universal Function Object
zero= np.zeros((2, 3)) This create a 2x3 arr, and every value must be 0 one= np.ones((3, 2)) This create a 3x2 arr, and every value must be 1 ranges= np.arange(0, 10, 2) this use as Start , Stop , Skip

Day 7
first we give data to ML then analyses Past Data then trains , Then predicts Output

Application Face rec. , Healthcare, alexa , swiggy, Weather Casting

<!-- ML types -->
ML have Four Types

1. Supervised Learing
and its learned from he past 
mai mere pass input and output hota hai 
     1.  Regression("Agar o/p no. mai arra hai to vo Reg.")
     2. Classification("Agar o/p word ya text mai to vo hai to vo Classification.")

2. Un-Supervised Learing
  mai mere pass input and output nahi hota hai 

3. reinforcement learning

4. semi-supervised learning

<!-- process involved in ML -->
1. Data Gathering
2. Data pre-processing
3. Choose Model
4. Train Model
5. Test Model
6. Tune Model
7. prediction("BEST FITLINE")

<!-- Algorithm -->
1. linear Reg.
2. Logistic Reg.
3. Decision Tree
4. Random Forest
5. K Nearest Neighbors

<!-- linear Reg. -->
liner reg. is a linear modeling approch to 
find a realn btw one or more independent 
Varaible . 

.csv file = comma seprated value 
   name,age,address, 
   aman,18,'bhopal'
    .tsv file = Tab seprated value 
       name age add


<!-- implemented of linear Reg -->
1. Load the lib 
importing the lib


2. Import the dataset


3. Visualize the Data Visualize the dataset


4. split the data into traning and testing set spliting the data into traning and testing set


5. Fit simple Linear reg.


6. predict the test set


7. Visualize the train set result


8. Visualize the test set result


9. Calculating the residuals


Day 8
Today we make a new file called num_liner_reg.py

"num_liner_reg.py" have to use prediect Marks

seaborn use for Advance Graph pandas use for manuplation NumPy use for Array matplotlib Use for make a Graph

Day 9
X kya hI INDEPENDENT Var. Y kya hI DEPENDENT Var.

Eqn of Lin

MSE Squared Error (MSE) is a method us ed to measure how accurately a reg. Model predicts the traget Value EX suppose our model pre how to cal. MSE: mse = 4+4+4+4/4 =5.35

Day 10
A superviesd ML algo. used for Classification problems. is not used for Predicting Contionus Values . its predict the the probablity.

based on sigmod(logistic) fun.

-for ex

0.98 0.18

types of Logistic

binary
Multinomial
Ordinal
and also make logistic_reg.py

Day 11
KNN (K Nearest Neibour) Euclidian Method used to calculate distance b\w two points formula =(\sqrt{(x_{1}+x_{2})^{2}+(y_{1}+y_{2})^{2}})


Day 12 

<!-- Decision Tree -->
decision tree is a supervised ML Algo used for 
classfication and regression . It Make decission 
by Askin a series of que spliting the data intro 
branches

Process of cleaning Data is called

have two criterian
1. Gini 
2. Entropy

also make a file called Decision_tree.py


Day 13

   overfitting and underfitting
       <!-- overfitting -->
       Overfitting happens when a machine 
       learning model learns the training
       data too well.
   
    -- Reason 
    1. noisy Garbage Data 
    2. Complex Model


   -- How To Avoid 
   1. Removing Features
   2. Early stopping the  training 
   3. Complex Model
   4. Training the model with sufficient
   data 
   5. using cross-validating

    <!--  underfitting  -->
      underfitting happens when a machine 
       learning model is too simple to learn 
       the true patterns in data


        -- Reason 
    1. Noisy garbage data 
    2. simple data


    -- How To Avoid 
    1. More training to the model 
    2. Increase the model Complexity 

