# RO11_TP5

### **Authors** : Lara Polachini and Henrique Gundlach Lacerda

---

The following questions are relative to the image below:

![alt text](image.png)

---

### **Question 1:** Enumarate all possible policies

A policy, usually identified as π, is the behavior of an agent in an environment. It is a mapping from states to actions. For example, the policy π:s→a defines: for each state s, the policy tells the agent which action a to take.

So, for this problem, the possible policies are exposed in the table below:

|  π   | Current state | Input | Next State |
|:----:|:--------------:|:-----:|:-----------:|
| π₁  | S₀             | a₁    | S₁          |
| π₂  | S₀             | a₂    | S₂          |
| π₃  | S₁             | a₀    | S₁          |
| π₄  | S₁             | a₀    | S₃          |
| π₅  | S₃             | a₀    | S₀          |
| π₆  | S₂             | a₀    | S₀          |
| π₇  | S₂             | a₀    | S₃          |


### **Question 2:** 

---

![alt text](image-1.png)

---

Using the transition functions:

$$
T(S, a_0, S') =
\begin{pmatrix}
0 & 0 & 0 & 0 \\
0 & 1 - x & 0 & x \\
1 - y & 0 & 0 & y \\
1 & 0 & 0 & 0
\end{pmatrix}
$$


$$
T(S, a_1, S') =
\begin{pmatrix}
0 & 1 & 0 & 0 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0
\end{pmatrix}
$$


$$
T(S, a_2, S') =
\begin{pmatrix}
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0
\end{pmatrix}
$$


And the reward functions:

$$
R(s) =
\begin{cases}
10, & \text{for state } S_3 \\
1,  & \text{for state } S_2 \\
0,  & \text{otherwise}
\end{cases}
$$


we can write the equations for all the different states:

$$
V^{*}(S_{0}) = R(0) + \max_{a} \gamma \, [ T(S_{0}, a_{1}, S_{1})V^{*}(S_{1}) + T(S_{0}, a_{2}, S_{2})V^{*}(S_{2}) ]
$$

$$
V^{*}(S_{0}) = \max_{a} \gamma \, [ V^{*}(S_{1}) + V^{*}(S_{2}) ]
$$

---

$$
V^{*}(S_{1}) = R(1) + \max_{a} \gamma \, [ T(S_{1}, a_{0}, S_{1})V^{*}(S_{1}) + T(S_{1}, a_{0}, S_{3})V^{*}(S_{3}) ]
$$

$$
V^{*}(S_{1}) = \max_{a} \gamma \, [ (1 - x)V^{*}(S_{1}) + xV^{*}(S_{3}) ]
$$

---

$$
V^{*}(S_{2}) = R(2) + \max_{a} \gamma \, [ T(S_{2}, a_{0}, S_{3})V^{*}(S_{3}) + T(S_{2}, a_{0}, S_{0})V^{*}(S_{0}) ]
$$

$$
V^{*}(S_{2}) = 1 + \max_{a} \gamma \, [ yV^{*}(S_{3}) + (1 - y)V^{*}(S_{0}) ]
$$

---

$$
V^{*}(S_{3}) = R(3) + \max_{a} \gamma \, [ T(S_{3}, a_{0}, S_{0})V^{*}(S_{0}) ]
$$

$$
V^{*}(S_{3}) = 10 + \max_{a} \gamma \, [ V^{*}(S_{0}) ]
$$


### **Question 3:** Is there a value for $ x $, such that for all $ \gamma \in [0,1) $ and $ y \in [0,1] $, $ \pi^{*}(S_{0}) = a_{2} $ ? Justify your answer.



### **Question 4:** 
